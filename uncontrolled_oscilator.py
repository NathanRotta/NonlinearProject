import numpy as np
import matplotlib.pyplot as plt
from oscilator import *
from scipy.fft import fft,fftfreq
sample_T = 0.001
simulation_T = 120
fex=3.8
def main():
	state0 = np.array([0,0])
	t = np.arange(0,simulation_T,sample_T)
	states = rkt.runge4Ivp(t,state0,oscilator)
	x = states[:,0]
	y = states[:,1]
	ynoDC = y-y.mean()
	f,Pxx = np.fft.rfftfreq(len(t),T0*sample_T) ,np.abs(np.fft.rfft(ynoDC))**2
	Pxx_db = 10*np.log10(Pxx)
	plt.plot(t,y)

	plt.figure(2)
	plt.plot(f*1e-6,Pxx_db)
	plt.ylim(bottom=0)
	plt.xlim(left=0,right=10)
	plt.show()
if __name__=="__main__":
	main()
