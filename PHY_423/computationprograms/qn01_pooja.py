import math
import numpy as np
#taking values from text file GQ_data into an array
values=np.loadtxt("GQ_data",comments="#",delimiter="	")
print(values)

x=values[:,1]
c=values[:,2]
print("x= ",x)
print("c= ",c)
n=4
#defining function
def func(t):
	return math.exp(-9*t*t/2)

def gq(f,x,c,n):
	sum=0
	for i in range(n):
		sum+=c[i]*f(x[i])
	return sum

I=3*gq(func,x,c,n)
print("The integral value = ",I)	
