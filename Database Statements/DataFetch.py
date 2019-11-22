import mysql.connector
from mysql.connector import MySQLConnection, Error



try:
    connection = mysql.connector.connect(host='localhost',
                             database='test',
                             user='root',
                             password='xxxx')
    if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ", db_Info)
       cursor=connection.cursor()
       cursor.execute("select * from test.test;")
       record=cursor.fetchall()
       for row in record:
           print("id={}, name={}, lastname={},email={}".format(row[0], row[1], row[2], row[3], "\n"))
           print("id=", row[0])
           print("name=", row[1])
           print("lastname=", row[2])
           print("email=", row[3], "\n")
       cursor.close()

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


