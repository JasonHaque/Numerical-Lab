def fx(num):
	return (num*num)-(4*num)-10

def find_x2(x0,x1):
	return (x1)-((fx(x1)*(x1-x0))/(fx(x1)-fx(x0)))

def find_error(x1,x2):
	return abs((x1-x2)/x2)
x0=2
x1=4
print(find_x2(x0,x1))
file=open("data1.txt","w")
file.write("x0         x1       x2.       error \n \n ")
file.close()
for i in range(10):
	x2=find_x2(x0,x1)
	err=find_error(x1,x2)
	file = open("data1.txt","a")

	file.write(str(x0)+"   "+str(x1)+"    "+str(x2)+"   "+str(err)+"\n \n ")
	file.close()
	x0=x1
	x1=x2



