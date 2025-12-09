class employee:
    sid=0
    sname=""
    sdept=""
    def selfdata(self,a,b,c):
        self.sid=a
        self.sname=b
        self.sdept=c
        
    def getdata(self):
        print("ID:",self.sid)
        print("NAME:",self.sname)
        print("DEPT:",self.sdept)
        
emp=employee()
emp.selfdata(118,'jaseem','IT')
emp.getdata()