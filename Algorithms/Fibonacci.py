import time
import gmpy2
import numpy as np
from itertools import count
import eulerlib
from decimal import *
getcontext().prec = 100


def Fibonacci(n):
    iter = 0 		# Number of terms
    #	ORIGINAL Fibonacci with iteration, while loop
    a, b = 0, 1
    while iter < n:
        iter +=1
        a  , b = b, a + b
    return a


def Fibonacci_Binet(n_th) :
    ''':Description:    Returns the Fibonacci corresponding to the number  and uses the Binet Formula.
        http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
        :param n_th: F_nth Fibonacci in sequence
        :return: str, first 9 digits of the Fibonacci number
    '''
    phi = Decimal((5**(1/2)+1)/2)
    phi_ = Decimal((1- 5**(1/2))/2)
    # phi = (1+5**(1/2))/2
    # phi_ = (1-5**(1/2))/2
    # a = ( ( phi**n_th-phi_**n_th ) / ( phi - phi_) )%(10**9)
    a = str(((phi**n_th)-(phi_)**n_th)/( phi - (phi_)))[0:10].replace( '.' , '')
    # b =   ( (( 1 + np.sqrt(5))/2)**n_th - ((1 - np.sqrt(5))/2)**n_th  ) /np.sqrt(5)
    return str(a)