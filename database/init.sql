CREATE SCHEMA star_wars;
CREATE TABLE star_wars.film(
    film_id INT PRIMARY KEY,
    episode_id SMALLINT,
    title VARCHAR(100),
    opening_crawl TEXT,
    director VARCHAR(100),
    producer VARCHAR(200),
    release_date DATE
);
CREATE TABLE star_wars.starship(
    starship_id INT PRIMARY KEY,
    name VARCHAR(50),
    model VARCHAR(200),
    manufacturer VARCHAR(500),
    cost_in_credits BIGINT,
    length FLOAT,
    max_atmosphering_speed INT,
    crew INT,
    passengers INT,
    cargo_capacity BIGINT,
    consumables VARCHAR(50),
    hyperdrive_rating FLOAT,
    mglt INT,
    starship_class VARCHAR(50)
);
CREATE TABLE star_wars.vehicle(
    vehicle_id INT PRIMARY KEY,
    name VARCHAR(50),
    model VARCHAR(200),
    manufacturer VARCHAR(500),
    cost_in_credits BIGINT,
    length FLOAT,
    max_atmosphering_speed INT,
    crew INT,
    passengers INT,
    cargo_capacity INT,
    consumables VARCHAR(50),
    vehicle_class VARCHAR(50)
);
CREATE TABLE star_wars.planet(
    planet_id INT PRIMARY KEY,
    name VARCHAR(100),
    rotation_period INT,
    orbital_period INT,
    diameter INT,
    climate VARCHAR(50),
    gravity VARCHAR(50),
    terrain VARCHAR(50),
    surface_water FLOAT,
    population BIGINT
);
CREATE TABLE star_wars.specie(
    specie_id INT PRIMARY KEY,
    name VARCHAR(50),
    classification VARCHAR(50),
    designation VARCHAR(50),
    average_height INT,
    average_lifespan INT,
    planet_id INT,
    language VARCHAR(50),
    CONSTRAINT fk_planet_1 FOREIGN KEY(planet_id) REFERENCES star_wars.planet(planet_id)
);
CREATE TABLE star_wars.character(
    character_id INT PRIMARY KEY,
    name VARCHAR(100),
    height INT,
    mass FLOAT,
    hair_color VARCHAR(50),
    skin_color VARCHAR(50),
    eye_color VARCHAR(50),
    birth_year VARCHAR(50),
    gender VARCHAR(50),
    planet_id INT,
    specie_id INT,
    CONSTRAINT fk_planet_2 FOREIGN KEY(planet_id) REFERENCES star_wars.planet(planet_id),
    CONSTRAINT fk_specie FOREIGN KEY(specie_id) REFERENCES star_wars.specie(specie_id)
);
CREATE TABLE star_wars.film_starship(
    film_id INT,
    starship_id INT,
    PRIMARY KEY(film_id, starship_id),
    CONSTRAINT fk_rel_film_starship_film FOREIGN KEY(film_id) REFERENCES star_wars.film(film_id),
    CONSTRAINT fk_rel_film_starship_starship FOREIGN KEY(starship_id) REFERENCES star_wars.starship(starship_id)
);
CREATE TABLE star_wars.film_vehicle(
    film_id INT,
    vehicle_id INT,
    PRIMARY KEY(film_id, vehicle_id),
    CONSTRAINT fk_rel_film_vehicle_film FOREIGN KEY(film_id) REFERENCES star_wars.film(film_id),
    CONSTRAINT fk_rel_film_vehicle_vehicle FOREIGN KEY(vehicle_id) REFERENCES star_wars.vehicle(vehicle_id)
);
CREATE TABLE star_wars.film_character(
    film_id INT,
    character_id INT,
    PRIMARY KEY(film_id, character_id),
    CONSTRAINT fk_rel_film_character_film FOREIGN KEY(film_id) REFERENCES star_wars.film(film_id),
    CONSTRAINT fk_rel_film_character_character FOREIGN KEY(character_id) REFERENCES star_wars.character(character_id)
);
CREATE TABLE star_wars.film_planet(
    film_id INT,
    planet_id INT,
    PRIMARY KEY(film_id, planet_id),
    CONSTRAINT fk_rel_film_planet_film FOREIGN KEY(film_id) REFERENCES star_wars.film(film_id),
    CONSTRAINT fk_rel_film_planet_planet FOREIGN KEY(planet_id) REFERENCES star_wars.planet(planet_id)
);
CREATE TABLE star_wars.film_specie(
    film_id INT,
    specie_id INT,
    PRIMARY KEY(film_id, specie_id),
    CONSTRAINT fk_rel_film_specie_film FOREIGN KEY(film_id) REFERENCES star_wars.film(film_id),
    CONSTRAINT fk_rel_film_specie_specie FOREIGN KEY(specie_id) REFERENCES star_wars.specie(specie_id)
);
CREATE TABLE star_wars.starship_character(
    starship_id INT,
    character_id INT,
    PRIMARY KEY(starship_id, character_id),
    CONSTRAINT fk_rel_starship_character_starship FOREIGN KEY(starship_id) REFERENCES star_wars.starship(starship_id),
    CONSTRAINT fk_rel_starship_character_character FOREIGN KEY(character_id) REFERENCES star_wars.character(character_id)
);
CREATE TABLE star_wars.vehicle_character(
    vehicle_id INT,
    character_id INT,
    PRIMARY KEY(vehicle_id, character_id),
    CONSTRAINT fk_rel_vehicle_character_vehicle FOREIGN KEY(vehicle_id) REFERENCES star_wars.vehicle(vehicle_id),
    CONSTRAINT fk_rel_vehicle_character_character FOREIGN KEY(character_id) REFERENCES star_wars.character(character_id)
);
CREATE TABLE star_wars.specie_skin_color(
    specie_id INT,
    skin_color VARCHAR(50),
    PRIMARY KEY(specie_id, skin_color),
    CONSTRAINT fk_rel_specie_skin_color FOREIGN KEY(specie_id) REFERENCES star_wars.specie(specie_id)
);
CREATE TABLE star_wars.specie_hair_color(
    specie_id INT,
    hair_color VARCHAR(50),
    PRIMARY KEY(specie_id, hair_color),
    CONSTRAINT fk_rel_specie_hair_color FOREIGN KEY(specie_id) REFERENCES star_wars.specie(specie_id)
);
CREATE TABLE star_wars.specie_eye_color(
    specie_id INT,
    eye_color VARCHAR(50),
    PRIMARY KEY(specie_id, eye_color),
    CONSTRAINT fk_rel_specie_eye_color FOREIGN KEY(specie_id) REFERENCES star_wars.specie(specie_id)
);

CREATE DATABASE airflow_db;