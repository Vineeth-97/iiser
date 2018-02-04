import numpy as np

print('+------+------+')
print('|{:^6s}|{:^6s}|'.format("t", "y(t)"))
print('+------+------+')

u = 10.0
g = 9.8

#t = range(0, 2*u/g, u/(10*g))

for t in [x*u/(10*g) for x in range(0, 20)]:
    print('|{:^6.2f}|{:^ 6.2f}|'.format(t, u*t-0.5*g*t*t))
    print('+------+------+')
