#!/usr/bin/env python3
import numpy as np

noblock = np.loadtxt("colvar_noblock.txt",skiprows=1)
block100 = np.loadtxt("colvar_block100.txt",skiprows=1)


print(noblock[:,1])

np.savetxt("colvar_noblock_mathematica.dat",noblock[:,1])