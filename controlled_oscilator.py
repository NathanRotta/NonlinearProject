import numpy as np
import matplotlib.pyplot as plt
from oscilator import *

def main():
	k=0.17
	tau = 2*T
	y0 = np.array([0,0])
	t = np.arange(0,120,0.001)
	states = sim_cont_oscilator(t,y0,tau)
	x = states[:,0]
	y = states[:,1]
	plt.plot(t,y)
	plt.plot(x,y)
if __name__=="__main__":
	main()
