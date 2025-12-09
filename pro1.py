from pymysql import*
def add():
    try:
        i=int(input('enter id:'))
        n=input('enter name:')
        p=float(input('enter price:'))
        con=connect(host='localhost',user='root',password='jaseem16',database='smart')
        q="insert into product value({0},'{1}',{2})".format(i,n,p)
        c=con.cursor()
        c.execute(q)
        con.commit()
        con.close()
        print('inserted succesfully!!')
    except Exception as e:
        print(e)
add()