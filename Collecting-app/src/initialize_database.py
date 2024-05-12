from database_connection import get_database_connection
import os


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS users;')
    connection.commit()



def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    connection.commit()


def create_phone_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS phones (
            id INTEGER PRIMARY KEY,
            image TEXT,
            series TEXT,
            model_year INTEGER,
            price DECIMAL
        );
    ''')
    connection.commit()


def initialize_database():

    connection = get_database_connection()

    if os.getenv('DROP_TABLES', 'False') == 'True':
        drop_tables(connection)
        create_tables(connection)
        create_phone_table(connection)


if __name__ == "__main__":
    initialize_database()
