#lambda and recursion
for i in range(1,6):
    for j in range(1,6):
        if j==1 or j==5 or i==3:
            print("*",end="'")
        else:
            print('  ',end="")
    print('  ')
