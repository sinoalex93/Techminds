import sqlite3
conn=sqlite3.connect("taskmanagement1.db")
cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY, AUTOINCREMENT,
        username VARCHAR(20),
        password TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY, AUTOINCREMENT,
        taskname VARCHAR(20),
        taskdes TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(id))

    )
''')
conn.close()

def register():
    conn=sqlite3.connect("taskmanagement1.db")
    cursor=conn.cursor()
    username=input("enter username::")
    password=input("enter password::")
    cursor.execute('''
    INSERT INTO user(username,password)
    values(?,?)
    ''',(username,password))
    conn.commit()
    print("user registered")

def login():
    conn=sqlite3.connect("taskmanagement1.db")
    cursor=conn.cursor()
    username=input("enter username::")
    password=input("enter password::")
    cursor.execute('''
    SELECT id from user WHERE username = ? AND password = ?
    ''',(username,password))

    user=cursor.fetchone()
    if user:
        print(user)
    else:
        print("invalid login")


def main():
    print("WELCOME TO TASK MANAGEMENT")
    while True:
        ch=int(input("1.Register\n2.Login\n3.Exit"))
        if ch==1:
            register()
        elif ch==2:
            user_id=login()
            sub(user_id)
        elif ch==3:
         break

def addtask():
    conn=sqlite3.connect("taskmanagement1.db")
    cursor=conn.cursor()
    name=input("Enter Task Name")
    desc=input("Enter Tak Description")
    
    cursor.execute('''
    insert into tasks(taskname,taskdes)
    values(?,?)

    ''')

def viewtask():
     conn=sqlite3.connect("taskmanagement1.db")
     cursor=conn.cursor()
     cursor.execute('''
        SELECT * FROM tasks
     ''')
     data=cursor.fetchall() #
     print("Task Found")
     for i in data:
          print(f"{i[0]}--task name--{i[1]}, task desc--{i[2]}")


def serachtask():
     conn=sqlite3.connect("taskmanagement1.db")
     cursor=conn.cursor()
     t_id=int(input("enter the task id"))
     cursor.execute("SELECT * FROM tasks WHERE id=?",(t_id,))
     task=cursor.fetchone()
     if task:
          print("task found")
          print(f"---{task[0]}---{task[1]}---{task[2]}")
     else:
          print("no task found")
 
def edittask():
    conn=sqlite3.connect("taskmanagement1.db")
    cursor=conn.cursor()
    t_id=int(input("enter the task id"))
    name=input("enter task name")
    desc=input("enter task desc")
    cursor.execute(''' 
    UPDATE tasks SET taskname=? , taskdes=? WHERE id=?
    ''',(name,desc,t_id))
    conn.commit()
    print("task updated")
     
def deletetask():
    conn=sqlite3.connect("taskmanagement1.db")
    cursor=conn.cursor()
    t_id=int(input("enter the task id"))
    ch=input("are you want to delete this y/n")
    if ch=="y":
         cursor.execute(''' 
         DELETE FROM tasks WHERE id=? 
        ''',(t_id,))
         conn.commit()
         print("deleted")
    else:
         print("not deleted")

def sub(user_id):
     print("TASK MANAGEMENT")
     while True:
          ch=int(input("enter your choice\n1.Add Task\n2.view Task\n3.serach task\n4.edit task\n5.delete task\n6.exit\n"))
          if ch==1:
               addtask(user_id)
          elif ch==2:
               viewtask(user_id)
          elif ch==3:
               serachtask(user_id)
          elif ch==4:
                edittask(user_id)
          elif ch==5:
               deletetask(user_id)
          elif ch==6:
               break
main()