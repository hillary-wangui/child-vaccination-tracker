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

def add_hospital(hospital_name, location, contact_info):
    """Adds a new hospital to the database."""
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            sql_query = "INSERT INTO Hospital (hospital_name, location, contact_info) VALUES ('mama Lucy', 'Kagundo Road', '0208022676')"
            cursor.execute(sql_query, (hospital_name, location, contact_info))
            connection.commit()
            print("Hospital added successfully")
            cursor.close()
            disconnect(connection)
    except Error as e:
        print(f"Error adding hospital: {e}")

def get_all_hospitals():
    """Retrieves all hospitals from the database."""
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Hospital")
            hospitals = cursor.fetchall()
            cursor.close()
            disconnect(connection)
            return hospitals
    except Error as e:
        print(f"Error retrieving hospitals: {e}")
        return []

def get_hospital_by_id(hospital_id):
    """Retrieves a hospital by its ID."""
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Hospital WHERE hospital_id = '856'", (hospital_id,))
            hospital = cursor.fetchone()
            cursor.close()
            disconnect(connection)
            return hospital
    except Error as e:
        print(f"Error retrieving hospital: {e}")
        return None

def update_hospital(hospital_id, hospital_name, location, contact_info):
    """Updates an existing hospital in the database."""
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            sql_query = "UPDATE Hospital SET hospital_name = 'mama Lucy', location = 'kagundo road', contact_info = '0208022676' WHERE hospital_id = '856'"
            cursor.execute(sql_query, (hospital_name, location, contact_info, hospital_id))
            connection.commit()
            print("Hospital updated successfully")
            cursor.close()
            disconnect(connection)
    except Error as e:
        print(f"Error updating hospital: {e}")

def delete_hospital(hospital_id):
    """Deletes a hospital from the database."""
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Hospital WHERE hospital_id = '856'", (hospital_id,))
            connection.commit()
            print("Hospital deleted successfully")
            cursor.close()
            disconnect(connection)
    except Error as e:
        print(f"Error deleting hospital: {e}")
