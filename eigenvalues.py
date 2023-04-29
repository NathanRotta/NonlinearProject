from oscilator import *
import math
import numpy as np
def dNdy(y):
    A1 = alpha*(y**(alpha-1))*np.exp(alpha*(1-y))
    A2 = alpha*(y**alpha)*np.exp(alpha*(1-y))
    A=A1-A2
    B = beta*np.exp(y)
    C =1+beta*(np.exp(1)-1) 
    ans = (A+B)/C
    return ans
def get_mat(contk,m):
    mata = 0
    matb = -1
    matc = 1
    matd = contk-b*dNdy(0)-d
    print(mata,matb,matc,matd)
    return np.array([[mata,matb],[matc,matd]])
def main():
    klist = np.arange(0,10,0.001)
    mats = [get_mat(kval,0) for kval in klist]
    eigs = np.array([np.linalg.eigvals(mat) for mat in mats])
    for mat in mats:
        print(mat)
        print(np.linalg.eigvals(mat))
    plt.plot(klist,eigs[:,0])
    plt.plot(klist,eigs[:,1])
    plt.show()
main()
