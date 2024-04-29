import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("movies.db")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Create Movies table if it doesn't exist
cursor.execute("""CREATE TABLE IF NOT EXISTS Movies
               (Title TEXT, Director TEXT, Year INT)""")

# Commit changes to the database
connection.commit()
print("Table created successfully.")
# Close connection
connection.close()
