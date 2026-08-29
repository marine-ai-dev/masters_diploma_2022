import os
import mysql.connector
from mysql.connector import Error


# ПІДКЛЮЧЕННЯ ДО MYSQL
def connect_to_mysql_database():
    try:
        connection = mysql.connector.connect(host=os.environ.get("MYSQL_HOST", "localhost"),
                                             database=os.environ.get("MYSQL_DATABASE"),
                                             user=os.environ.get("MYSQL_USER"),
                                             password=os.environ.get("MYSQL_PASSWORD"),
                                             use_pure=True)

        db_Info = connection.get_server_info()

        print("• Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("• You're connected to database: ", record)
        print("• DB connection = ", connection)
        print()
        return connection

    except Error as e:
        print("ERROR WHILE CONNECTING TO MySQL: ", e)
        print()
        raise SystemExit()
