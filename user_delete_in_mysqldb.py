import mysql.connector
import getpass
# Get database credentials from user raw_input
#password = getpass.getpass("Enter database password: ")

# Connect to database

conn = mysql.connector.connect(

    database='mysql',
    user='root',
    password='db_password'
)


# Prompt the user for a comma-separated list of usernames to delete
usernames_input = raw_input("Enter comma-separated list of usernames to delete: ")
usernames = [username.strip() for username in usernames_input.split(",")]

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

            # Prompt for confirmation to delete the user
            confirm = raw_input("Are you sure you want to delete %s@'%s'? (Y/N): " % (user_name, user_host))

            if confirm.lower() == "y":
                # Create a separate cursor for executing the DROP USER query
                drop_cursor = conn.cursor()
                drop_query = "DROP USER %s@%s"
                drop_cursor.execute(drop_query, (user_name, user_host))

                # Commit the changes to the database
                conn.commit()
                print("%s@'%s' deleted from the database" % (user_name, user_host))
            else:
                print("%s@'%s' deletion canceled" % (user_name, user_host))
    else:
        print("%s not found in the database" % username)

# Close the database connection
conn.close()
