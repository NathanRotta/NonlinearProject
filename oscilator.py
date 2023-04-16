import numpy as np
import matplotlib.pyplot as plt
import runge_kutta as rkt
#constants defined in the paper
Lind = 17.4e-6 #Henries
Cap = 510e-12 #farads
Res  = 5.1e3 #ohms
fex = 3.8e6 #Hz
Ip= 1.5e-3 #Amp
Up = 67e-3 #Volts

a = 1.4
b=4.1
c= 0.92
d = 0.15
omega = 2.25
alpha = 1.7
beta = 0.001
T = 2*np.pi/omega
k=0.17
def oscilator(t,state,control=0):
    x,y = state
    N_num = (y**alpha)*np.exp(alpha*(1-y))+beta*(np.exp(y)-1)
    N_den = 1+beta*(np.exp(1)-1)
    N=N_num/N_den
    xdot = -y+c
    ydot = x - b*N - d*y + a*np.sin(omega*t)+control
    return np.array([xdot,ydot])

def cont_oscilator(t,state):
	x,y,xp,yp = state
	er = y-yp
	control = -k*er
	output =  oscilator(t,np.array([x,y]),control=control)
	return np.concatenate((output, [x], [y]),axis=None)
	
	


def sim_cont_oscilator(t,y0,period):
	y = np.zeros((len(t), 2))
	diff = t[1]-t[0]
	perInd =int(np.round(diff/period))
	y[0,:] = y0
	

	for i in range(1,len(t)):
		if i>perInd:
			y[i,:], = rkt.runge4Step(t[i-1],np.concatenate((y[i-1,:],y[i-1-perInd,:])),cont_oscilator,diff)
		else:
			y[i,:], = rkt.runge4Step(t[i-1],np.concatenate((y[i-1,:],y[i-1,:],[k]),axis=None),cont_oscilator,diff)

	return y


# state0 = np.array([0,0])
# t = np.arange(0,120,0.001)
# states = rkt.runge4Ivp(t,state0,oscilator)
# x = states[:,0]
# y = states[:,1]
# plt.plot(t,y)
# plt.show()
