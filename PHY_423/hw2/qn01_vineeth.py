import numpy as np


def gaus(x, m, a):
    return((1/(2*np.pi*a))*np.exp((-0.5*((x-m)/a)**2)))


print(gaus(1, 0, 2))
