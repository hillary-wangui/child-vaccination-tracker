import mysql.connector
from mysql.connector import Error

# Establish a connection to the MySQL database
def connect_to_database():
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

# Function to add a new child
def add_child(parent_id, child_name, age, gender, weight):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = """INSERT INTO Child (parent_id, child_name, age, gender, weight)
                           VALUES ('6446318', 'Nia jaime', '1 year', 'F', '11 kgs')"""
            data = (parent_id, child_name, age, gender, weight)
            cursor.execute(sql_query, data)
            connection.commit()
            print("Child added successfully")
    except Error as e:
        print(f"Error adding child: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to retrieve all children for a given parent
def get_children_for_parent(parent_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "SELECT * FROM Child WHERE parent_id = '6446318'"
            cursor.execute(sql_query, (parent_id,))
            children = cursor.fetchall()
            if children:
                return children
            else:
                print("No children found for the parent")
                return None
    except Error as e:
        print(f"Error retrieving children: {e}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to update child details
def update_child(child_id, new_child_name, new_age, new_gender, new_weight):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = """UPDATE Child
                           SET child_name = 'Nia Jaime', age = '2 years', gender = 'F', weight = '15kgs'
                           WHERE child_id = '1234'"""
            data = (new_child_name, new_age, new_gender, new_weight, child_id)
            cursor.execute(sql_query, data)
            connection.commit()
            print("Child details updated successfully")
    except Error as e:
        print(f"Error updating child details: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to delete a child
def delete_child(child_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "DELETE FROM Child WHERE child_id = '1234'"
            cursor.execute(sql_query, (child_id,))
            connection.commit()
            print("Child deleted successfully")
    except Error as e:
        print(f"Error deleting child: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Sample usage of the functions
if __name__ == "__main__":
    # You can test the functions here
    pass
