import mysql.connector
from mysql.connector import MySQLConnection, Error
import subprocess
db = mysql.connector.connect(host='127.0.0.1',
                             user='root',
                             passwd='xxx'
                             )
cursor = db.cursor()
if db.is_connected():
    db_Info = db.get_server_info()
    print("Connected to MySQL database... MySQL Server version on ", db_Info)




with open(r'C:\Users\xxxxx\Documents\mysql\import.txt', newline='') as f:
    for lines in f:
        fields = lines.rstrip().split(";")
        first = str(fields[0])
        second = str(fields[1])
        third = str(fields[2])
        fourth = str(fields[3])
        sql = "INSERT INTO `test`.`deneme` (`ID`, `FIRSTNAME`,`LASTNAME`,`EMAIL`) VALUES ('%s', '%s', '%s', '%s');" % (first, second, third, fourth)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()




#############import.txt####################

5;test;test;test@gmail.com
6;test1;test1;test1@gmail.com
7;test2;test2;test2@gmail.com
8;test3;test3;test3@gmail.com



##############output###################
Connected to MySQL database... MySQL Server version on  5.7.25-log
INSERT INTO `test`.`deneme` (`ID`, `FIRSTNAME`,`LASTNAME`,`EMAIL`) VALUES ('5', 'test', 'test', 'test@gmail.com');
INSERT INTO `test`.`deneme` (`ID`, `FIRSTNAME`,`LASTNAME`,`EMAIL`) VALUES ('6', 'test1', 'test1', 'test1@gmail.com');
INSERT INTO `test`.`deneme` (`ID`, `FIRSTNAME`,`LASTNAME`,`EMAIL`) VALUES ('7', 'test2', 'test2', 'test2@gmail.com');
INSERT INTO `test`.`deneme` (`ID`, `FIRSTNAME`,`LASTNAME`,`EMAIL`) VALUES ('8', 'test3', 'test3', 'test3@gmail.com');

Process finished with exit code 0



