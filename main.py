import sqlite3 

try:
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('DB init')
    
    # Writing a query to test it out
    query = 'select sqlite_version();'
    cursor.execute(query)
    
    # Fetching the result 
    result = cursor.fetchall()
    print(f'SQLite version is {result}')
    
    cursor.close()
except sqlite3.Error as error:
    print('Error occured - ', error)
finally:
    if sqlite3.Connection:
        sqliteConnection.close()
        print('SQLite connection closed')
        
        