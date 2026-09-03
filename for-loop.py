# #print 1 to 20 numbers avoid mutiple of 5
# for i in range(1,21):
#     if i%5==0:
#         continue
#     print(i)
# list property programs
# #print all elements in a list
# numbers=[10,20,30,40,50]
# for i in numbers:
#     print(i)

# #find the sum of list elements
# sum=0
# numbers=[10,20,30,40]
#
# for i in numbers:
#     sum=sum+i
# print ("sum is",sum)

# # #find the largest element
# numbers=[100,20,300,40]
# large=0
# for i in numbers:
#    if i>large:
#        large=i
# print("Largest element is", large)

##count even numbers
# numbers=[1,2,3,4,5,6]
# count=0
# for i in numbers:
#     if i %2 == 0:
#         count+=1
# print("count is",count)


##print list in reverse
# numbers=[10,20,30,40,50]
# for i in numbers[::-1]:
#     print(i)

#tuple property programs
# #print tuple elements
# fruits=("apple","banana","orange")
# for i in fruits:
#     print(i)

# #count total ements
# t=(10,20,30,40,50)
# count=0
# for i in  t:
#     count+=1
# print(count)

#find maximum elemt
# t=(12,45,23,67,34)
# large=0
# for i in t:
#    if i>large:
#        large=i
# print("Largest element is", large)

# #find sum of tuple
# sum=0
# t=(5,10,15,20)
#
# for i in t:
#     sum=sum+i
# print ("sum is",sum)

#search an element
t=(10,20,30,40)
x=30
f=0
for i in t:
    if i== x:
        f=1
        break
if f==1:
    print("found")
else:
    print("not found")
