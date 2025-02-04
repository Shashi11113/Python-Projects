import sqlite3

def cleanup_test_data():
    connection = sqlite3.connect('waamo.db')
    cursor = connection.cursor()
    # Delete test data from tables if necessary
    cursor.execute('DELETE FROM contacts WHERE name = "Test User"')
    cursor.execute('DELETE FROM menu_items WHERE name = "Borito"')
    connection.commit()
    connection.close()
