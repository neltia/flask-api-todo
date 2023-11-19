from elasticsearch_dsl import connections
from dotenv import load_dotenv
import os


def es_init():
    load_dotenv(verbose=True)

    # es host info
    es_api_key = os.getenv("ES_API_KEY")
    es_host = os.getenv("ES_HOST")
    es_port = os.getenv("ES_PORT")

    # es ssl key (vagrant/virtualbox 8.10.4)
    # cp /etc/elasticsearch/certs/http_ca.crt /vagrant
    ca_file_path = os.getenv("ES_CRT_PATH")

    # connection create
    connections.create_connection(
        hosts=[f"https://{es_host}:{es_port}"],
        ca_certs=ca_file_path,
        api_key=es_api_key
    )
