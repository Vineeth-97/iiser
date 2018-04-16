import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
k=0.005
h=0.1
a=0
b=1
M=int((b-a)/h)

D=1
sigma=(D*k)/(h*h)
T=10
N=int(T/k)

A=np.zeros((M+1,M+1))

#boundary conditions
w=np.zeros((M+1,N+1))

w[0,:]=0
w[M,:]=0
x=0
for i in range(M+1):
	x+=i*h
	w[i,0]=math.sin(math.pi*x)*math.sin(math.pi*x)

	
def pde(w,sigma,M,N):
	for i in range(1,M):
		A[i,i]=1-2*sigma
	for i in range(1,M-1):
		A[i,i+1]=sigma
	for i in range(2,M):
		A[i,i-1]=sigma
	for j in range(N):
		for i in range(1,M):
				for l in range(1,M):
					w[i,j+1]=A[i,l]*w[l,j]
		w[1,j+1]+=w[0,j]*sigma
		w[M-1,j+1]+=w[M,j]*sigma
	return w

Sol=pde(w,sigma,M,N)
print(w)

x=np.linspace(0,1,11)
t=np.linspace(0,10,2501)

fig = plt.figure()
plt.plot(w)
#ax = fig.add_subplot(111, projection='3d')
#Axes3D.plot_surface(x,t,w)
plt.show()
