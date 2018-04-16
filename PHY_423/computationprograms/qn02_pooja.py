import math
import numpy as np
#integration limits
a=0
b=1
#defining function
def func(x):
	return np.log(1+x*x)
	
def integrate(f,a,b,m):	
	h=(b-a)/(2*m)
	#array of x values from 0 to 1
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
	#integral value
	I=(term1+term2+term3)*h/3
	return I
I=integrate(func,a,b,16)
print("The integral value using Simpson's 1/3 rule = ",I)

