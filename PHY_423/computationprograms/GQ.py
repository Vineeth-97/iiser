import math
import numpy as np

values=np.loadtxt("GQ_data",comments="#",delimiter="	")
print(values)
x=values[:,1]
c=values[:,2]
print("x= ",x)
print("c= ",c)
n=4

def func(t):
	return math.exp(-t*t/2)

def gq(f,x,c,n):
	sum=0
	for i in range(n):
		sum+=c[i]*f(x[i])
	return sum

I=gq(func,x,c,n)
print(I)	
