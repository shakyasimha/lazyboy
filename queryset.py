"""
    This is where the sqlite database is initialized and every sql query is run
"""

import sqlite3

DB_NAME = 'lazyboy.db'

class QuerySet:
    """ Class for running the SQL queries on my main runner code """
    def __init__(self):
        """ Ctor """
        try:
            self.connection = sqlite3.connect(DB_NAME)
            self.cursor = self.connection.cursor()
            
            """ Creating table here """
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Task(
                    ID INTEGER PRIMARY KEY, 
                    TASK_NAME TEXT, 
                    AGE INTEGER, 
                    URGENCY INTEGER, 
                    COMPLETED INTEGER
                );
            ''')
            
            self.connection.commit()
            # self.close_db()
        except sqlite3.Error as error:
            print(f"[sqlite3] [error] ${error}")
        
    # def create_table(self):
    #     """ Function for creating tables """
    #     try:
    #         self.cursor.execute('''
    #             CREATE TABLE Task(
    #                 ID INTEGER PRIMARY KEY,
    #                 TASK_NAME TEXT,
    #                 AGE INTEGER,
    #                 URGENCY INTEGER,
    #                 COMPLETED INTEGER
    #             )
    #         ''')
            
    #         self.connection.commit()
    #     except sqlite3.Error as error:
    #         print(f'[sqlite3] [error] ${error}')
            
    def close_db(self):
        """ Method for closing the connection """
        if sqlite3.Connection:
            self.connection.close()
            print("[sqlite3] Connection closed successfully.")
        else:
            print("[sqlite3] [error] Database was never initialized.")

    def drop_db(self):
        """ Method for dropping the table """
        try: 
            self.cursor.execute('DROP TABLE IF EXISTS Task;')
            self.connection.commit()
        except sqlite3.Error as error:
            print(f"[sqlite3] [error] ${error}.")
            
    def add_task(self, task_name, age=0, urgency=0, completed=0):
        """ Method for adding tasks to the database """
        try:
            self.cursor.execute('''
                INSERT INTO Task (TASK_NAME, AGE, URGENCY, COMPLETED)
                VALUES (?,?,?,?);
            ''', (task_name, age, urgency, completed))
            
            self.connection.commit()
        except sqlite3.Error as error:
            print(f'[sqlite3] [error] ${error}')
    
    def fetch_task(self, task_id=None, task_name=None):
        """ Method for retrieving task by id """    
        try: 
            if task_name:
                self.cursor.execute('''
                    SELECT * FROM Task WHERE TASK_NAME=?;
                ''', (task_name,))
                task = self.cursor.fetchone()
                return task if task else None
            
            elif task_id:
                self.cursor.execute('''
                    SELECT * FROM Task WHERE ID=?;
                ''', (task_id,))
                task = self.cursor.fetchone()
                return task if task else None
                
        except sqlite3.Error as error: 
            print(f'[sqlite3] [error] ${error}')
    
    def fetch_all(self):
        """ Method for retrieving all tasks """
        try: 
            self.cursor.execute('''
                SELECT * FROM Task;
            ''')
            tasks = self.cursor.fetchall() 
            return tasks if tasks else None
        except sqlite3.Error as error: 
            print(f'[sqlite3] [error] ${error}')
            
    def remove_task(self, task_name=None, task_id=None):
        """ Method for removing task via id """
        
        try: 
            if task_name: 
                self.cursor.execute('''
                    DELETE FROM Task 
                    WHERE TASK_NAME=?;
                ''', (task_name,))
                self.connection.commit()
                
            elif task_id:
                self.cursor.execute('''
                    DELETE FROM Task 
                    WHERE ID=?;
                ''', (task_id,))
                
                self.connection.commit()
        except sqlite3.Error as error: 
            print(f'[sqlite3] [error] ${error}')
    
