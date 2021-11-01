import json
import requests
import traceback
from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator


def etl():
    contents = {
        "films": films,
        "people": people,
        "planets": planets,
        "species": species,
        "starships": starships,
        "vehicles": vehicles,
    }

    payload = {
        'records': []
    }

    for content, instance in contents.items():
        current = f"https://swapi.dev/api/{content}"
        while current:
            print(current)
            result = json.loads(requests.get(current).content)
            for record in result["results"]:
                try:
                    payload["records"] += instance(record)
                except Exception as e:
                    print(record)
                    print(traceback.format_exc())
                    raise e
            current = result["next"]

    result = requests.put(
        'http://api_rest:5000/api',
        data=json.dumps(payload)
    )
    print(result.content)


with DAG(
    dag_id='star_wars_extraction',
    start_date=datetime(2021, 1, 1),
    schedule_interval="@once"
) as dag:
    PythonOperator(
        task_id="star_wars_etl",
        python_callable=etl,
        dag=dag
    )


def films(record):

    result = []
    record_fields = {}

    keys = (
        "episode_id",
        "title",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
    )

    for key in keys:
        record_fields[key] = record[key]

    id = record["url"].split("/")[-2]
    record_fields["film_id"] = id

    result.append(["star_wars", "film", record_fields])

    lists = {
        "characters": "character",
        "planets": "planet",
        "starships": "starship",
        "vehicles": "vehicle",
        "species": "specie"
    }

    for key, value in lists.items():
        for item in record[key]:
            result.append(
                [
                    "star_wars",
                    f"film_{value}",
                    {"film_id": id, f"{value}_id": item.split("/")[-2]}
                ]
            )

    return result


def people(record):

    result = []
    record_fields = {}

    keys = (
        "name",
        "hair_color",
        "skin_color",
        "eye_color",
        "birth_year",
        "gender",
    )

    for key in keys:
        record_fields[key] = record[key]

    keys = (
        "height",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        else:
            record_fields[key] = int(record[key].replace(",", ""))

    keys = (
        "mass",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        else:
            record_fields[key] = float(record[key].replace(",", ""))

    id = record["url"].split("/")[-2]
    if record["homeworld"]:
        planet_id = record["homeworld"].split("/")[-2]
    else:
        planet_id = None

    if len(record["species"]) > 1:
        raise Exception
    if record["species"]:
        specie_id = record["species"][0].split("/")[-2]
    else:
        specie_id = None

    record_fields["character_id"] = id
    record_fields["planet_id"] = planet_id
    record_fields["specie_id"] = specie_id

    result.append(["star_wars", "character", record_fields])

    lists = {
        "vehicles": "vehicle",
        "starships": "starship",
    }

    for key, value in lists.items():
        for item in record[key]:
            result.append(
                [
                    "star_wars",
                    f"{value}_character",
                    {"character_id": id, f"{value}_id": item.split("/")[-2]}
                ]
            )

    return result


def planets(record):

    result = []
    record_fields = {}

    keys = (
        "name",
        "climate",
        "gravity",
        "terrain",
    )

    for key in keys:
        record_fields[key] = record[key]

    keys = (
        "rotation_period",
        "orbital_period",
        "diameter",
        "population",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        else:
            record_fields[key] = int(record[key].replace(",", ""))

    keys = (
        "surface_water",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        else:
            record_fields[key] = float(record[key].replace(",", ""))

    id = record["url"].split("/")[-2]
    record_fields["planet_id"] = id

    result.append(["star_wars", "planet", record_fields])

    return result


def species(record):

    result = []
    record_fields = {}

    keys = (
        "name",
        "classification",
        "designation",
        "language",
    )

    for key in keys:
        record_fields[key] = record[key]

    keys = (
        "average_height",
        "average_lifespan",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        else:
            record_fields[key] = int(record[key].replace(",", ""))

    id = record["url"].split("/")[-2]
    if record["homeworld"]:
        planet_id = record["homeworld"].split("/")[-2]
    else:
        planet_id = None

    record_fields["specie_id"] = id
    record_fields["planet_id"] = planet_id

    result.append(["star_wars", "specie", record_fields])

    lists = {
        "skin_colors": "skin_color",
        "hair_colors": "hair_color",
        "eye_colors": "eye_color",
    }

    for key, value in lists.items():
        for item in record[key].split(", "):
            result.append(
                [
                    "star_wars",
                    f"specie_{value}",
                    {"specie_id": id, f"{value}": item}
                ]
            )

    return result


def starships(record):

    result = []
    record_fields = {}

    keys = (
        "name",
        "model",
        "manufacturer",
        "consumables",
        "starship_class"
    )

    for key in keys:
        record_fields[key] = record[key]

    keys = (
        "cost_in_credits",
        "max_atmosphering_speed",
        "passengers",
        "cargo_capacity",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        else:
            record_fields[key] = int(record[key].replace(",", "").replace("km", ""))

    if record["MGLT"] in ("unknown", "n/a", "indefinite"):
        record_fields["mglt"] = None
    else:
        record_fields["mglt"] = int(record["MGLT"].replace(",", ""))

    keys = (
        "crew",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        else:
            record_fields[key] = int(record[key].split("-")[0].replace(",", ""))

    keys = (
        "length",
        "hyperdrive_rating",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        else:
            record_fields[key] = float(record[key].replace(",", ""))

    id = record["url"].split("/")[-2]
    record_fields["starship_id"] = id

    result.append(["star_wars", "starship", record_fields])

    return result


def vehicles(record):

    result = []
    record_fields = {}

    keys = (
        "name",
        "model",
        "manufacturer",
        "consumables",
        "vehicle_class"
    )

    for key in keys:
        record_fields[key] = record[key]

    keys = (
        "cost_in_credits",
        "max_atmosphering_speed",
        "passengers",
        "cargo_capacity",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        elif record[key] == "none":
            record_fields[key] = 0
        else:
            record_fields[key] = int(record[key].replace(",", ""))

    keys = (
        "crew",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        else:
            record_fields[key] = int(record[key].split("-")[0].replace(",", ""))

    keys = (
        "length",
    )

    for key in keys:
        if record[key] in ("unknown", "n/a", "indefinite"):
            record_fields[key] = None
        else:
            record_fields[key] = float(record[key].replace(",", ""))

    id = record["url"].split("/")[-2]
    record_fields["vehicle_id"] = id

    result.append(["star_wars", "vehicle", record_fields])

    return result
