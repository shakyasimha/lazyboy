import sqlite3
import os 

DB_NAME = 'lazyboy.db'

def init_db():
    """
        Function for initializing sqlite3 upon running the application
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    """
        Now we run queries where we create a new table for the application
        
        Table: Tasks
        Columns:
        - ID (auto generated)
        - TASK_NAME (TEXT)
        - AGE (INTEGER)
        - URGENCY (INTEGER)
        - COMPLETED (INTEGER)
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
    
    