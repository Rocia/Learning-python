import Account
from xml.dom import HIERARCHY_REQUEST_ERR
a1= Account.Account(0)
a2=Account.Account(300)

a1.deposit(500)
a1.withdraw(50)
a2.deposit(400)
print("balance  of a1 is", a1.getBalance())
print("balance  of a2 is", a2.getBalance())

print(Account.__name__)
#print(Account.__module__)
#print(Account.__bases__)
print(Account.__dict__)
#print(Account.__doc__)
print(a1.__class__)
print(a1.__dict__)

'''
balance  of a1 is 450
balance  of a2 is 700
'''

'''__init__.py IS ALWAYS NEEDED AS WHEN YOU INITIALIZE A PACKAGE A HIERARCHY MUSTV BE BUILT
__init__.py HELPS US IN BUILDING THIS HIERARCHY
'''