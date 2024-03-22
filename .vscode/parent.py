import mysql.connector
from mysql.connector import Error

def connect():
    """Establishes a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='vaccination tracker',
            user='root',
            password='Niajaime@22'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def disconnect(connection):
    """Closes the connection to the MySQL database."""
    if connection.is_connected():
        connection.close()
        print("Connection to MySQL database closed")

def add_parent(parent_name, contact_info):
    """Adds a parent to the database."""
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            sql_query = "INSERT INTO Parent (parent_name, contact_info) VALUES ('Silvia Wanjeri', '0791009842')"
            cursor.execute(sql_query, (parent_name, contact_info))
            connection.commit()
            print("Parent added successfully")
            cursor.close()
            disconnect(connection)
    except Error as e:
        print(f"Error adding parent: {e}")

def update_parent(parent_id, new_parent_name, new_contact_info):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            sql_query = """UPDATE parent
                           SET parent_name = 'James Oduor', contact_info = '0112825864',
                           WHERE parent_id = '41939159'"""
            data = (parent_id, new_parent_name, new_contact_info)
            cursor.execute(sql_query, data)
            connection.commit()
            print("parent details updated successfully")
    except Error as e:
        print(f"Error updating parent details: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def delete_parent(parent_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            sql_query = "DELETE FROM parent WHERE parent_id = '41939159'"
            cursor.execute(sql_query, (parent_id,))
            connection.commit()
            print("parent deleted successfully")
    except Error as e:
        print(f"Error deleting parent: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    