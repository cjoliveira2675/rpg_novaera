# app/database/db.py

from app.services.config_service import load_config
import mysql.connector

config = load_config()
db_config = config['database']

def get_connection():
    return mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        port=db_config.get('port', 3306)
    )
