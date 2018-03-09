# a function to determine the machine epsilon of a given data type 'func'
import numpy as np


def machine_eps(func):
    eps = func(1)
    while func(1) + func(eps) != func(1):
        eps /= func(2)
    return eps*func(2)


print(machine_eps(np.float32))
print(machine_eps(np.float64))
