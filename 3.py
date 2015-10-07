import matplotlib.pyplot as plt
import numpy as np

sep=1500 #cantidad de divisiones en los periodos pedidos
y=np.zeros(sep)
yprima=np.zeros(sep)
h=20*np.pi/sep # el paso, la cantidad de periodos pedidos/ #divisiones
print h
mu=1.657

#condiciones iniciales
y[0]=0.1
yprima[0]=0
def f(y,yprima):
    int= (-mu*((y**2)-1)*yprima) - y
    return (yprima,int)


for n in range(0,sep-1):
    fun=f(y[n],yprima[n])
    k1=(h*fun[0],h*fun[1])
    fun2=f(y[n]+k1[0]/2., yprima[n]+k1[1]/2.)
    k2=(h*fun2[0],h*fun2[1])
    fun3=f(y[n]-k1[0]-2*k2[0],yprima[n]-k1[1]-2*k2[1])
    k3=(h*fun3[0],h*fun3[1])
    y[n+1]=y[n] + (1/6.)*(k1[0]+ 4.*k2[0]+ k3[0])
    yprima[n+1]=yprima[n] + (1/6.)*(k1[1]+ 4.*k2[1]+ k3[1])


print y
print yprima

plt.figure(1)
plt.clf()
plt.plot(y,yprima)
plt.show()
#for n in x:
#    k1=h*f1(y[n],yprima[n])
#    k2=h*f1(y[n+h/2],yprima[n+k1/2])
#    k3=h*f1(y[n+h],yprima[n-k1-2*k2])
#    yprima[n+1]=yprima[n] + 1/6(k1+ 4*k2+ k3)
