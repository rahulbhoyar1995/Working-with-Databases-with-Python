from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User
from pathlib import Path

DB_FILE = Path(__file__).parent / "static_db.sqlite3"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

# Create tables (if not exist)
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
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        if name:
            user.name = name
        if age:
            user.age = age
        self.db.commit()
        return user

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user

    def close(self):
        self.db.close()
