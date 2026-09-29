import sqlite3
conn=sqlite3.connect("taskmanagement.db")
cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY, AUTO_INCREMENT,
        taskname VARCHAR(20),
        taskdes TEXT
    )
''')
conn.close()
def addtask():
    conn=sqlite3.connect("taskmanagement.db")
    cursor=conn.cursor()
    name=input("Enter Task Name")
    desc=input("Enter Tak Description")
    
    cursor.execute('''
    insert into tasks(?,?)
    values(name,desc)

    ''')

def viewtask():
     conn=sqlite3.connect("taskmanagement.db")
     cursor=conn.cursor()
     cursor.execute('''
        SELECT * FROM tasks
     ''')
     data=cursor.fetchall() #
     print("Task Found")
     for i in data:
          print(f"{i[0]}--task name--{i[1]}, task desc--{i[2]}")


def serachtask():
     conn=sqlite3.connect("taskmanagement.db")
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
    conn=sqlite3.connect("taskmanagement.db")
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
    conn=sqlite3.connect("taskmanagement.db")
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

def main():
     print("TASK MANAGEMENT")
     while True:
          ch=int(input("enter your choice\n1.Add Task\n2.view Task\n3.serach task\n4.edit task\n5.delete task\n6.exit\n"))
          if ch==1:
               addtask()
          elif ch==2:
               viewtask()
          elif ch==3:
               serachtask()
          elif ch==4:
                edittask()
          elif ch==5:
               deletetask()
          elif ch==6:
               break

main()