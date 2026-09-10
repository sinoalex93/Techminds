# #w.a.p to find prime or not
# number= int(input("enter a number:"))
# is_prime=True
# if number==1:
#     is_prime=False
# for i in range(2,number):
#     if number%i==0:
#         is_prime=False
# if is_prime==True:
#     print("prime")
# else:
#     print("not prime")

#w.a.p to print pyramid

# number=5
# for i in range(1,number+1):
#     for j in range(number - i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end="   ")
#     print()

# #w.a.p to print cheesboard
# #WBWBWBWB
# #BWBWBWBW
#
# for i in range(9):
#     for j in range(9):
#         if(i+j)%2==0:
#             print("W",end="")
#         else:
#             print("B",end="")
#     print()


#w.a.p to print
# str = "apple"
#
# for i in range(1, len(str) + 1):
#     print(str[:i])

word = "apple"
number = len(word)

for i in range(1, number + 1):
    for j in range(number - i):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print(word[k - 1], end="")

    print()
