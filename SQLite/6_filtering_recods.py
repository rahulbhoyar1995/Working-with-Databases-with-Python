import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("movies.db")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define the release year to filter
release_year = (1972,)

# Execute the SELECT query with a WHERE clause to filter records by release year
cursor.execute("SELECT * FROM Movies WHERE Year = ?", release_year)

# Fetch filtered records
filtered_records = cursor.fetchall()

# Print filtered records
print("Movies released in 1972:")
for record in filtered_records:
    print(record)

# Close connection
connection.close()
