import psycopg2
import getpass

# Get user input
usernames = input("Enter comma-separated list of usernames to check: ")
password = getpass.getpass("Enter database password: ")

# Split the list of usernames into individual usernames
usernames_list = [u.strip() for u in usernames.split(",")]

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="yourdatabase",
    user="yourusername",
    password=password
)

# Create a cursor object to execute queries
cursor = conn.cursor()

# Loop over each username and execute the query
for username in usernames_list:
    # Execute the query
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))

    # Fetch the results
    result = cursor.fetchone()

    # Check if the user was found
    if result:
        print(f"{username} found in the database")
    else:
        print(f"{username} not found in the database")

# Clean up
cursor.close()
conn.close()
