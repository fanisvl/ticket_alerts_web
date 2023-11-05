import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

def get_upcoming():
    with get_db_connection() as db, db.cursor(buffered=True, dictionary=True) as cursor:
        cursor.execute("SELECT * FROM upcoming_movies")
        return cursor.fetchall()

def get_movie(id):
    with get_db_connection() as db, db.cursor(buffered=True, dictionary=True) as cursor:
        cursor.execute(f"SELECT * FROM upcoming_movies WHERE id={id}")
        return cursor.fetchone()

def post_alert(email, id):
    with get_db_connection() as db, db.cursor(buffered=True, dictionary=True) as cursor:
        insert_query =  "INSERT INTO alerts (email, movie_id) VALUES (%s, %s)"
        cursor.execute(insert_query, (email, id))
        db.commit()