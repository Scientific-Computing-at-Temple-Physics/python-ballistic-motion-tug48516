#Gravitational constant =g
#IVM=initial velo mag IH=initial height
#time step(0.1), initial angle (30)
#HP=highest point
#Distance to ground =DG
#Flight time=FT

import numpy
import math as ma
import matplotlib
import matplotlib.pyplot as plt

IH ="Initial height"
IVM ="Initial velocity"
IA ="initial angle"
HP ="highest point"
FT ="flight time"
DG ="distance to ground"

g=-9.8
IH=10
IVM=5.0
t=0.05
IA = 30

# Vx = x velocity, constant
# Vyi = y initial velocity, not constant
Vx=IVM*ma.cos(IA*ma.pi/180)
Vyi=IVM*ma.sin(IA*ma.pi/180)

# Flight time
FT = (2.0*Vyi)/(-g)
print (FT,"fight time")

#distance to ground and highest point
HP = (Vyi**2)/(-2*g)
DG = HP + IH
print (HP,"highest point")
print (DG,"distance to ground")

#y and x position with timestep
timestep = 0.1
arr = numpy.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7])
y=IH+Vyi*arr+0.5*g*arr**2
x=Vx*arr

#plotting
plt.figure()
plt.scatter(x,y)
plt.xlabel("Traveled distance (m)")
plt.ylabel("Height (m)")
plt.title("ballistic motion")

plt.show()
