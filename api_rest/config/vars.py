import logging


environment = "PROD"
log_level = {
    "DEV": logging.DEBUG,
    "UAT": logging.INFO,
    "PROD": logging.ERROR,
}
object_storage = {
    "host": "object_storage",
    "port": "9000",
    "user": "blu_champion",
    "password": "blu_challenge_accepted",
    "bucket": "datalake",
}
database = {
    "host": "database",
    "port": "5432",
    "user": "blu_champion",
    "password": "blu_challenge_accepted",
    "database": "data_warehouse",
}
