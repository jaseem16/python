class banking:
    minimum_balance=500
   
    def __init__(self,init_balance=5000):
        self.balance=init_balance
        
    def __init__(self,deposit,withdraw,minimum_balance):
        self.deposit=deposit
        self.withdraw=withdraw
        self.minimum_balance=minimum_balance
        if minimum_balance<500:
            print('minimum balance should be more than RS:500')
        
    def display(self):
        print("deposit:",self.deposit)
        print("withdraw:",self.withdraw)
        print("minimum_balance:",self.minimum_balance)
        
bk=banking(2000,1000,400)
bk.display()