from database_connection import get_database_connection
import os




def drop_tables(connection):
    print("initialize, Dropping tables...")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS users;')
    connection.commit()
    print("Tables dropped.")


def create_tables(connection):
    print("initialize database,create_tables")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    print("taulu luotu")
    connection.commit()

def initialize_database():
    

    connection = get_database_connection()

    if os.getenv('DROP_TABLES', 'False') == 'True':
        drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()