"""
    This is where the sqlite database is initialized and every sql query is run
"""

import sqlite3
import os 

DB_NAME = 'lazyboy.db'

def init_db():
    """Function for initializing sqlite
    """
    try: 
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        
        """Now we run queries where we create a new table for the application
        
        Table: Tasks
        Columns:
            ID (auto generated)
            TASK_NAME (TEXT)
            AGE (INTEGER)
            URGENCY (INTEGER)
            COMPLETED (INTEGER)
        """
        cursor.execute('''
            CREATE TABLE Task(
                ID INTEGER PRIMARY KEY,
                TASK_NAME TEXT,
                AGE INTEGER, 
                URGENCY INTEGER,
                COMPLETED INTEGER
            );
        ''')
    except sqlite3.Error as error:
        print('Error occured - ', error)
    finally:
        if sqlite3.Connection:
            sqlite_connection.close()
            print("Connecetion closed successfully")
            
    
