import time


def get_divisors_2(n):       ### o(^_^)o  #  More powerfull for numbers > 10**10
    ''' first it decomposes the number in prime factors , then makes combinations of all the factors
    to get all the divisors '''
    from pyprimes import factorise
    from itertools import combinations
    from functools import reduce
    from operator import mul
    import heapq
    L = [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
    # print(L)
    D={1}
    for i in range(1, len(L)+1):
        # print( list(combinations(L,i)) )
        for j in list(combinations(L,i)) :
            D.add ( reduce(mul, j)   )
    return list(sorted(D))

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST     MUST BE IMPROVED !! It is a sqrt(n) Algorithm
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

n = 123456789000

##############    ALGORITHM 1

t1  = time.time()


print(get_divisors(n))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

###################     ALGORITHM 2

t1  = time.time()



print(get_divisors_2(n))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')
