import math
import numpy as np
#defining function to calculate rk method
def rk4_integrate(f,y0,t,constants):
	m=len(y0)
	n=len(t)
	w=np.zeros((m,n))
	w[:,0]=y0
	for i in range(n-1):
		h=t[i+1]-t[i]
		s1=f(w[:,i],t[i],constants)
		s2=f(w[:,i]+h/2*s1,t[i]+h/2,constants)
		s3=f(w[:,i]+h/2*s2,t[i]+h/2,constants)
		s4=f(w[:,i]+h*s3,t[i]+h,constants)
		w[:,i+1]=w[:,i]+h*(s1+2*s2+2*s3+s4)/6
	return w
#defining function to give velociy & acceleration
def func(y,t,constants):
	m,k,g=constants
	f1=y[1]
	f2=(-k*y[1]*y[1]+m*g)/m
	return np.array([f1,f2])

m=0.01
k=0.0001
g=9.8
#initial condition
y0=np.array([100.0,0.0])
t=np.linspace(0,10,1001)

Sol=rk4_integrate(func,y0,t,(m,k,g))

#plotting
import matplotlib as mpl
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

#ax.plot(t,Sol[0,:],'r')
ax.plot(t,Sol[1,:],'b')
plt.xlabel("time (sec)")
plt.show()
