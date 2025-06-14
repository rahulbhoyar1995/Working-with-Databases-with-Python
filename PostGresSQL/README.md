## 📘  PostgreSQL CLI App with SQLAlchemy

### 📌 Overview

This is a simple CLI app built with Python, SQLAlchemy, and PostgreSQL to perform basic database operations like:

* Insert a user
* Get all users
* Get a user by ID
* Update a user
* Delete a user

---

### 🔧 Prerequisites

#### 🐘 Install PostgreSQL

* macOS:

  ```bash
  brew install postgresql
  brew services start postgresql
  ```
* Ubuntu/Debian:

  ```bash
  sudo apt install postgresql postgresql-contrib
  sudo service postgresql start
  ```
* Windows:
  Download installer from: [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)

---

### 🔐 PostgreSQL Setup Instructions (First-Time Only)

1. **Create a PostgreSQL role (if not already created):**

   Open your terminal and run:

   ```bash
   createdb $USER     # Create a DB matching your macOS username
   psql               # Login to PostgreSQL
   ```

   Once inside the `psql` prompt:

   ```sql
   CREATE ROLE postgres WITH LOGIN SUPERUSER PASSWORD 'your_password';
   \q
   ```
2. **Create your target database**:

   ```bash
   createdb testdb
   ```

---

### ⚙️ Environment Setup
1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
2. **Create a `.env` file in the root folder**

   ```ini
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=testdb
   ```

---

### 📁 Project Structure

```
.
├── main.py
├── db_handler.py
├── models.py
├── .env
├── README.md
└── requirements.txt
```

---

### 🚀 Usage

Run commands like this:

#### 🔹 Insert a user

```bash
python3 main.py insert "Alice" 30
```

#### 🔹 Get all users

```bash
python3 main.py get_all
```

#### 🔹 Get a user by ID

```bash
python3 main.py get 1
```

#### 🔹 Update a user

```bash
python3 main.py update 1 "Bob" 35
```

#### 🔹 Delete a user

```bash
python3 main.py delete 1
```

---

### 🛠 Requirements File (`requirements.txt`)

```
SQLAlchemy
click
psycopg2-binary
python-dotenv
```

Install using:

```bash
pip install -r requirements.txt
```

---

### ✅ Troubleshooting

#### ❗ Error: `role "postgres" does not exist`

Run:

```bash
createdb $USER
psql
```

Then inside the prompt:

```sql
CREATE ROLE postgres WITH LOGIN SUPERUSER PASSWORD 'your_password';
\q
```
