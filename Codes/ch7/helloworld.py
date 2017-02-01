#Objects and methods
'''
methods-functions defined inside the class
applets= application classes
syntax: always use constructor init as __init__(self, balance):
self.balance = balance
self will be autopopulted- neede only when functio  i inside th eclass
'''
class Account:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def getBalance(self):
        return self.balance
a1= Account(50000)
a2= Account(3000)

a1.deposit(1000)
a1.withdraw(400)
a2.deposit(4000)
print(" Balance is", a1.getBalance())
print(" Balance is", a2.getBalance())
'''
 Balance is 50600
 Balance is 7000
'''


#alias of function eg
from _operator import mul
a=mul
a=mul(5,5)
print(a)
'''25'''

class Account:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def getBalance(self):
        return self.balance
    
a3=Account(0)
a4=a3
a4.deposit(1000)
print("a3 balance is ",a3.getBalance())
print("a4 balance is ",a4.getBalance())
print("a3 id is",id(a3))
print("a4 id is",id(a4))

'''a3 balance is  1000
a4 balance is  1000
a3 id is 26740016
a4 id is 26740016
'''
'''
a3 balance is  1000
a4 balance is  1000
'''


class Account:
    numAccounts= 0
    def __init__(self,balance):
        self.balance=balance 
        Account.numAccounts +=1
    def HowManyAccounts(self):
        return Account.numAccounts
a1= Account(0)
a2=Account(300)
print("We have creayed", a1.HowManyAccounts(),"accounts")
print("We have creayed", a2.HowManyAccounts(),"accounts")
'''We have creayed 2 accounts
We have creayed 2 accounts
'''
    