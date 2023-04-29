import numpy as np
import matplotlib.pyplot as plt
from oscilator import *
from scipy.fft import fft,fftfreq
sample_T = 0.001
simulation_T = 1000
fex=3.8
Pmap1 = 1/T
Pmap2 = 1/(2*T)
pmap3 = 1/(4*T)
def pmap(t,x,y,Tper):
    Samples = np.floor(t[-1]/Tper)
    index = val_to_index(t,Tper*np.arange(Samples))
    return x[index],y[index],t[index]
    
def main():
	state0 = np.array([0,0])
	t = np.arange(0,simulation_T,sample_T)
	states = rkt.runge4Ivp(t,state0,oscilator)
	x = states[:,0]
	y = states[:,1]
	plt.plot(t,y)
	plt.title('Uncontrolled time domain')
	plt.xlabel('time')
	plt.ylabel('y')
	plt.figure(2)
	Pxx_db,f = power_spectrum_db(y,sample_T,len(t))
	plt.plot(f,Pxx_db)
	plt.title(r'Power Spectrum(dB) $\tau=T$')
	plt.ylim(bottom=0)
	plt.xlim(left=0,right=5/T)
	fper = val_to_index(f,np.arange(6)/T)
	plt.scatter(f[fper],Pxx_db[fper])
	plt.figure(3)
	xm,ym,tm=pmap(t,y,oscilator(t,[x,y])[1],T)
	plt.scatter(xm,ym)
	plt.title('Poincare Section')
	plt.xlabel("y")
	plt.ylabel(r'$\frac{dy}{dy}$')
	plt.figure(4)
	#plt.plot(tm,ym)
	plt.show()
if __name__=="__main__":
	main()
