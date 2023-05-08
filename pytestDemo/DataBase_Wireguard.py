import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='private-leadgen-mysql-ny-1-read-only-90023-do-user-7297834-0.a.db.ondigitalocean.com',
                                         database='leadgen',
                                         user='jyoti.y_ro',
                                         password='E#twrT#$#%%^TEGE3rse%^')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select ;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to Database", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection")