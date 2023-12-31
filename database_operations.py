import psycopg2
from config import user, host, db_name, password

def connect_to_database():
    try:
        return psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

def execute_query(query, params=None):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
    except psycopg2.Error as e:
        print(f"Error executing the query: {e}")
        # Здесь можно предпринять дополнительные действия в случае ошибки
        raise  # Пробросим исключение выше
    finally:
        if conn is not None:
            conn.close()
            print('Connection closed.')