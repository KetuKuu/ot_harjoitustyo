import os
import sqlite3



def get_database_connection():
      
    dirname = os.path.dirname(__file__)
    database_directory = os.path.join(dirname, "data")
    db_path = os.path.join(database_directory, "database.sqlite")


    os.makedirs(database_directory, exist_ok=True)

  
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row

    return connection