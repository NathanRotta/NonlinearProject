import numpy as np
import matplotlib.pyplot as plt
from oscilator import *
sample_T = 0.001

def val_to_index(arr,val):
    return [np.argmin(np.abs(arr-i)) for i in val] 
def main():
	tau = 2*T

	y0 = np.array([0,0])
	t = np.arange(0,120,sample_T)
	states = sim_cont_oscilator(t,y0,tau)
	x = states[:,0]
	y = states[:,1]
	plt.plot(t,y)
	plt.xlabel("time")
	plt.ylabel("y")
	plt.title(r'time domain $\tau=2T$ A=1.2 k=0.5')
	plt.figure(2)
	plt.plot(x,y)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title(r'state space $\tau=2T$')
	Pxx_db,f = power_spectrum_db(y,sample_T,len(t))
	plt.figure(3)
	plt.plot(f,Pxx_db)
	plt.title(r'Power Spectrum(dB) $\tau=2T$')
	plt.ylim(bottom=0)
	plt.xlim(left=0,right=5/T)
	fper = val_to_index(f,np.arange(6)/T)
	plt.scatter(f[fper],Pxx_db[fper])
	plt.show()

if __name__=="__main__":
	main()
