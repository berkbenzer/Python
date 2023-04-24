import mysql.connector
import getpass

# Get user input
password = getpass.getpass("Enter database password: ")
usernames = raw_input("Enter comma-separated list of usernames to check: ")


# Split the list of usernames into individual usernames
usernames_list = [u.strip() for u in usernames.split(",")]

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    database="mysql",
    user="root",
    password=password
)

# Create a cursor object to execute queries
cursor = conn.cursor()

# Loop over each username and execute the query
for username in usernames_list:
    # Execute the query
    query = "SELECT * FROM user WHERE user = %s"
    cursor.execute(query, (username,))

    # Fetch the results
    result = cursor.fetchone()

    # Check if the user was found
    if result:
        print username + " found in the database"
    else:
        print username + " not found in the database"

# Clean up
cursor.close()
conn.close()
