## Postgresql

> https://dev.to/stefanopassador/docker-compose-with-python-and-posgresql-33kk

- Build postgresql in docker
    ``` bash
    docker run --name postgres-db -e POSTGRES_PASSWORD=docker -p 5432:5432 -d postgres
    ```

- postgresql db info
    - Host: localhost
    - Port: 5432
    - User: postgres
    - Password: docker


- postgresql command line
    - show current database name and use
        ``` bash
        \c
        ```
    - show current tables
        ``` bash
        \dt
        ```
    
    - show specific table contents
        ``` sql
        SELECT * from accounts
        ```

    - create table
        ``` sql
        CREATE TABLE accounts (
            id int,
            name VARCHAR(50) UNIQUE NOT NULL
        );
        ```
    
    - insert rows to table
        ``` sql
        INSERT INTO accounts (id, name)
        VALUES
        (2, 'user_2'),
        (0, 'user_0'),
        (1, 'user_1'),
        (3, 'user_3');
        ```
    