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
IVM=45
t=0.5
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
