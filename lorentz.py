import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

sigma=10
beta=8/3
rho=28

def atractorlorenz (t,P):
    ''' sistema de ecuaciones para el atractor de lorentz'''
    parax=sigma*(P[1]-P[0])
    paray= P[0]*(rho-P[2])-P[1]
    paraz=P[0]*P[1]-beta*P[2]
    return [parax,paray,paraz]

''' set de c.i'''
ci=[1,1,1]
'''implementar ode dopri5'''
rk4=ode(atractorlorenz)
rk4.set_integrator('dopri5')
rk4.set_initial_value(ci)
t1=200
dt=0.1

'''defino vectores para guardar'''
x=np.zeros(200/0.1)
y=np.zeros(200/0.1)
z=np.zeros(200/0.1)
t=np.linspace(0,10* np.pi,200/0.1)

for i in range(len(t)):
    rk4.integrate(t[i])
    t[i]=rk4.t
    x[i]=rk4.y[0]
    y[i]=rk4.y[1]
    z[i]=rk4.y[2]

'''graficar 3d'''
print x

fig= plt.figure(1)
fig.clf()

ax=fig.add_subplot(111, projection='3d')
ax.set_aspect('equal')

ax.plot(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.savefig('lorenz')

plt.show()
