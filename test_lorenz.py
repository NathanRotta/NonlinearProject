import numpy as np
import matplotlib.pyplot as plt
import runge_kutta as rkt

def lorenz(t,y,sig=10,rho=28,beta=8/3):
#	print(y)
	x1,x2,x3 =y
	x1_dot = sig*(x2-x1)
	x2_dot = x1*(rho-x3)-x2
	x3_dot = x1*x2-beta*x3
	out = [x1_dot,x2_dot,x3_dot]
	outnp = np.array(out)
	return outnp

t = np.arange(0,100,0.0001)
lz = rkt.runge4Ivp(t,np.array([1,1,1]),lorenz)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(lz[:,0], lz[:,1], lz[:,2])
plt.show()

	
