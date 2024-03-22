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

# Function to link hospital to MoH branch
def link_hospital_to_moh(hospital_id, branch_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "INSERT INTO Hospital_MoH_Branches (hospital_id, branch_id) VALUES ('856', '976')"
            data = (hospital_id, branch_id)
            cursor.execute(sql_query, data)
            connection.commit()
            print("Hospital linked to MoH branch successfully")
    except Error as e:
        print(f"Error linking hospital to MoH branch: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to retrieve hospitals linked to a specific MoH branch
def get_hospitals_for_moh_branch(branch_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = """SELECT h.*
                           FROM Hospital h
                           INNER JOIN Hospital_MoH_Branches hm ON h.hospital_id = hm.hospital_id
                           WHERE hm.branch_id ='976'"""
            cursor.execute(sql_query, (branch_id,))
            hospitals = cursor.fetchall()
            if hospitals:
                return hospitals
            else:
                print("No hospitals linked to the MoH branch")
                return None
    except Error as e:
        print(f"Error retrieving hospitals for MoH branch: {e}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Sample usage of the functions
if __name__ == "__main__":
    # You can test the functions here
    pass
