#!/usr/bin/env python3
import random
import numpy as np

header = "FIELDS time rand"
list=[]
for i in range(0,10001):
	list.append([i, random.uniform(0,1)])


np.savetxt("testdata1.txt",list,header=header,comments="#! ")
