import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            #database=config['PGSQL_DATABASE'],
            #user=config['PGSQL_USER'],
            #password=config['PGSQL_PASS'],
            #host=config['PGSQL_HOST'],
            database="flask",
            user="postgres",
            password="postgres",
            host="localhost",
            port='5432'
        )
    except DatabaseError as ex:
        raise ex