CREATE TABLE IF NOT EXISTS solutions (
    id SERIAL NOT NULL,
    size integer NOT NULL,
    board integer[][],
    PRIMARY KEY (id)
);
