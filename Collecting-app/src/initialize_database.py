from database_connection import get_database_connection

class DataBase:


    def __init__(self, connection, user_repository):
        self._connection = connection
        self._user_repository = user_repository
                 
    def drop_tables(connection):
        
        cursor = connection.cursor() #Connection-olio database_connection

        cursor.execute('''
            drop table if exists users;
        ''')

        connection.commit()


    def create_tables(connection):
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE);
        ''')

        connection.commit()


    def initialize_database():
        connection = get_database_connection()
        DataBase.drop_tables(connection)
        DataBase.create_tables(connection)



    if __name__ == "__main__":
        initialize_database()