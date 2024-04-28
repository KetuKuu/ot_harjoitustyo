from database_connection import get_database_connection

class CollectingRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_phone(self, image, series, model_year, price):
        cursor = self._connection.cursor()
        cursor.execute('''
            INSERT INTO phones (image, series, model_year, price) 
            VALUES (?, ?, ?, ?)
        ''', (image, series, model_year, price))
        self._connection.commit()
        print("New phone added")