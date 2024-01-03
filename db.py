import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

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

def execute_query(query,curent_id,params=None,):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT user_telegram_id FROM users")
            user_telegram_id = cursor.fetchall()
            if not any(curent_id in id_tuple for id_tuple in user_telegram_id):
                print(f"{user_telegram_id}!!!!!!!!!!!!!!!{curent_id}")
                cursor.execute(query)
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error executing the query: {e}")
        raise
    finally:
        if conn is not None:
            conn.close()
            print('Connection closed.')