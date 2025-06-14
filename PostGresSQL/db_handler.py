import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

class DBHandler:
    def __init__(self):
        self.db = SessionLocal()

    def insert_user(self, name, age):
        user = User(name=name, age=age)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all_users(self):
        return self.db.query(User).all()

    def get_user_by_id(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user_id, name=None, age=None):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            if name:
                user.name = name
            if age:
                user.age = age
            self.db.commit()
            self.db.refresh(user)
        return user

    def delete_user(self, user_id):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
        return user

    def close(self):
        self.db.close()
