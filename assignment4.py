class bank:
    def __init__(self,name,initial_deposit):
        self.name=name
        self.blance=initial_deposit
        self.create_account()

    def create_account(self):
        print("account created")
        file1=open("transations.txt","a")
        file1.write(f"\n Account created. name--{self.name}  Account Blance:--{self.blance}")
        file1.close()


    def deposit(self,amount):
        self.blance = self.blance + amount
        print("blance=",self.blance)
        file1=open("transations.txt","a")
        file1.write(f"\n Amount deposited. amount{self.blance}")
        file1.close()

    def withdraw(self,amount):
       self.blance = self.blance - amount
       print("blance=",self.blance)
       file1=open("transations.txt","a")
       file1.write(f"\n Amount withdraw. amount{self.blance}")
       file1.close()
      
    def viewdetails(self):
        print(f"User Name:--{self.name}  Account Blance:--{self.blance}")

obj_bank=bank("sino alex",1000)
obj_bank.deposit(500)
obj_bank.withdraw(100)
obj_bank.viewdetails()