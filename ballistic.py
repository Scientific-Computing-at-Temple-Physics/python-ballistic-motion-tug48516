#Gravitational constant =g
#IVM=initial velo mag IH=initial height
#time step(0.1), initial angle (30)




#HP=highest point
#Distance to ground =DG
#Flight time=FT
#y velo=22.5, x velo=39.0

import numpy
import math as ma
import matplotlib
import matplotlib.pyplot as plt

g=-9.8
IH=10
IVM=45
t=0.5
IA=ma.pi/6.
HP=((45**2.)*ma.sin(IA))/(2*g)
DG=HP+IH
FT=(2*IVM*ma.sin(IA))/g


arr=numpy.array([0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0])
y=22.5+g*arr
x=39*arr

plt.figure()
plt.scatter(x,y)
plt.show()
