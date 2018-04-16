import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
c=2
k=0.004
h=0.1
M=int((1/h))
sigma=(c*k)/h
T=1
N=int((T/k))

A=np.zeros((M+1,M+1))

#boundary conditions
w=np.zeros((M+1,N+1))

w[0,:]=0
w[M,:]=0
x=0
for i in range(M+1):
	x+=i*h
	w[i,0]=math.sin(math.pi*x)

g=np.zeros((M+1,0))
	
def pde(w,sigma,M,N):
	for i in range(1,M):
		A[i,i]=2-2*sigma*sigma
	for i in range(M-1):
		A[i+1,i]=sigma*sigma
	for i in range(2,M):
		A[i-1,i]=sigma*sigma
	
	for j in range(1,N):
		
		if j==0:
			for i in range(1,M):
				for l in range(1,M):
					w[i,j+1]=0.5*A[i,l]*w[l,j]
				w[i,j+1]+=k*g[i]
			w[1,1]+=0.5*sigma*sigma*w[0,0]
			w[M-1,1]+=0.5*sigma*sigma*w[M,0]
		else:
			for i in range(1,M):
				for l in range(1,M):
					w[i,j+1]=A[i,l]*w[l,j]
				w[i,j+1]-=w[i,j-1]
			w[1,j+1]+=w[0,j]*sigma*sigma
			w[M-1,j+1]+=w[M,j]*sigma*sigma
		
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
