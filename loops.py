#while loop
#print upto 10
# i=0
# while i<=10:
#     print (i)
#     i+=1

#print upto 100
# i=0
# while i<=100:
#     print (i)
#     i+=1

#sum of numbers
# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i+=1
# print("sum is",sum)

#print 1st 10 even numbers
# count=1
# evennum=1
# while count<=10:
#     if evennum%2==0:
#         print("even numbers:",evennum)
#         count+=1
#     evennum+=1

#print 1st 10 odd numbers

# count=1
# oddnum=1
# while count<=10:
#     if oddnum%2!=0:
#         print("odd numbers:",oddnum)
#         count+=1
#     oddnum+=1

#print multiplication table of 5

# count=1
# a=1
# while count<=10:
#     ans=a*5
#     print (a,"* 5 =",ans)
#     a+=1
#     count+=1

#find sum of digits
# num=12
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print("sum is",sum)

#find rev of number

# num=123
# rev=0
# while num>0:
#     rem = num % 10
#     rev=rev*10+rem
#     num = num // 10
# print("rev is", rev)

#claculator

optr=input("enter the operation want to perform eg:add, mul,sub,div")
number1=int(input("enter 1st number"))
number2=int(input("enter 2nd number"))
if optr=="add":
    ans=number1+number2
if optr=="mul":
    ans = number1 * number2
if optr=="sub":
    ans = number1 - number2
if optr=="div":
    ans = number1 / number2

print("answer is:",ans)