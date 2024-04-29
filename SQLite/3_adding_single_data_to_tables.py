import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("movies.db")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Insert a single record into the Movies table
single_record = ("Inception", "Christopher Nolan", 2010)
cursor.execute("INSERT INTO Movies (Title, Director, Year) VALUES (?, ?, ?)", single_record)

# Commit changes to the database
connection.commit()

print("Data Added Successfully.")

# Close connection
connection.close()
