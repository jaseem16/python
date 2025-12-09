m1=int(input("enter m1:"))
m2=int(input("enter m2:"))
m3=int(input("enter m3:"))
m4=int(input("enter m4:"))
m5=int(input("enter m5:"))
total=(m1+m2+m3+m4+m5)
print("total marks out of 500:",total)
avg=(total/5)
print('average is:',avg)
	if(avg>=75 and avg<=100):
		print("distinction")
	elif(avg>=65 and avg<75):
		print("first class")
	elif(avg>=50 and avg<65):
		print("second class")
	elif(avg<50):
		print("fail")
	
	