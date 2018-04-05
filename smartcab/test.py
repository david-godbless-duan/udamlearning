# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:27:55 2018

@author: David
"""

import numpy as np
import math
import matplotlib.pyplot as plt
x=np.linspace(1,400,100000)
y1=1/np.power(x,2)
y2=[math.pow(0.8,i) for i in x]
y3=[math.pow(math.e,-0.1*i) for i in x]
y4=[math.pow(math.e,-0.5*i) for i in x]
y5=[math.cos(0.0039*i)for i in x]
#plt.plot(x,y1,color='blue')
#plt.plot(x,y2,color='yellow')
#plt.plot(x,y3,color='green')
plt.plot(x,y4,color='red')
plt.plot(x,y5,color='yellow')
#print(math.pow(math.e,-0.05*100))
#for i in range(10000):
#    if math.cos(0.00157*i)<0.99:
#        print(i)
#        break
print(math.cos(0.0039*420))