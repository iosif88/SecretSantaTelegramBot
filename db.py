import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD
from handlers import get_user_id

def connect_to_database():
    try:
        return psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

def execute_query(query, params=None):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT user_telegram_id FROM users")
            user_telegram_id = cursor.fetchall()
            if not any(user_telegram_id in id_tuple for id_tuple in get_user_id):
                print (f"{user_telegram_id}!!!!!!!!!!!!!!!{get_user_id}")
                cursor.execute(query)
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error executing the query: {e}")
        raise
    finally:
        if conn is not None:
            conn.close()
            print('Connection closed.')