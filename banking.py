class SBI:
    bal=85000
    c=0
class Gpay(SBI):
    def gppayment(self):
        print("---Gpay payment portal---")
        self.amt=int(input("enter amount:"))
        if(self.amt<self.bal and self.amt<=0):
            self.bal=self.bal-self.amt
            print("amount debited")
            print("current balance",self.bal)
            self.c=c+1
        elif(self.amt<0):
            print("negative amount not allowed")
        else:
            print("cannot transact!!")
            self.c=0
        
class Phonepe(SBI):
    def phpayment(self):
        print("---Phonpe payment portal---")
        self.amt=int(input("enter amount:"))
        if(self.amt<=25000):
            if(self.amt<self.bal and self.amt>=0):
                self.bal=self.bal-self.amt
                print("amount debited")
                print("current balance",self.bal)
                self.c=self.c+1
            elif(self.amt<0):
                print("negative amount not allowed")
            else:
                print("cannot transact!!")
                self.c=0
        else:
            print("amount exceeds per transaction limt")
     
while(True):     
    ch=int(input("1.Gpay\n2.Phonepe\n0.Exit\nEnter:"))
    if(ch==1):
        gp=Gpay()
        gp.gppayment()
        print("transaction count",gp.c,"success")
    elif(ch==2):
        ph=Phonepe()
        ph.phpayment()
        print("transaction count",ph.c,"success")
    elif(ch==0):
        print("terminated")
        break
    else:
        print("invalid option selected")
    
            
            