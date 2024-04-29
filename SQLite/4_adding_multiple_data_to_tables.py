import sqlite3

# Sample data for movies
movies_data = [
    ("The Shawshank Redemption", "Frank Darabont", 1994),
    ("The Godfather", "Francis Ford Coppola", 1972),
    ("The Dark Knight", "Christopher Nolan", 2008)
]

# Connect to SQLite database
connection = sqlite3.connect("movies.db")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Insert rows into the Movies table
cursor.executemany("INSERT INTO Movies (Title, Director, Year) VALUES (?, ?, ?)", movies_data)

# Commit changes to the database
connection.commit()
print("Movie Data Added successfully.")
# Close connection
connection.close()
