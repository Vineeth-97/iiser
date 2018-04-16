import math
import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,100,10001)
#defining 2 element coulmn arrays for r and theta (initial condition) as y0 & z0
y0=np.zeros(2)
z0=np.zeros(2)
y0[0]=2
y0[1]=1
z0[0]=math.pi/2
z0[1]=0
#input parameters
m = float(input("Enter the mass of satellite: "))
M = float(input("Enter the mass of planet: "))
#calculate conserved angular momentum
l=m*y0[0]*y0[0]*z0[1]

def ode_integrate(f,g,y0,t):
	m=len(y0)
	n=len(t)
#defining arrays with two rows for r, its derivative and theta,derivative as w1 & w2 
	w1=np.zeros((m,n))
	w2=np.zeros((m,n))
	w1[:,0]=y0
	w2[:,0]=z0
	for i in range(n-1):
		h=t[i+1]-t[i]
#improved euler method
		w1[:,i+1]=w1[:,i]+h/2*(f(w1[:,i],t[i])+f(f(w1[:,i],t[i])*h+w1[:,i],t[i]+h))
		w2[:,i+1]=w2[:,i]+h/2*(g(w2[:,i],w1[:,i],t[i])+g(g(w2[:,i],w1[:,i],t[i])*h+w2[:,i],f(w1[:,i],t[i])*h+w1[:,i],t[i]+h))
	return w1,w2

def func1(y,t):
	f1=y[1]
	f2=l*l/(m*m*pow(y[0],3))-M/(y[0]*y[0])
	return np.array([f1,f2])

def func2(y1,y2,t):
	g1=y1[1]
	g2=-2*l*y2[1]/(m*y2[0]*y2[0])
	return np.array([g1,g2])

sol1,sol2=ode_integrate(func1,func2,y0,t)

x=np.zeros(10001)
y=np.zeros(10001)
#x=r*cos(theta) & y=r*sin(theta)
x=sol1[0,:]*np.cos(sol2[0,:])
y=sol1[0,:]*np.sin(sol2[0,:])




import matplotlib as mpl
import matplotlib.pyplot as plt

fig=plt.figure()

plt.plot(x,y)

plt.show()
