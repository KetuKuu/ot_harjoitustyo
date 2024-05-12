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
     

    def fetch_data(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id, image, series, model_year, price FROM phones")
        return cursor.fetchall()

    def delete_phone(self, phone_id):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM phones WHERE id = ?", (phone_id,))
        self._connection.commit()

    def fetch_phone_stats(self):
        cursor = self._connection.cursor()
        cursor.execute('''
            SELECT COUNT(*) AS total_phones, SUM(price) AS total_value FROM phones
        ''')
        stats = cursor.fetchone()
        return stats if stats else {'total_phones': 0, 'total_value': 0}


collecting_repository = CollectingRepository(get_database_connection())
