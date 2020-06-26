import numpy as np
from math import exp,sqrt
import random
import matplotlib.pyplot as plt


def gBM(S,sigma,mu,t,z):
    gBM= S*exp((mu - sigma**2/2)*t + sigma * sqrt(t) * z)
    return gBM


sigma=0.3
mu=0.05
delta_t=0.01


process=np.zeros(10000) 
process[0]=100 


for n in range(1,len(process)):
    process[n]=gBM(process[n-1],sigma,mu,delta_t,random.gauss(0,1))

plt.plot(process)
plt.show()
