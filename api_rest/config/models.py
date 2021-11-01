table_definitions = {
    "star_wars.character": {
        "precedence": 3,
        "keys": [
            "character_id",
        ],
        "fields": [
            "character_id",
            "height",
            "mass",
            "planet_id",
            "specie_id",
            "skin_color",
            "eye_color",
            "name",
            "birth_year",
            "gender",
            "hair_color",
        ],
    },
    "star_wars.film": {
        "precedence": 1,
        "keys": [
            "film_id",
        ],
        "fields": [
            "episode_id",
            "film_id",
            "release_date",
            "producer",
            "opening_crawl",
            "title",
            "director",
        ],
    },
    "star_wars.film_character": {
        "precedence": 4,
        "keys": [
            "film_id",
            "character_id"
        ],
        "fields": [
            "film_id",
            "character_id"
        ],
    },
    "star_wars.film_planet": {
        "precedence": 4,
        "keys": [
            "film_id",
            "planet_id"
        ],
        "fields": [
            "film_id",
            "planet_id"
        ],
    },
    "star_wars.film_specie": {
        "precedence": 4,
        "keys": [
            "film_id",
            "specie_id"
        ],
        "fields": [
            "film_id",
            "specie_id"
        ],
    },
    "star_wars.film_starship": {
        "precedence": 4,
        "keys": [
            "film_id",
            "starship_id"
        ],
        "fields": [
            "film_id",
            "starship_id"
        ],
    },
    "star_wars.film_vehicle": {
        "precedence": 4,
        "keys": [
            "film_id",
            "vehicle_id"
        ],
        "fields": [
            "film_id",
            "vehicle_id"
        ],
    },
    "star_wars.planet": {
        "precedence": 1,
        "keys": [
            "planet_id",
        ],
        "fields": [
            "planet_id",
            "orbital_period",
            "diameter",
            "surface_water",
            "population",
            "rotation_period",
            "name",
            "climate",
            "gravity",
            "terrain",
        ],
    },
    "star_wars.specie": {
        "precedence": 2,
        "keys": [
            "specie_id",
        ],
        "fields": [
            "specie_id",
            "average_height",
            "average_lifespan",
            "planet_id",
            "language",
            "name",
            "classification",
            "designation",
        ],
    },
    "star_wars.specie_eye_color": {
        "precedence": 4,
        "keys": [
            "specie_id",
            "eye_color",
        ],
        "fields": [
            "specie_id",
            "eye_color",
        ],
    },
    "star_wars.specie_hair_color": {
        "precedence": 4,
        "keys": [
            "specie_id",
            "hair_color",
        ],
        "fields": [
            "specie_id",
            "hair_color",
        ],
    },
    "star_wars.specie_skin_color": {
        "precedence": 4,
        "keys": [
            "specie_id",
            "skin_color",
        ],
        "fields": [
            "specie_id",
            "skin_color",
        ],
    },
    "star_wars.starship": {
        "precedence": 1,
        "keys": [
            "starship_id",
        ],
        "fields": [
            "starship_id",
            "crew",
            "passengers",
            "cargo_capacity",
            "hyperdrive_rating",
            "mglt",
            "cost_in_credits",
            "length",
            "max_atmosphering_speed",
            "name",
            "model",
            "manufacturer",
            "consumables",
            "starship_class",
        ],
    },
    "star_wars.starship_character": {
        "precedence": 4,
        "keys": [
            "starship_id",
            "character_id",
        ],
        "fields": [
            "starship_id",
            "character_id",
        ],
    },
    "star_wars.vehicle": {
        "precedence": 1,
        "keys": [
            "vehicle_id",
        ],
        "fields": [
            "vehicle_id",
            "length",
            "max_atmosphering_speed",
            "crew",
            "passengers",
            "cargo_capacity",
            "cost_in_credits",
            "name",
            "model",
            "manufacturer",
            "consumables",
            "vehicle_class",
        ],
    },
    "star_wars.vehicle_character": {
        "precedence": 4,
        "keys": [
            "vehicle_id",
            "character_id",
        ],
        "fields": [
            "vehicle_id",
            "character_id",
        ],
    },
}
