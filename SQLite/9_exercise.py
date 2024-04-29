# Exercise statement :
# Create a table called Users
# It should have the columns ID (Primary key), First Name, Last Name, Email Address, Phone number
# Add 10 records to it. 6 of them at least should end with gmail.com
# Use SQLITE3  for this
# Display all the records added

import sqlite3
import random
import string

# Connect to SQLite database
connection = sqlite3.connect("users.db")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Create Users table
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                    ID INTEGER PRIMARY KEY,
                    First_Name TEXT,
                    Last_Name TEXT,
                    Email_Address TEXT,
                    Phone_Number TEXT
                )''')

# Generate 10 records
records = []
for i in range(10):
    first_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    email_suffix = '@gmail.com' if i < 6 else '@example.com'
    email = f"{first_name.lower()}.{last_name.lower()}{email_suffix}"
    phone_number = ''.join(random.choices(string.digits, k=10))
    records.append((first_name, last_name, email, phone_number))

# Insert records into the Users table
cursor.executemany('''INSERT INTO Users (First_Name, Last_Name, Email_Address, Phone_Number) 
                    VALUES (?, ?, ?, ?)''', records)

# Commit changes to the database
connection.commit()

# Fetch all records from the Users table
cursor.execute("SELECT * FROM Users")
all_records = cursor.fetchall()

# Display all records added
print("All records added to the 'Users' table:")
for record in all_records:
    print(record)

# Close connection
connection.close()
