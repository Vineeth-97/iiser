import math
import numpy as np

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

Sol=rk4_integrate(func,y0,t,(b,c))


import matplotlib as mpl
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

ax.plot(t,Sol[0,:],'r',label='theta(t)')
ax.plot(t,Sol[1,:],'b',label="theta(t)")
plt.show()
