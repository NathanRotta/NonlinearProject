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
T0 = (Cap*Lind)**0.5
k=0.50
A = 1.2
def oscilator(t,state,control=0):
	x,y = state
	#print(state)
	N_num = (np.sign(y)*np.abs(y)**alpha)*np.exp(alpha*(1-y))+beta*(np.exp(y)-1)
	#print(N_num)
	N_den = 1+beta*(np.exp(1)-1)
	N=N_num/N_den
	xdot = -y+c
	ydot = x - b*N - d*y + A*np.sin(omega*t)+control
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
	perInd =int(np.round(period/diff))
	y[0,:] = y0
	
#	breakpoint()
	for i in range(1,len(t)):
		if i>perInd:
			yn = rkt.runge4Step(t[i-1],np.concatenate((y[i-1,:],y[i-1-perInd,:]),axis=None),cont_oscilator,diff)
		else:
			yn = rkt.runge4Step(t[i-1],np.concatenate((y[i-1,:],y[i-1,:]),axis=None),cont_oscilator,diff)
		y[i,0]=yn[0]
		y[i,1]=yn[1]
	return y
def power_spectrum_db(y,sample_T,length):
	ynoDC = y-y.mean()
	f,Pxx = np.fft.rfftfreq(length,sample_T) ,np.abs(np.fft.rfft(ynoDC))**2
	Pxx_db = 10*np.log10(Pxx)
	return Pxx_db,f


def val_to_index(arr,val):
    return [np.argmin(np.abs(arr-i)) for i in val] 
# state0 = np.array([0,0])
# t = np.arange(0,120,0.001)
# states = rkt.runge4Ivp(t,state0,oscilator)
# x = states[:,0]
# y = states[:,1]
# plt.plot(t,y)
# plt.show()
