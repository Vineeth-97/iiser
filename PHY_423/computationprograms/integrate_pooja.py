import math
import numpy as np
a=0
b=math.pi

def func(x):
	return np.sin(x)*np.sin(x)
	
def integrate(f,a,b,m):	
	h=(b-a)/(2*m)
	x=np.linspace(a,b,2*m+1)
	print("x = ",x)
	term1=f(a)+f(b)
	sum=0
	for i in range(1,m+1):
		sum+=f(x[2*i-1])
	term2=4*sum
	sum1=0
	for i in range(1,m):
		sum1+=f(x[2*i])
	term3=2*sum1
	I=(term1+term2+term3)*h/3
	return I
I=integrate(func,a,b,20)
print(I)

