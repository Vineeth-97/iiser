import math
import numpy as np

t=np.linspace(0.0,5.0,20.0)
#print(t)
n=len(t)
# model: y=c1+c2*t
A=np.zeros((n,2))
A[:,0]=1.0
for i in range(n):
	A[i,1]=t[i]

At=A.transpose()
#print(At)
C=np.matmul(At,A)
b=np.ones(20)
D=np.matmul(At,b)
x=np.linalg.solve(C,D)
print(x)
#find error
e=np.zeros(n)
for i in range(n):
	e[i]=

