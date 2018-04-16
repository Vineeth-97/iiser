# Cubic Spline interpolation of cos(x)

import numpy as np

def cubic_spline(xv, yv):
    num_points = len(xv)
    
    # delta_i
    delta = []
    for i in range(num_points-1):
        delta.append(xv[i+1]-xv[i])
    # Delta_i
    Delta = []
    for i in range(num_points-1):
        Delta.append(yv[i+1]-yv[i])
    
    '''
    Solutions for 'c_i'-s
    '''
    # Coefficient matrix
    A = np.zeros((num_points,num_points))
    # diagonal elements
    A[0,0] = 1.0
    A[num_points-1,num_points-2]=1.0
	#A[num_points-1,num_points-1]=0.0
    for i in range(1, num_points-1):
        A[i,i] = 2.0*(delta[i-1]+delta[i])
    # upper diagonal elements
    for i in range(1, num_points-1):
        A[i,i+1]=delta[i]
    # lower diagonal elemets
    for i in range(1, num_points-1):
        A[i,i-1]=delta[i-1]
    # The rhs vector
    rhs = np.zeros((num_points))
    for i in range(1, num_points-1):
        rhs[i]=3.0*(Delta[i]/delta[i]-Delta[i-1]/delta[i-1])
    # solve for c_i
    c = np.linalg.solve(A, rhs)
    
    '''
    Solutions for 'd_i'-s
    '''
    d = np.zeros((num_points))
    for i in range(num_points-1):
        d[i]=(c[i+1]-c[i])/(3.0*delta[i])
        
    '''
    Solutions for 'b_i'-s
    '''
    b = np.zeros((num_points))
    for i in range(num_points-1):
        b[i]=Delta[i]/delta[i]-(delta[i]/3.0)*(2.0*c[i]+c[i+1])
    
    def nth_spline(n,x):
        if n < 0 or n >= num_points-1:
            print('Error: Out-of-range spline segment')
            return None
        p = yv[n] + b[n]*(x-xv[n]) + c[n]*(x-xv[n])**2 + d[n]*(x-xv[n])**3
        return p
    
    return nth_spline


# Generate data
xpoints = np.linspace(0, np.pi/2, num=5, endpoint=True)
ypoints = np.cos(xpoints)
print(xpoints)
print(ypoints)


# Get cubic splines
nth_spline=cubic_spline(xpoints,ypoints)
# Construct the splines
x_intpol = np.array(0)
y_intpol = np.array(0)
for i in range(len(xpoints)-1):
    x = np.linspace(xpoints[i],xpoints[i+1],10)
    x_intpol = np.append(x_intpol,x)
    y_intpol = np.append(y_intpol,nth_spline(i, x))

# Verify by plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
# plot the points
ax.plot(xpoints, ypoints, 'ro')
# plot the splines
ax.plot(x_intpol, y_intpol, '--')
plt.show()

