def fx(num):
	return (num*num)-(4*num)-10

def find_x2(x1,x0):
	return x0 -((fx(x0)*(x1-x0))/(fx(x1)-fx(x0)))

def find_error(x1,x2):
	return abs((x1-x2)/x2)
x0=4
x1=9
file=open("data3.txt","w")
file.write("x0         x1       x2.     error    \n \n ")
file.close()

i=0
for i in range(10):
	x2=find_x2(x1,x0)
	err=find_error(x1,x2)
	file=open("data3.txt","a")
	file.write(str(x0)+"   "+str(x1)+"    "+str(x2)+"   "+str(err)+"\n \n ")
	file.close()
	if(fx(x2)*fx(x0) <0):
		x1=x2
	else:
		x0=x2


