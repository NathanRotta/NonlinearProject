import numpy as np
import matplotlib.pyplot as plt
from oscilator import *

def main():
	tau = 2*T
	tau = 2.7925*2
	y0 = np.array([0,0])
	t = np.arange(0,180,0.0001)
	states = sim_cont_oscilator(t,y0,tau)
	x = states[:,0]
	y = states[:,1]
	plt.plot(t,y)
#	plt.plot(x,y)
	Pxx,f = power_spectrum_db(y,sample_T)
	plt.show()

if __name__=="__main__":
	main()
