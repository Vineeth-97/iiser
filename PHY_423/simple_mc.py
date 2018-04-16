#!/usr/bin/env python3
import numpy as np

# system
Lattice = (10, 10)
J = 1.0
Lx, Ly = Lattice
num_sites = Lx * Ly
T = 1.0

# Numbering scheme for a 4 x 3 lattice
'''
8   9   10  11
4   5   6   7
0   1   2   3
'''

# Nearest neighbour labels
right, left, top, bottom = (0,1,2,3)
N1 = Lx*(Ly-1)
# right & left nn-s
num_nn = 4
nn_table = np.zeros((num_sites, num_nn),dtype=int)
for site in range(num_sites):
	nn_table[site,right] = site+1
	nn_table[site,left] = site-1
	nn_table[site,top] = site+Lx
	nn_table[site,bottom] = site-Lx
# boundary wrap
for site in range(Lx): nn_table[site,bottom]=site+N1 
for site in range(N1,num_sites): nn_table[site,top]=site-N1 
for site in range(0,num_sites,Lx): nn_table[site,left]=site+(Lx-1) 
for site in range(num_sites,Lx): nn_table[site,right]=site-(Lx-1)
#for s in range(num_sites):
#	print(s, ' ', nn_table[s,right], ' ', nn_table[s, left])


# basis states
basis_states = np.ones((num_sites), dtype=int)

def initialize_basis_state():
	# random initial state
	for i in range(L):
		if np.random.uniform(0, 1.0) < 0.5: basis_state[i] = +1
		else: basis_state[i] = -1
	return None

def gen_next_state(beta):
	select_site = np.random.randint(0,num_sites)
	isum = 0
	for site in nn_table[select_site]:
		isum += basis_state[site]
	delE = 2.0 * J * basis_state[select_site] * isum
	# transition proby
	W = np.exp(-beta*delE)

	# acceptance
	if (np.random.uniform(0,1.0) < W):
		basis_state[select_site] = -basis_state[select_site]
	return None


def run_simulation(T):
	beta = 1.0/T

	max_time_steps = 10000
	warmup_steps = 5000
	interval = 3
	count = interval
	samples = 0

	initialize_basis_state()
	for t in range(max_time_steps):
		for i in range(num_sites): gen_next_state(beta)
		if t > warmup_steps:
			if count == interval:
    			# do measurements
				samples += 1
				count = 0
			count += 1

	return None


for T in np.linspace(0, 4.0, 0.2):
	run_simulation(T)















