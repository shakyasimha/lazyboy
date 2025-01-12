import unittest 
import sqlite3
from queryset.QuerySet import create_table, add_task, remove_task, fetch_task, fetch_all

class TestQueries(unittest.TestCase):
    def test_entries(self):
        """ Test cases will be written here
        """
        def set_up(self):
            """ Setting up an in-memory database before each test. """
            self.conn = sqlite3.connect(':memory:') # In-memory database 
            self.cursor = self.conn.cursor() 
            create_table()
            
        def tear_down(self):
            """ Clean up the database after each test """
            self.conn.close()
        
        def test_create_table(self):
            """ Test if the table has been created """
            ## Create a table 
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Task'")
            
            ## Fetches the created table
            table = self.cursor.fetchone() 
            
            ## Checks and asserts if the table exists or not
            self.assertIsNotNone(table) 
            
        def test_add_task(self):
            """ Test if the tasks can be added correctly """
            add_task('Test Task', 1, 1, 1)
            self.cursor.execute("SELECT * FROM Task WHERE TASK_NAME='Test Task'")
            task = self.cursor.fetchone() 
            self.assertIsNotNone(task)
            self.assertEqual(task[1], 'Test Task')
            
        def test_get_task_by_id(self):
            
            
        