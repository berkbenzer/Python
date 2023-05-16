import mysql.connector
import getpass
import os
import subprocess
import psycopg2
import cx_Oracle

# Get database credentials from user raw_input
#password = getpass.getpass("Enter database password: ")

# Connect to databases

def establish_connection():
    conn = mysql.connector.connect(
        database='mysql',
        user='mysql',
        password='mysql'
    )
    return conn

def establish_connection_postgresql():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    return conn

def establish_connection_oracle():
    db_connection_string = 'username/passwort@servicename'
    conn = cx_Oracle.connect(db_connection_string)
    return conn

def close_connection(conn):
    # Close the database connection
    conn.close()

def prompt_confirmation(user_name, user_host):
    # Prompt for confirmation to delete the user
    confirm = raw_input("Are you sure you want to delete %s@'%s'? (Y/N): " % (user_name, user_host))
    return confirm.lower() == "y"


def is_mysql_working():
    command = "ps -ef | grep mysql"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return 0

return_value_mysql = is_mysql_working()


def delete_usernames_mysql(conn, usernames):
    # Delete each username from the database
    for username in usernames:
        # Check if the user exists in the database
        query = "SELECT user, host FROM mysql.user WHERE user = %s"
        cursor = conn.cursor()
        cursor.execute(query, (username,))
        results = cursor.fetchall()

        if results:
            for result in results:
                user_name = result[0]
                user_host = result[1]
                print("%s@'%s' found in the database" % (user_name, user_host))

                if prompt_confirmation(user_name, user_host):
                    delete_user_mysql(conn, user_name, user_host)
                    print("%s@'%s' deleted from the database" % (user_name, user_host))
                else:
                    print("%s@'%s' deletion canceled" % (user_name, user_host))
        else:
            print("%s not found in the database" % username)

def delete_user_mysql(conn, user_name, user_host):
    # Create a cursor for executing the DROP USER query
    cursor = conn.cursor()
    drop_query = "DROP USER %s@%s"
    cursor.execute(drop_query, (user_name, user_host))

    # Commit the changes to the database
    conn.commit()
    cursor.close()


def is_postgresql_working():
    command = "ps -ef | grep postmaster"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return 0

return_value_postgresql = is_postgresql_working()

def delete_usernames_postgresql(conn, usernames):
    # Delete each username from the database
    for username in usernames:
        # Check if the user exists in the database
        query = "select usename from pg_catalog.pg_user where usename = %s"
        cursor = conn.cursor()
        cursor.execute(query, (username,))
        results = cursor.fetchall()

        if results:
            for result in results:
                user_name = result[0]

                print("%s found in the database" % (user_name))

                if prompt_confirmation(user_name):
                    delete_user_mysql(conn, user_name)
                    print("%s deleted from the database" % (user_name))
                else:
                    print("%s deletion canceled" % (user_name))
        else:
            print("%s not found in the database" % username)


def delete_user_postgresql(conn, user_name):
    # Create a cursor for executing the DROP USER query
    cursor = conn.cursor()
    drop_query = "DROP USER %s"
    cursor.execute(drop_query, (user_name))

    # Commit the changes to the database
    conn.commit()
    cursor.close()

def is_oracle_working():
    command = " ps -ef | grep pmon"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return 0

return_value_oracle = is_oracle_working()

def delete_usernames_oracle(conn, usernames):
    # Delete each username from the database
    for username in usernames:
        # Check if the user exists in the database
        query = "select username from all_users where username = %s"
        cursor = conn.cursor()
        cursor.execute(query, (username,))
        results = cursor.fetchall()

        if results:
            for result in results:
                user_name = result[0]

                print("%s found in the database" % (user_name))

                if prompt_confirmation(user_name):
                    delete_user_mysql(conn, user_name)
                    print("%s deleted from the database" % (user_name))
                else:
                    print("%s deletion canceled" % (user_name))
        else:
            print("%s not found in the database" % username)


def delete_user_oracle(conn, user_name):
    # Create a cursor for executing the DROP USER query
    cursor = conn.cursor()
    drop_query = "DROP USER %s CASCADE"
    cursor.execute(drop_query, (user_name))

    # Commit the changes to the database
    conn.commit()
    cursor.close()


def main():
    # Prompt the user for a comma-separated list of usernames to delete
    usernames_input = raw_input("Enter comma-separated list of usernames to delete: ")
    usernames = [username.strip() for username in usernames_input.split(",")]


    if return_value_mysql == 0:
     # Establish a database connection
        conn = establish_connection()
    # Delete the usernames from the database
        delete_usernames_mysql(conn, usernames)
    # Close the database connection
        close_connection(conn)
    elif return_value_postgresql == 0:
        conn = establish_connection_postgresql()
        delete_usernames_postgresql(conn, usernames)
        close_connection(conn)
    else:
        conn = establish_connection_oracle()
        delete_usernames_oracle(conn, usernames)
        close_connection(conn)    

# Entry point of the script
if __name__ == "__main__":
    main()

