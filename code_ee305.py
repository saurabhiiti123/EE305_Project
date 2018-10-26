#code for project EE 305- Study of EM wave propagation in Al and Cu
# by Saurabh Sharma and Safal Bahare
# 160002053 and 160002050 resp.

import matplotlib.pyplot as plt
from math import *
import numpy as np 
#w = np.arange(8000)

stop = 0.5
x = np.arange(start=1e-5,stop=0.5,dtype= np.float32,step=np.float32(stop/1000))

'''
delta= 0.2123/np.sqrt(w+1)
plt.xlabel("angular frequency (W)")
plt.ylabel("Skin Depth")
#plt.title(label='Skin depth vs Angular frequency for Aluminium')
Copper
'''

#mu= 0.16341*np.sqrt(w)

w = 1
alpha = 6.114398*np.sqrt(1)
exp1 = np.exp((-1)*alpha*x)
h1 = np.float32(6886834.1636*exp1/np.sqrt(w))
print(h1)
w = 10
alpha =6.114398*np.sqrt(10)

exp2 = np.exp((-1)*alpha*x)
h2 = np.float32(6886834.1636*exp2/np.sqrt(w))
w = 100
alpha = 6.114398*np.sqrt(100)

exp3 = np.exp((-1)*alpha*x)
h3 = np.float32(6886834.16367*exp3/np.sqrt(w))
'''

plt1 = plt.plot(x,exp1,'r',label='w1 = 1rad/s')
plt2 = plt.plot(x,exp2,'g',label="w2 = 10rad/s")
plt3 = plt.plot(x,exp3,'b',label="w3 = 100rad/s")

'''
plt1 = plt.plot(x,h1,'r',label='w1 = 1rad/s')
plt2 = plt.plot(x,h2,'g',label="w2 = 10rad/s")
plt3 = plt.plot(x,h3,'b',label="w3 = 100rad/s")

plt.legend()

plt.xlabel("Distance traversed")
plt.ylabel("Magentic Field amplitutde ")
plt.title('Magnetic Field Amplitutde vs Angular frequency for Copper')

plt.savefig('Magnetic Field Amplitutde vs Angular frequency for Copper')

plt.show()
