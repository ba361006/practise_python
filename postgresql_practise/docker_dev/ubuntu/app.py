from sqlalchemy import create_engine

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'playground_ubuntu' # this should be the container's name in the network
db_port = '5432'

# Connecto to the database
db_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
db = create_engine(db_string)

if __name__ == '__main__':
    print('Application started')

    # get data in accounts table
    response = db.execute("SELECT * FROM accounts;")
    print("app response: ", response.all())


# get in container and run with the following cammand line
# uvicorn app:app --reload --host 0.0.0.0 --port 80001

# at host machine, send request to 127.0.0.1:8001
# then you should see the response from app.py