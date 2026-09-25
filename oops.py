####object oriennted programming#####
###object
##atribute--> define an object--variable
##behvaiours-->what an onject does-- function 
## methods -- functions inside the class
##class
##blueprint to create object 
##syntax-- class class_name:


# class car:
#     def start():
#         print("car start")
#     def stop():
#         print("car stop")

# car1=car
# car1.start()
# car1.stop()


###constructor  to initilaize an object
###__init__(self)

##self()-->reffers current object
#eg1
# class car:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def start(self):
#         print(f"{self.name} can start and it {self.color} color")
#     def stop(self):
#         print(f"{self.name} can stop it {self.color} color")

# car1=car("nisan","red")
# car1.start()
# car1.stop()

# #eg2
# class pen:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def write(self):
#         print(f"{self.name} and {self.color}")

# obj_pen=pen("pinpoint","blue")
# obj_pen.write()



class student:
    def __init__(self,name,m1,m2,m3,m4,m5):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def sum_of_marks(self):
        sum=self.m1+self.m2+self.m3+self.m4+self.m5
        return sum
    def avg_mark(self):
        #avg=self.m1+self.m2+self.m3+self.m4+self.m5/5
        avg=self.sum_of_marks()/5
        return avg
    def display(self):
        print("name:-",self.name)
        print("avg-",self.avg_mark())
        print("sum-",self.sum_of_marks())
obj_student=student("sino",40,50,60,70,80)
obj_student.display()