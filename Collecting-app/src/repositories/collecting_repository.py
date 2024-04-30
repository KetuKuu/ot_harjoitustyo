from database_connection import get_database_connection

class CollectingRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_phone(self, d):
        cursor = self._connection.cursor()
        cursor.execute('''
            INSERT INTO phones (image, series, model_year, price) 
            VALUES (?, ?, ?, ?)
        ''', (d["image"], d["series"], d["model_year"], d["price"]))
        self._connection.commit()
        print("New phone added")

    def fetch_data(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM phones')
        print("hakuu")
        return cursor.fetchall()
        
    
collecting_repository = CollectingRepository(get_database_connection())
  