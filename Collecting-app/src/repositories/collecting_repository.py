from database_connection import get_database_connection

class CollectingRepository:
    def __init__(self, connection):
        self._connection = connection