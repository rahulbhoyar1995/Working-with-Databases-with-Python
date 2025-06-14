
# 📦 PostgreSQL Basics: User, Database & Table Management (No Python)

This guide helps you manage PostgreSQL using only terminal and SQL — great for DBAs or backend engineers.

---

### 🔧 1. Start PostgreSQL (macOS / Linux / Windows)

**macOS (Homebrew):**

```bash
brew services start postgresql
```

**Ubuntu/Debian:**

```bash
sudo service postgresql start
```

---

### 👤 2. Create a PostgreSQL Role (User)

```bash
createuser --interactive --pwprompt
```

You'll be prompted for:

* Role name (e.g., `postgres` or `rahul`)
* Superuser permission (choose `y` if needed)

**Or use SQL inside `psql`:**

```sql
CREATE ROLE postgres WITH LOGIN SUPERUSER PASSWORD 'your_password';
```

---

### 🗃️ 3. Create a PostgreSQL Database

```bash
createdb testdb
```

To create a DB owned by a specific user:

```bash
createdb testdb -O postgres
```

---

### 🔑 4. Connect to PostgreSQL

```bash
psql -U postgres -d testdb
```

> If you're connecting as your system user:

```bash
psql
```

---

### 🧱 5. Create Tables

Inside `psql`:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
);
```

---

### 📋 6. View All Databases

```sql
\l
```

---

### 🔍 7. Connect to a Database

```bash
psql -d testdb
```

Or, inside `psql`:

```sql
\c testdb
```

---

### 📂 8. List All Tables in Current DB

```sql
\dt
```

---

### 🧾 9. Show Table Schema

```sql
\d users
```

---

### 🔎 10. Select Data

```sql
SELECT * FROM users;
```

---

### ✍️ 11. Insert Data

```sql
INSERT INTO users (name, age) VALUES ('Alice', 30);
```

---

### 📝 12. Update Data

```sql
UPDATE users SET age = 31 WHERE name = 'Alice';
```

---

### ❌ 13. Delete Data

```sql
DELETE FROM users WHERE name = 'Alice';
```

---

### 🔄 14. Drop Table or DB

```sql
DROP TABLE users;
DROP DATABASE testdb;
```

---

### 🚪 15. Exit `psql`

```sql
\q
```

---

### 🧠 Tip: Connect with custom port (optional)

```bash
psql -U postgres -d testdb -h localhost -p 5432
```

