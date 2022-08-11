https://dev.to/stefanopassador/docker-compose-with-python-and-posgresql-33kk

this tutorial works with a minor error

just modify 

```python
db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
```
to 

```python
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
```

due to postgresql version