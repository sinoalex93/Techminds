# #functions
# #block of codes excuted when it call
# #syntax
# #  def function_name(<parameters>):
# #       code to be executed
#
#
# def hello():
#     print("good mrng")
#
# hello()
#
#
# #arguments->values to be passed to a function
# #parameters->values mapped in the function
#
#
# # 2 type of argument
# #1. possional arugument eg:add(5,6)
# #2.keyword argument eg:add(b=5,a=6)
#
# #possional argumment
# def addp(a,b):
#     print(a+b)
#
# addp(4,5)
#
# #keyword argument
# def addk(a,b):
#     print(a+b)
#
# addk(b=7,a=1)
#
# #default value
#
# def addd(a=1,b=1):
#     print(a+b)
#
# addd()
# addd(4,4)
# addd(5)
#
#
# #retrun
# #after retrun funciton will exit
# def addr(a,b):
#     return a+b
# print(addr(5,5))

# #w.a.p. for calculator using functions
# def add(a,b):
#     result=a+b
#     return result
#
# def sub(a,b):
#     result=a-b
#     return result
#
# def mul(a,b):
#     result=a*b
#     return result
#
# def div(a,b):
#     result=a/b
#     return result
#
# print("Basic Calculator\nPlease select the operations you want to perform\n"
#       "1.ADD\n2.Substract\n3.Division\n4.multiplication\n")
# choice=int(input("Select your choice:"))
# value1=int(input("enter your 1st value"))
# value2=int(input("enter your 2nd value"))
#
# if choice==1:
#     print("the result is",add(value1,value2))
# elif choice==2:
#     print("the result is",sub(value1,value2))
# elif choice==3:
#     print("the result is",div(value1,value2))
# elif choice==4:
#     print("the result is",mul(value1,value2))
# else:
#     print("Not a valid choice")

#w.a.p to find factorial of a number
# def factorial(n):
#     factorial=1
#     for i in range(1, n + 1):
#         factorial = factorial * i
#     return factorial
#
#
# print(factorial(5))

# h.w age calculator,BMI cacualtor

#age calculator
def findage(byear):
  #  year_now = date.today().year
    year_now=2026
    age=year_now-byear
    return age

def agecalculator():
    byear=int(input("enter year of birth"))
    print("age is",findage(byear))

agecalculator()

## BMI Calculator
# def calculatebmi(weight,height):
#     bmi=weight/(height**2)
#
#     if bmi < 18.5:
#         return 'Underweight'
#     elif 18.5 <= bmi < 25:
#         return 'Healthy Weight'
#     else:
#         return 'Overweight'
#
#
# weight=float(input("enter weight"))
# height=float(input("enter height"))
# print(calculatebmi(weight,height))