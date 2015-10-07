import matplotlib.pyplot as plt
import numpy as np

sep=1500 #cantidad de divisiones en los periodos pedidos
y=np.zeros(sep)
yprima=np.zeros(sep)
h=20*np.pi/sep # el paso, la cantidad de periodos pedidos/ #divisiones
print h
mu=1.657
t=np.linspace(0,20*np.pi,sep)


def f(y,yprima):
    '''funcion que entrega lo que integraremos para encontrar la posicion y
    la velocidad , respectivamente, entregandole los valores iniciales de
    ambas'''

    int= (-mu*((y**2)-1)*yprima) - y
    return (yprima,int)

def obtienevalores(y0,yprima0):
    '''recibe condiciones iniciales y entrega y y dy'''
    #condiciones iniciales 1
    y[0]=y0
    yprima[0]=yprima0
    for n in range(0,sep-1):
        fun=f(y[n],yprima[n])
        k1=(h*fun[0],h*fun[1])
        fun2=f(y[n]+k1[0]/2., yprima[n]+k1[1]/2.)
        k2=(h*fun2[0],h*fun2[1])
        fun3=f(y[n]-k1[0]-2*k2[0],yprima[n]-k1[1]-2*k2[1])
        k3=(h*fun3[0],h*fun3[1])
        y[n+1]=y[n] + (1/6.)*(k1[0]+ 4.*k2[0]+ k3[0])
        yprima[n+1]=yprima[n] + (1/6.)*(k1[1]+ 4.*k2[1]+ k3[1])
    return (y,yprima)

print y
print yprima
''' a es primer set de condiciones iniciales y b el segundo'''

a=obtienevalores(0.1,0)
plt.figure(1)
plt.clf()
plt.plot(a[0],a[1],label='condiciones iniciales 2')
b=obtienevalores(4.,0)
plt.plot(b[0],b[1],'r',label='condiciones iniciales 1')
plt.legend()
plt.xlabel('y')
plt.ylabel('dy')
plt.title('espacio de fase')
plt.savefig('espaciofase')


plt.figure(2)
plt.plot(t,a[0],'r',label='condiciones iniciales 2')
plt.plot(t,b[0],'g',label='condiciones iniciales 1')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.title('Y en el tiempo')
plt.savefig('yeneltiempo')

plt.show()
#for n in x:
#    k1=h*f1(y[n],yprima[n])
#    k2=h*f1(y[n+h/2],yprima[n+k1/2])
#    k3=h*f1(y[n+h],yprima[n-k1-2*k2])
#    yprima[n+1]=yprima[n] + 1/6(k1+ 4*k2+ k3)
