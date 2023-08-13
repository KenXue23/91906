import pymysql

def connect_database():
    try:
        # Connect to the MySQL database
        con = pymysql.connect(host='localhost', user='root', password='9603')
        return con
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_database():
    con = connect_database()
    if con:
        try:
            with con.cursor() as cursor:
                # Create the 'userdata' database if it doesn't exist
                cursor.execute("CREATE DATABASE IF NOT EXISTS userdata")
            con.commit()
        except pymysql.Error as e:
            print(f"Error creating database: {e}")
        finally:
            con.close()

def create_table():
    con = connect_database()
    if con:
        try:
            with con.cursor() as cursor:
                cursor.execute("USE userdata")
                # Create the 'data' table with columns: id, username, password, email
                cursor.execute("CREATE TABLE IF NOT EXISTS data (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, username VARCHAR(50), password VARCHAR(200), email VARCHAR(50))")
            con.commit()
        except pymysql.Error as e:
            print(f"Error creating table: {e}")
        finally:
            con.close()

def insert_user(username, password, email):
    con = connect_database()
    if con:
        try:
            with con.cursor() as cursor:
                cursor.execute("USE userdata")
                # Insert a new user into the 'data' table
                query = "INSERT INTO data (username, password, email) VALUES (%s, %s, %s)"
                cursor.execute(query, (username, password, email))
            con.commit()
            return True
        except pymysql.Error as e:
            print(f"Error inserting user: {e}")
        finally:
            con.close()
    return False

def check_user(email_or_username, password):
    con = connect_database()
    if con:
        try:
            with con.cursor() as cursor:
                cursor.execute("USE userdata")
                # Check if a user exists in the 'data' table with the provided email/username and password
                query = "SELECT * FROM data WHERE (username=%s OR email=%s) AND password=%s"
                cursor.execute(query, (email_or_username, email_or_username, password))
                row = cursor.fetchone()
                if row:
                    return True
        except pymysql.Error as e:
            print(f"Error checking user: {e}")
        finally:
            con.close()
    return False
