import minio
import pandas
import psycopg2
import traceback
import logging as log
from io import BytesIO
from uuid import uuid4
from collections import OrderedDict
from flask_restful import Resource, Api
from flask import Flask, request, jsonify
from psycopg2.extras import execute_values

from api_rest.config.models import table_definitions as tb_def
from api_rest.config.vars import database, object_storage, environment, log_level


app = Flask(__name__)
api = Api(app)
log.basicConfig(level=log_level[environment])


class DataReceiver(Resource):

    def put(self):
        """
        Receives json data in below format, saves to object storage and inserts into database.
        {
            data: [
                [
                    schema_1,
                    table_1,
                    {
                        field_1: value_1,
                        field_2: value_2,
                        (...)
                    }
                ],
                [
                    schema_2,
                    table_2,
                    {
                        field_1: value_1,
                        field_2: value_2,
                        (...)
                    }
                ],
                (...)
            ]
        }
        :return: json response with "Success" or "Error"
        """

        data = request.get_json(force=True)
        log.debug(f"Received Data:\n{data}")

        ready_data = OrderedDict()
        current_record = ("",)
        try:

            # Processing Data
            log.info("Starting data conversion.")
            log.debug(f"{len(data)} records received.")
            for record in sorted(data['records'], key=lambda x: tb_def['.'.join(x[0:2])]["precedence"]):
                current_record = record
                table = '.'.join(record[0:2])
                fields = record[2]
                log.debug(f"Expected: {tb_def[table]['fields']} - Current record: {current_record}")
                if table not in ready_data:
                    ready_data[table] = [[fields[field] for field in tb_def[table]['fields']], ]
                else:
                    ready_data[table] += [[fields[field] for field in tb_def[table]['fields']], ]
            log.info("Finished data conversion successfully.")

            # Saving to Object Storage
            log.info("Starting Object Storage Insertion.")
            client = minio.Minio(
                endpoint=f"{object_storage['host']}:{object_storage['port']}",
                access_key=object_storage["user"],
                secret_key=object_storage["password"],
                secure=False
            )

            for table, records in ready_data.items():
                log.debug(f"Generating .parquet for records of {table} table:\n{records}")
                buffer = BytesIO()
                dataframe = pandas.DataFrame(records, columns=tb_def[table]['fields'])
                dataframe.to_parquet(buffer, index=False)
                buffer.seek(0)
                client.put_object(
                    object_storage["bucket"],
                    f"{table.replace('.', '/')}/{uuid4().hex.upper()}.parquet",
                    buffer,
                    length=buffer.getbuffer().nbytes
                )
            log.info("Finished Object Storage Insertion Successfully.")

            log.info("Starting DB batch insertion.")
            with psycopg2.connect(**database) as conn:
                cur = conn.cursor()

                for table, records in ready_data.items():
                    sql = f"""
                        INSERT INTO {table} ({','.join(['"' + field + '"' for field in tb_def[table]['fields']])}) 
                        VALUES %s 
                        ON CONFLICT ({','.join(['"' + key + '"' for key in tb_def[table]['keys']])}) DO NOTHING
                    """
                    log.debug(f"SQL to run: {sql}")
                    log.debug(f"Records to insert: {records}")
                    execute_values(
                        cur=cur,
                        sql=sql[:],
                        argslist=records,
                        page_size=1000
                    )
            log.info("Finished DB batch insertion successfully.")

            result = {"status": "Success"}

        except Exception as e:

            result = {"status": "Error", "message": f"{str(e)}"}
            log.critical(
                f"Current record: {current_record}\n{traceback.format_exc()}"
            )

        return jsonify(result)


api.add_resource(DataReceiver, '/api')


if __name__ == "__main__":
    app.run()
