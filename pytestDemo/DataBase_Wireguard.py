import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='private-leadgen-mysql-ny-1-read-only-2-do-user-7297834-0.b.db.ondigitalocean.com',
                                         database='leadgen',
                                         user='jyoti.y_ro',
                                         password='E#twrT#$#%%^TEGE3rse%^',
                                         port = 25060
                                     )

connection.close()


