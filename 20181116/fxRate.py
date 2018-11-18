# this is to practice file input
# USD/JPY historical data from 2007 to 2018

import matplotlib.pyplot as plt
import numpy as np

x,y = [],[]
#file open
with open('rate.txt', 'r') as file:
    data = file.read().splitlines()
    
    for line in data:
        line = line.split('\t')
        x.append(line[0])
        y.append(float(line[1]))

plt.plot(x,y)
plt.show()