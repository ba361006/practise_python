# -*- coding: utf-8 -*-
from sqlalchemy import create_engine

db_name = "database"  # nosec
db_user = "username"  # nosec
db_pass = "secret"  # nosec
db_host = "playground_db"  # nosec
db_port = "5432"  # nosec

# Connecto to the database
db_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
db = create_engine(db_string)

if __name__ == "__main__":
    print("Application started")

    # get data in accounts table
    response = db.execute("SELECT * FROM accounts;")
    print("app response: ", response.all())
