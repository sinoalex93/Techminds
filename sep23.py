# ##inheritance
# ### method overriding---> same function name 


#### single inheritance
# class Person1:

#     def __init__(self):
#         pass

#     def read(self):
#         print("person reads")

#     def write(self):
#         print("person writes")


# class Person2(Person1):

#     def __init__(self):
#         pass

#     def run(self):
#         print("person runs")

#     def walks(self):
#         print("person walks")


# p2 = Person2()

# p2.read()


# #### multilevel inheritance
# class person1:

#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def read(self):
#         print("person can read")
#     def speak(self):
#         print("person can speak")

# class person2(person1):




###multiple inheritance
### it flow MRO --- method resolution order
class person1:
    def __init__(self):
        pass
    def sleep(self):
        print("person can sleep")
    def eat(self):
        print("person can eat")

class person2:
    def __init(self):
        pass
    def swim(self):
        print("person can swim")
    def speak(self):
        print("person can speak")

class person3:
    def __int__(self):
        pass
    def walk(self):
        print("print person can walk")

class person4(person2,person1,person3):
    def __init__(self):
        def read(self):
            print("can read")

p4=person4()
p4.walk()