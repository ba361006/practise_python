CREATE TABLE IF NOT EXISTS accounts (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO accounts (id, name)
VALUES
(2, 'user_2'),
(0, 'user_0'),
(1, 'user_1'),
(3, 'user_3');