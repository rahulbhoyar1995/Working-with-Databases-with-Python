import sqlalchemy

# Database connection URL for SQLite
db_url = 'sqlite:///movies.db'

# Create an SQLAlchemy engine
engine = sqlalchemy.create_engine(db_url, echo=True)

with engine.connect() as conn:
    # Define the SQL query
    query = sqlalchemy.text("SELECT * FROM Movies")

    # Execute the SQL query
    result = conn.execute(query)

    # Fetch all records
    records = result.fetchall()

    # Print fetched records
    for record in records:
        print(record)
