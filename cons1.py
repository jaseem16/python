class person:
    def __init__(self,sid,sname):
        self.sid=sid
        self.sname=sname
    
    def display(self):
        print('ID:',self.sid)
        print('NAME:',self.sname)
    
p1=person(1,'jas')
p1.display()
p2=person(2,'sam')
p2.display()