import sqlite3
conn=sqlite3.connect("mybook.db")
cursor=conn.cursor()

cursor.execute(''' CREATE TABLE Author(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(20),
email VARCHAR(20),
phone INTEGER)  ''')

cursor.execute(''' CREATE TABLE Book(
id INTEGER PRIMARY KEY AUTOINCREMENT,
tittle VARCHAR(20),
desc TEXT,
price INTEGER,
author_id INTEGER,
FOREIGN KEY (author_id) REFERENCES Author(id))  ''')