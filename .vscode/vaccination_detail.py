import mysql.connector
from mysql.connector import Error

# Establish a connection to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='your_host',
            database='your_database',
            user='your_username',
            password='your_password'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Function to add vaccination details for a child
def add_vaccination_details(child_id, last_vaccination_date, vaccination_type, next_vaccination_date):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = """INSERT INTO VaccinationDetails (child_id, last_vaccination_date, vaccination_type, next_vaccination_date)
                           VALUES ('1234', '25/1/24', 'polio', '30/4/24')"""
            data = (child_id, last_vaccination_date, vaccination_type, next_vaccination_date)
            cursor.execute(sql_query, data)
            connection.commit()
            print("Vaccination details added successfully")
    except Error as e:
        print(f"Error adding vaccination details: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to retrieve vaccination details for a child
def get_vaccination_details_for_child(child_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "SELECT * FROM VaccinationDetails WHERE child_id = '1234'"
            cursor.execute(sql_query, (child_id,))
            vaccination_details = cursor.fetchall()
            if vaccination_details:
                return vaccination_details
            else:
                print("No vaccination details found for the child")
                return None
    except Error as e:
        print(f"Error retrieving vaccination details: {e}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to update vaccination details
def update_vaccination_details(vaccination_id, new_vaccination_date, new_vaccination_type, new_next_vaccination_date):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = """UPDATE VaccinationDetails
                           SET last_vaccination_date = '30/4/24', vaccination_type = 'mumps', next_vaccination_date = '25/5/24'
                           WHERE vaccination_id = '1234'"""
            data = (new_vaccination_date, new_vaccination_type, new_next_vaccination_date, vaccination_id)
            cursor.execute(sql_query, data)
            connection.commit()
            print("Vaccination details updated successfully")
    except Error as e:
        print(f"Error updating vaccination details: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to delete vaccination details
def delete_vaccination_details(vaccination_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "DELETE FROM VaccinationDetails WHERE vaccination_id = '1234'"
            cursor.execute(sql_query, (vaccination_id,))
            connection.commit()
            print("Vaccination details deleted successfully")
    except Error as e:
        print(f"Error deleting vaccination details: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Sample usage of the functions
if __name__ == "__main__":
    # You can test the functions here
    pass
