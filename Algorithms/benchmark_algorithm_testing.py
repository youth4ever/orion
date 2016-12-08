import time
from math import sqrt, gcd


#   CMMDC - Cel Mai Mare Divizor Comun - The Greatest Common Divisor - GCD
print('\n------------   CMMDC - Cel Mai Mare Divizor Comun - The Greatest Common Divisor - GCD ------------------')
def cmmdc(a, b):
    '''a, b: positive integers     , cmmdc, c.m.m.d.c., Cel Mai Mare Divizor Comun
    returns: a positive integer,  The Greatest Common Divisor of a & b.   '''
    testValue = min(a, b)
    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1
    return testValue

def cmmdc_rec(a, b):        # CMMDC Recursive
    '''    a, b: positive integers     , cmmdc, c.m.m.d.c., Cel Mai Mare Divizor Comun
        returns: a positive integer,  The Greatest Common Divisor of a & b.    '''
    if b == 0:
       return a
    else:
       return cmmdc_rec(b, a % b)

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a



print('\n------------------ 1  ----------------')
t1  = time.time()

print('Test for the GCD cmmdc Function :\t',cmmdc(1445468, 300173))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2 ------------------')
t1  = time.time()

print('Test for the GCD cmmdc_rec Function :\t',cmmdc(1445468, 300173))




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#################### #####################

print('\n--------------- 3 ------------------')
t1  = time.time()

print('Test for the GCD math.gcd Function :\t',cmmdc(1445468, 300173))




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#################### #####################

print('\n--------------- 4 ------------------')
t1  = time.time()

print('Test for the GCD gcd Custom Function :\t',cmmdc(1445468, 300173))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


