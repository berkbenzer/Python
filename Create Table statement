import mysql.connector
from mysql.connector import MySQLConnection, Error


try:
    connection = mysql.connector.connect(host='localhost',
                             database='test',
                             user='root',
                             password='xxx')
    if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ", db_Info)
       cursor=connection.cursor()
       cursor.execute("CREATE TABLE TEST.TEST(COLUMN1 INT,CLOUMN2 CHAR);")
       record=cursor.fetchall()
       cursor.close()


except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
