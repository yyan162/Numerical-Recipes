import numpy as np

#Newton-Raphson Method

def newt(x,n,f, f_prime):
     for i in range(n):
        if f_prime(x) == 0:
            return x
        x = x - f(x)/f_prime(x)
     return x
	

