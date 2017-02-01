class Account:  
    def __init__(self,balance):
        self.balance=balance
    def printme(self):
        print("Account:",self.__class__,self.balance)
class Chqacc(Account):
    def __int__(self,balance,overdraft):
        Account.__init__(self, balance)
        self.overdraft=overdraft
    def printme(self):
        print("check account",self.__class__,self.balance,self.overdraft)
        
class savingAccount(Account):        
    def __init__(self,balance,interest):
        Account.__init__(self, balance)
        self.interest=interest
        
a= Account(100)
c= Chqacc(200,2)
s= savingAccount(300,5)

a.printme()
c.printme()
s.printme()        