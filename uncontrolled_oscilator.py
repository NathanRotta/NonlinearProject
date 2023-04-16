import numpy as np
import matplotlib.pyplot as plt
from oscilator import *

def main():
	state0 = np.array([0,0])
	t = np.arange(0,120,0.001)
	states = rkt.runge4Ivp(t,state0,oscilator)
	x = states[:,0]
	y = states[:,1]
	plt.plot(t,y)
	plt.show()
if __name__=="__main__":
	main()
