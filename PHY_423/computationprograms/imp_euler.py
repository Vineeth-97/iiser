import math
import numpy as np

t=np.linspace(-10,10,20001)
y0=np.zeros(2)
y0[0]=-1/10001
y0[1]=-4*pow(t[0],3)*y0[0]*y0[0]

def ode_integrate(f,y0,t):
	m=len(y0)
	n=len(t)
	w=np.zeros((m,n))
	w[:,0]=y0
	for i in range(n-1):
		h=t[i+1]-t[i]
		w[:,i+1]=w[:,i]+h/2*(f(w[:,i],t[i])+f(f(w[:,i],t[i])*h+w[:,i],t[i]+h))
	return w

def func(y,t):
	f1=y[1]
	f2=-12*pow(t,2)*y[0]*y[0]-8*pow(t,3)*y[0]*y[1]
	return np.array([f1,f2])

Sol=ode_integrate(func,y0,t)


import matplotlib as mpl
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

ax.plot(t,Sol[0,:],'r',label='theta(t)')
ax.plot(t,Sol[1,:],'b',label="theta(t)")
plt.show()
