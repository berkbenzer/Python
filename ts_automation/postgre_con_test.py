import psycopg2

db_host = "db_host"
db_port = "db_port"
db_name = "db_name"
db_user = "db_user"
db_password = "db_password"

try:
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )

    cursor = connection.cursor()

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
