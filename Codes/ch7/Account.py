class Account:
    """test document"""
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def getBalance(self):
        return self.balance
    
print(Account.__name__)
print(Account.__module__)
print(Account.__bases__)
print(Account.__dict__)
print(Account.__doc__)
'''
Account
__main__
(<class 'object'>,)
{'__weakref__': <attribute '__weakref__' of 'Account' objects>, '__dict__': <attribute '__dict__' of 'Account' objects>, '__doc__': 'test document', '__module__': '__main__', 'getBalance': <function Account.getBalance at 0x0204FA08>, 'deposit': <function Account.deposit at 0x0204F978>, '__init__': <function Account.__init__ at 0x0204F9C0>, 'withdraw': <function Account.withdraw at 0x0204FA50>}
test document
'''