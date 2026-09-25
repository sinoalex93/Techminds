import time
def saymyname(fun):
    def wrapper():
        print("say my name")
        fun()
        print("yes")
    return wrapper

@saymyname
def name():
    print("sino")

@saymyname
def hello():
    pass

hello()
name()

start=time.time()
for i in range(1,5):
    print(i)
    time.sleep(1)
end=time.time()
print("time",start-end)