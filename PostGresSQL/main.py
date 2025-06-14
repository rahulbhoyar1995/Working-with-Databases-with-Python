import typer
from db_handler import DBHandler

app = typer.Typer()

@app.command()
def insert(name: str, age: int):
    db = DBHandler()
    user = db.insert_user(name, age)
    print(f"Inserted: {user}")
    db.close()

@app.command(name="get_all")
def get_all_users():
    db = DBHandler()
    users = db.get_all_users()
    for user in users:
        print(user)
    db.close()

@app.command()
def get(id: int):
    db = DBHandler()
    user = db.get_user_by_id(id)
    print(user or "User not found.")
    db.close()

@app.command()
def update(id: int, name: str = None, age: int = None):
    db = DBHandler()
    user = db.update_user(id, name, age)
    print(user or "User not found.")
    db.close()

@app.command()
def delete(id: int):
    db = DBHandler()
    user = db.delete_user(id)
    print(user or "User not found.")
    db.close()

if __name__ == "__main__":
    app()
