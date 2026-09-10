#input function
# fname=input("enter fname")
# lname=input("enter lnmae")
# print("hello",fname,lname)
# num=input("enter num1")
# num2=input("enter num2")
# sum=int(num) + int(num2)
# print(sum)
#
# num=int(input("enter num1"))
# num2=int(input("enter num2"))
# sum=num + num2
# print(sum)
#arithmetic operators
# x=5
# y=4
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x//y)
# print(x**y)

#comparison operators
#logic operators
# x=10
# y=20
# print(x>y)
# print(x<y)
# print(x>5 and y<10)
# print(x<5 or y>10)
# print(not(x>7))
# print(not(x<5))

#if condition
# a=int(input("enter your age:"))
# if a>=18:
#     print("your are eligible")
#     print("age is: ",a)
# else:
#     print("you are not eligible")

# number=int(input("enter the number:"))
# if number>0:
#     print("number is positive")
# elif number==0:
#     print("number is zero")
# else:
#     print("number is negative")

mark=int(input("enter the mark: "))
if mark>90:
    print("A+")
elif mark<=90 and mark>80:
    print("A")
elif mark<=80 and mark>70:
    print("B+")
elif mark<=70 and mark>60:
    print("B")
elif mark<=60 and mark>50:
    print("C+")
elif mark<=50 and mark>40:
    print("C")
elif mark==40:
    print("D+")
else:
    print("F")