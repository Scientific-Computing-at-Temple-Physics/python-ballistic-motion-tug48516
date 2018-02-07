#Gravitational constant =g
#IVM=initial velo mag IH=initial height
#time step(0.1), initial angle (30)




#HP=highest point
#Distance to ground =DG
#Flight time=FT



import math as ma
g=9.8
IH=10
IVM=45
t=0.1
IA=ma.pi/6.
HP=((45**2.)*ma.sin(IA))/(2*g)
DG=HP+IH
FT=(2*IVM*ma.sin(IA))/g

print("highest point",HP,"Distance to Grond",DG,"Flight time",FT)
