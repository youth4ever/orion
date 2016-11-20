import time
def factors(a):         ##outputs a list of the unique prime factors of its input
    # This Function is splitting a number in its factors, and detects also if the number is a prime
    b = 2
    d = []
    f = a
    while f > 1:
        while f % b != 0:
            b = b + 1
        d = d + [b]
        f = f / b
    if len(d) >1:
        print('The factors of  ',a,':   ',d)
    else: print(a,' is prime')



def factor_split(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module'''
    from pyprimes import factorise
    return [i[0] for i in factorise(n)]

######################################

t1  = time.time()

# factors(6597326399323993)
# factors(1979197919791979)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

############################

t1  = time.time()
# print(factor_split(1979197919791979))
# print(factor_split(6597326399323993))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

###############################

print('\n\n==============    is_prime TESTS ================')

t1  = time.time()

def isprime(n):
    ''' VERY FAST. Does not depend on a pre-generated sieve or on other module !'''
    if n == 1:
        return False
    for i in range(2, int((n**0.5)+1)):
        if not n % i:
            return False
    return True

print('My  Function Test is_prime :  ',isprime(100000980001501))
# print('My  Function Test is_prime',isprime( 18014398241046527))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

###############################


t1  = time.time()

import gmpy2
print('gmpy2 is prime Test :    ',gmpy2.is_prime(100000980001501))
# print('gmpy2 is prime Test ',gmpy2.is_prime( 18014398241046527))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')
