from oscilator import *
import math
def dNdy(y):
    A1 = alpha*(y**(alpha-1))*math.exp(alpha*(1-y))
    A2 = alpha*(y**alpha)*math.exp(alpha*(1-y))
    A=A1-A2
    B = beta*math.exp(y)
    C =1+beta*(exp(1)-1) 
    ans = (A+B)/C
    return ans
def get_mat(k):
    mata = 0
    matb = -1
    matc = 1
    matd = k+DNdy()

def main():

