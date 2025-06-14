# 🗃️ SQLite3 Command-Line App with SQLAlchemy & Typer

This is a simple command-line application to perform CRUD operations on a static SQLite3 database using **Python 3**, **SQLAlchemy**, and **Typer**.

---

## 👨‍💻 Author

Rahul Bhoyar
📍 Berlin, Germany
🧠 AI & Software Professional | DFKI | MBA (AI)

---

## 🛠️ Features

- Persistent `static_db.sqlite3` database (auto-created)
- Uses SQLAlchemy ORM for clean and scalable schema handling
- Typer-powered CLI for intuitive and type-safe commands
- Fully supports: Insert, Read, Update, Delete

---

## 📦 Requirements

- Python 3.7+
- Install dependencies using:

```bash
pip install -r requirements.txt
````

### `requirements.txt` (optional if not created yet)

```
sqlalchemy
typer[all]
```

---

## 🚀 Project Structure

```
sqlite_sqlalchemy_app/
├── models.py           # SQLAlchemy ORM models
├── db_handler.py       # DB session + CRUD logic
├── main.py             # Typer CLI entry point
└── static_db.sqlite3   # Static SQLite DB (auto-created)
```

---

## ⚙️ How to Use

Run all commands using `python3 main.py` followed by a command name and arguments.

### 🔹 Insert a new user

```bash
python3 main.py insert --name Alice --age 30
```

### 🔹 Get all users

```bash
python3 main.py get_all
```

### 🔹 Get user by ID

```bash
python3 main.py get --id 1
```

### 🔹 Update user

```bash
python3 main.py update --id 1 --name "Alice Smith" --age 31
```

### 🔹 Delete user

```bash
python3 main.py delete --id 1
```

---

## ℹ️ Help & Command Info

To see all available commands:

```bash
python3 main.py --help
```

To see help for a specific command:

```bash
python3 main.py insert --help
```

---

## 📌 Notes

* The SQLite database is created as `static_db.sqlite3` in the same folder.
* You can customize or add new models in `models.py`.

---


## 🏁 License

This project is open-source and free to use.
