import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData

# Define the database connection URL for SQLite
db_url = 'sqlite:///movies.db'

# Create an SQLAlchemy engine without echoing
engine = sqlalchemy.create_engine(db_url, echo = False)

# Define metadata
metadata = MetaData()

# Define the "Movies" table
movies_table = Table(
    'Movies',
    metadata,
    Column('Title', String),
    Column('Director', String),
    Column('Year', Integer)
)

# Create the "Movies" table if it doesn't exist
metadata.create_all(engine)

# Insert a new record into the "Movies" table
with engine.connect() as conn:
    insert_statement = movies_table.insert().values(
        Title="Don",
        Director="Farhan Akhtar",
        Year=2006
    )
    conn.execute(insert_statement)

# Fetch all records from the "Movies" table
with engine.connect() as conn:
    select_statement = movies_table.select()
    result = conn.execute(select_statement)
    records = result.fetchall()

# Print fetched records
print("All records in the 'Movies' table:")
for record in records:
    print(record)
