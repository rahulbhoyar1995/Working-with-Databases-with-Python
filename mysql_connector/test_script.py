import mysql.connector
from mysql.connector import Error
import configparser

# Read database connection details from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

try:
    # Connect to MySQL using config settings
    connection = mysql.connector.connect(
        host=config['mysql']['host'],
        database=config['mysql']['database'],
        user=config['mysql']['user'],
        password=config['mysql']['password']
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version: ", db_info)
        
        # Get cursor object
        cursor = connection.cursor()
        
        # Execute query to create the "offers" table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS offers (
            publisher_id INT,
            offer_name VARCHAR(255),
            payout DECIMAL(10, 2),
            multi_reward BOOLEAN,
            -- Add more columns as needed
            PRIMARY KEY (publisher_id)
        )
        """
        cursor.execute(create_table_query)
        
        # Commit changes
        connection.commit()
        
        print("Table 'offers' created successfully.")

except Error as e:
    print("Error while connecting to MySQL:", e)
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
