-- Users table
CREATE TABLE users
(
    id serial NOT NULL,
    username VARCHAR(255) UNIQUE,
    email VARCHAR(255) UNIQUE,
    hashed_password VARCHAR(255),
    PRIMARY KEY(id)
);

-- Messages table
CREATE TABLE messages
(
    id serial NOT NULL,
    from_user int NOT NULL,
    to_user int NOT NULL,
    context text,
    created_at timestamp,
    PRIMARY KEY(id),
    FOREIGN KEY(from_user)
        REFERENCES users(id),
    FOREIGN KEY(to_user)
        REFERENCES users(id)
);