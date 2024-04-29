import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("movies.db")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute a SELECT query to fetch all records from the Movies table
cursor.execute("SELECT * FROM Movies")

# Fetch all records
records = cursor.fetchall()

# Print fetched records
for record in records:
    print(record)

# Close connection
connection.close()
