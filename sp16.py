#file handle
#1.text base file
#file read
# file1=open("hello.txt","r")
# print(file1.read())
# file1.close()

#file write
#file write is overwrite the file
# file1=open("sino.txt","w")
# file1.write("nithin")
# file1.close()

#file append
#it append the condent to file ratherthan overwite
# file1=open("fileappend.txt","a")
# for i in range(10):
#     file1.write(f"\n hai sino")
# file1.close()


#more better way
# with open("hello.txt","r") as f1:
#     print(f1.read())
#

#os module
import os
from logging import exception

#os.mkdir("myprojects")#create new folder
# os.rmdir("myprojects")
# os.rename("hello.txt","h1.txt")#to rename the file
# os.remove("h1.txt")#to remove the file
# path="C:\\Users\\sinoa\\OneDrive\\Desktop\\test.txt.txt"
# if os.path.exists(path):
#     if os.path.isdir(path):
#         print("folder")
#     elif os.path.isfile(path):
#         print("file")



#### exceptions---> events that affects the execution of a program
# try:
#     a=5
#     b=0
#     print(a/b)
# except Exception as e:
#     print(e)
#
# print("haiii")


##multiple exception handling
# try:
#     a=int(input("::--"))
#     b=0
#     print(a/b)
# except ZeroDivisionError:
#     print("cant divide by zero")
# except TypeError:
#     print("check type")
# except ValueError:
#     print("check value")
# finally:
#     print("always execute")
#

class myerror(Exception):
    pass  ## same as continue

age=17
if age <=18:
    raise(myerror("age should be 18"))

