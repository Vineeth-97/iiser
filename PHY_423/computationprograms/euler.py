import math
import numpy as np

def ode_integrate(f,y0,t,constants):
	m=len(y0)
	n=len(t)
	w=np.zeros((m,n))
	w[:,0]=y0
	for i in range(n-1):
		h=t[i+1]-t[i]
		w[:,i+1]=w[:,i]+h*f(w[:,i],t[i],constants)
	return w

def func(y,t,constants):
	b,c=constants
	f1=y[1]
	f2=-c*np.sin(y[0])-b*y[1]
	return np.array([f1,f2])

b=0.25
c=5.0
#initial condition
y0=np.array([np.pi-0.1,0.0])
t=np.linspace(0,10,1001)

Sol=ode_integrate(func,y0,t,(b,c))


import matplotlib as mpl
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

ax.plot(t,Sol[0,:],'r',label='theta(t)')
ax.plot(t,Sol[1,:],'b',label="theta(t)")
plt.show()
