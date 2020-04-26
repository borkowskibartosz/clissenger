CREATE TABLE users(
	id serial NOT NULL,
	username VARCHAR(255) UNIQUE,
	email VARCHAR(255) UNIQUE,
	hashed_password VARCHAR(255),
	PRIMARY KEY(id)
);