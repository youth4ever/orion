import pyprimes
import sympy

import random, functools, operator, time

test_nr= functools.reduce( operator.mul,  [  (random.randint(100000,500000)) for i in range(10) ] )
print(test_nr)



print('\n------------------ 1  ----------------')
t1  = time.time()


print( list( pyprimes.factorise(test_nr))  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2 ------------------')
t1  = time.time()


print( sympy.factorint(test_nr) )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#################### #####################

