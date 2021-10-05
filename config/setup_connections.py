import yaml

from airflow import settings
from airflow.models import Connection

with open("./connections.yml", "r") as f:
    connection_dict = yaml.safe_load(f.read())

print(connection_dict)

for connection_name, connection in connection_dict.items():
    print(connection_name)
    print(connection)
    print(connection.get("conn_type"))
    print(connection.get("schema"))

    conn = Connection(
        conn_id=connection_name,
        conn_type=connection.get("conn_type"),
        host=connection.get("host"),
        login=connection.get("login"),
        password=connection.get("password"),
        port=connection.get("port"),
        schema=connection.get("schema"),
        extra=connection.get("extra"),
    )
    session = settings.Session
    session.add(conn)
    session.commit()
