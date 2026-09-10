#print all the prime numbers within a limit .
limit=int(input("enter the limit:-"))
for i in range(2,limit+1):
    is_prime = True
    #print("i=",i)
    for j in range(2,i):
      #  print("j=",j)
        if i%j==0:
            is_prime = False
            break
    if is_prime == True:
        print(i)


