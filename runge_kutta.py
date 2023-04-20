import numpy as np
import matplotlib.pyplot as plt
#single step in a fourth order runge-kutta integrator
#y current state
#t current time
#fun derivitive function
#h step length
def runge4Step(t,y,fun,h):
	k1 = fun(t,y)
#	print(k1)
#	print(y)
	k2 = fun(t+h/2,y+h*k1/2)
	k3 = fun(t+h/2,y+h*k2/2)
	k4 = fun(t+h,y+h*k3)
	yout = y+(k1+2*k2+2*k3+k4)*h/6
	return yout


def runge4Ivp(t,y0,deriv):
	y = np.zeros((len(t), len(y0)))
	diff = t[1]-t[0]
	y[0,:] = y0
	for i in range(1,len(t)):
		#print("yprev is",yprev)
		y[i,:] = runge4Step(t[i-1],y[i-1,:],deriv,diff)
	return y
def xequalsy(t,x):
	return x

# t = np.arange(0,5,0.001)
# y=runge4Ivp(t,np.array([1]),xequalsy)
# plt.plot(t,np.exp(np.arange(0,5,0.001)),label="exp funtion")
# plt.plot(t,y,label="runga kutta")
# plt.legend()
# plt.show()
