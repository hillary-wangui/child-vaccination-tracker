import mysql.connector
from mysql.connector import Error

# Establish a connection to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='your_host',
            database='your_database',
            user='root',
            password='Niajaime@22'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Function to add a new Ministry of Health branch
def add_moh_branch(branch_name, location, contact_info):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "INSERT INTO MoHBranch (branch_name, location, contact_info) VALUES ('afya house', 'cathedral road', 'o202717077')"
            data = (branch_name, location, contact_info)
            cursor.execute(sql_query, data)
            connection.commit()
            print("Ministry of Health branch added successfully")
    except Error as e:
        print(f"Error adding Ministry of Health branch: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to retrieve all Ministry of Health branches
def get_all_moh_branches():
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "SELECT * FROM MoHBranch"
            cursor.execute(sql_query)
            branches = cursor.fetchall()
            if branches:
                return branches
            else:
                print("No Ministry of Health branches found")
                return None
    except Error as e:
        print(f"Error retrieving Ministry of Health branches: {e}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to update a Ministry of Health branch
def update_moh_branch(branch_id, new_branch_name, new_location, new_contact_info):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = """UPDATE MoHBranch
                           SET branch_name = 'afya house;, location = 'cathedral road', contact_info = '0202717077'
                           WHERE branch_id = '976'"""
            data = (new_branch_name, new_location, new_contact_info, branch_id)
            cursor.execute(sql_query, data)
            connection.commit()
            print("Ministry of Health branch updated successfully")
    except Error as e:
        print(f"Error updating Ministry of Health branch: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to delete a Ministry of Health branch
def delete_moh_branch(branch_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "DELETE FROM MoHBranch WHERE branch_id = '976'"
            cursor.execute(sql_query, (branch_id,))
            connection.commit()
            print("Ministry of Health branch deleted successfully")
    except Error as e:
        print(f"Error deleting Ministry of Health branch: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Sample usage of the functions
if __name__ == "__main__":
    # You can test the functions here
    pass
