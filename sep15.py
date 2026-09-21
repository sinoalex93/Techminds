# modules
#math module
#it perform math operation
# import math
# print(math.sqrt(25))
# print(math.floor(5))

#random module
#to select random value

#randint()
#print(random.randint(3,6)

#randomchoice()
#
# #w.a.p for coin toss
# import random
# coin=["head","tail"]
# print(random.choice(coin))
#
# #another way
# z=random.randint(0,1)
# print("head") if z else print("tail")

#w.a.p to game
# import random
# ch=["rock","paper","scissor"]
# cmch=random.choice(ch)
# player=""
# while player not in ch:
#     player = input("enter user choice:-").lower()
# print("user choice",player,"\n")
# print("computer choice",cmch,"\n")
# if player==cmch:
#     print("its a tiee")
# elif player=="rock":
#     if cmch=="paper":
#         print("computer win")
#     else:
#         print("user win")
# elif player=="paper":
#     if cmch=="scissor":
#         print("computer win")
#     else:
#         print("user win")


#w.a.p for dices 2 player game using function
import random

def play():
    value=random.randint(1,6)
    sum=0
    for i in range(value):
            b=random.randint(1,6)
            sum=sum+b
    return sum


player1=play()
player2=play()
print(player1,player2)
if player1 > player2:
    print("player 1 win")
elif player2 > player1:
    print("player 2 win")
else:
    print("its a tie")