FROM python:3.8-slim-buster
RUN apt-get update && \
  apt-get install -y netcat && \
  apt-get install vim -y && \
  apt-get install build-essential -y && \
  pip3 install apache-airflow[celery,redis,postgres,crypto]==2.0.0
WORKDIR /root/airflow
COPY config/variables.json variables.json
COPY config/connections.yml connections.yml
COPY config/setup_connections.py setup_connections.py
COPY config/requirements.txt requirements.txt
COPY entrypoint.sh entrypoint.sh
RUN chmod 777 entrypoint.sh
COPY dags/ dags
ENTRYPOINT ["./entrypoint.sh"]

