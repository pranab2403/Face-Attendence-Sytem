import sqlite3

conn = sqlite3.connect("database/students.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
department TEXT
)
""")

conn.commit()
conn.close()

print("Database Created")