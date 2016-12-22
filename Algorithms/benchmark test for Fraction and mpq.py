import time
from fractions import Fraction
import gmpy2


print('------------------ Fraction vs gmpy2.mpq ---------------')
 # Fractions : ',Fraction(i, j) , '      ',gmpy2.mpq(i, j)

i = 2*5*7*11*13*997*197
j = 2*3*13*19*23*17*41*73*97*10



print('\n------------------ 1  ----------------')
t1  = time.time()


print(Fraction(i, j))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2 ------------------')
t1  = time.time()


print(gmpy2.mpq(i, j))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#################### #####################