"""
    This is where the sqlite database is initialized and every sql query is run
"""

import sqlite3
import os 

DB_NAME = 'lazyboy.db'

class QuerySet:
    """
    Class for running the SQL queries on my main runner code
    """
    def __init__(self):
        """ Ctor
        """
        try:
            self.connection = sqlite3.connect(DB_NAME)
            self.cursor = self.connection.cursor()
            self.create_table()
        except sqlite3.Error as error:
            print(f"[sqlite3] [error] ${error}")
        
    def create_table(self):
        """ Function for creating tables
        """
        
        """
        Table: Tasks
        Columns:
            ID (auto generated)
            TASK_NAME (TEXT)
            AGE (INTEGER)
            URGENCY (INTEGER)
            COMPLETED (INTEGER)
        """
        try:
            self.cursor.execute('''
                CREATE TABLE Task(
                    id INTEGER PRIMARY KEY,
                    task_name TEXT,
                    age INTEGER,
                    urgency INTEGER,
                    completed INTEGER
                )
            ''')
        except sqlite3.Error as error:
            print(f'[sqlite3] [error] ${error}')
            
    def close_db(self):
        """Method for closing the connection
        """
        if sqlite3.Connection:
            self.connection.close()
            print("[sqlite3] Connection closed successfully.")
        else:
            print("[sqlite3] [error] Database was never initialized.")
    
    def add(self):
        """Method for adding tasks to the database
        """
        
    
