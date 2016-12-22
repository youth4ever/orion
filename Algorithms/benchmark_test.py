import time
from math import sqrt

def get_divisors(n):      ### o(^_^)o  FASTEST  o(^_^)o  ### !! FIRST FASTEST
    factors = set()
    for x in range(1, int(n**(1/2)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)


def get_divisors_1(n):      ### o(^_^)o  FASTEST  o(^_^)o  ### !! FIRST FASTEST
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)








######################################

t1  = time.time()

print(get_divisors_1(965329*1010519 ))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

############################

t1  = time.time()


print(get_divisors(965329*1010519 ))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

###############################

print('\n\n==============      ================')

t1  = time.time()

import gmpy2
k_th = 1210177
f =gmpy2.fib(k_th)
print( len(str(f)) , str(f)[:9])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

###############################


t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')
