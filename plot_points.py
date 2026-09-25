# class points:
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y

#     def reset(self):
#         self.move(0,0)
#     def move(self,a,b):
#         self.x=a
#         self.y=b    
#     def xmove(self,a):
#         self.x=a
#     def ymove(self,b):
#         self.y=b

# obj_point=points(0,0)
# obj_point.reset()
# obj_point=points(2,3)
# obj_point.move()



class queue:
    def __init__(self):
        self.element=[]
        
    def enqueue(self,a):
       self.element.append(a)

    def dequeue(self):
        #print(len(self.element))
        if(len(self.element)==0):
            print("list is empty")
        else:
         self.element.pop(0)
        
      
obj=queue()
obj.enqueue(18)
print(obj.element)
obj.enqueue(35)
print(obj.element)
obj.enqueue(10)
print(obj.element)
obj.enqueue(20)
print(obj.element)
obj.dequeue()
print(obj.element)