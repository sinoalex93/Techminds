import sqlite3
conn=sqlite3.connect("first.db")
cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER,
        name VARCHAR(20),
        address VARCHAR(100)
    )
''')

cursor.execute('''
insert into student(id,name,address)
values(1,"sino","gggg")
''')
conn.commit()
conn.close()