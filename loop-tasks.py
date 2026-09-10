# #find sum of digits
# num=12345
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print("sum is",sum)
#
# #find rev of number
#
# num=123
# rev=0
# while num>0:
#     rem = num % 10
#     rev=rev*10+rem
#     num = num // 10
# print("rev is", rev)

# #Find the Fibanocci series up to 100.
# a = 0
# b = 1
#
# for i in range(100):
#     print(a)
#
#     c = a + b
#     a = b
#     b = c
#
#     if a > 100:
#         break

## Find factorial of a number

# n = 5
# factorial = 1
#
# for i in range(1, n + 1):
#     factorial = factorial * i
#
# print("Factorial is", factorial)

n = 9
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print(n, "is a Prime number")
else:
    print(n, "is not a Prime number")