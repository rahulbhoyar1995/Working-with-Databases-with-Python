import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

print("Database created successfully.")
