import typer
from db_handler import DBHandler

app = typer.Typer()

@app.command()
def insert(
    name: str = typer.Option(..., help="Name of the user"),
    age: int = typer.Option(..., help="Age of the user")
):
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
def get(
    id: int = typer.Option(..., help="ID of the user")
):
    db = DBHandler()
    user = db.get_user_by_id(id)
    print(user or "User not found.")
    db.close()

@app.command()
def update(
    id: int = typer.Option(...),
    name: str = typer.Option(None),
    age: int = typer.Option(None)
):
    db = DBHandler()
    user = db.update_user(id, name, age)
    print(user or "User not found.")
    db.close()

@app.command()
def delete(
    id: int = typer.Option(..., help="ID of the user to delete")
):
    db = DBHandler()
    user = db.delete_user(id)
    print(user or "User not found.")
    db.close()

if __name__ == "__main__":
    app()
