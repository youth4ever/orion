
from itertools import count, product
from math import gcd

def pythagorean_triple(plim):
    '''
    a^2 + b^2 = c^2

    a = m^2 - n^2
    b = 2mn
    c = m^2 + n^2

    k [ a + b + c = p = 2 * m * ( m + n ) ]

    #>>> next(pythagorean_triple(30))
    Pythagorean triplets with this property that the greatest common divisor of
    any two of the numbers is 1 are called primitive Pythagorean triplets.
    '''
    iter=0 # Added later
    for m in count(1):
        if 2*m**2 > plim:
            break
        for n in range( 1 + m%2, m, 2):
            if gcd(m, n)==1:
                p = 2 * m * (m+n)
                a, b, c = m**2-n**2  ,    2*m*n ,     m**2+n**2
                for k in range(1, plim//p+1):
                    iter+=1
                    print( str(iter)+'.    ',  (k*a, k*b, k*c))
                    yield (k*a, k*b, k*c)

def problem0086():
    lim = 10000
    table = [0] * lim
    for a, b, c in map(sorted, pythagorean_triple(lim)):
        table[a] += max(0, b//2 - (b-a) + 1)
        table[b] += a//2
    return next(M for M in range(lim) if sum(table[:M+1]) > 1E6)

print(problem0086())



print('\n---------------------------------')
######################################

from math import gcd
PrimitiveTripleCache = []
def primitive_triples():
    u, v = 2, -1    # prime the generator the first time it's used
    for u, v, a, b in PrimitiveTripleCache:
        yield a, b
    # Generate further triples that haven't yet been cached.  The first
    # time through, the 'v' loop needs to pick up with the previously
    # cached 'u'.
    restart = True
    while True:
        if restart:
            range_start = v + 2
            restart = False
        else:
            u += 1
            range_start = 1 + (u & 1)
        for v in range(range_start, u, 2):
            if gcd(u, v) != 1:
                continue
            a, b = u*u - v*v, 2*u*v
            PrimitiveTripleCache.append((u, v, a, b))
            yield a, b

pt = primitive_triples()
print(pt.__next__())
print(next(pt))
print(PrimitiveTripleCache)


print('\n---------------------------------')

##########################################

def gen_Pythagorean_triplets(i,j):    # by Bogdan Trif
    ''':Usage:      >>> pyt = gen_Pythagorean_triplets(5,5)
                        # >>> next(pyt)
                        # >>> for i in gen_Pythagorean_triplets(8,8): print(i)
    :param i:   i
    :param j:   j
    :return:    a,b,c - pythagorean triplet
    '''
    for m in range(1,i+1):
        for n in range(1, j):
            a = m**2-n**2
            b = 2*m*n
            c = m**2 + n**2
            if a > 0:
                print(m,n,'    ',sorted((a,b,c)))
                yield a,b,c

print('\n#########   MORE ADVANCED METHODS TO GENERATE PYTHAGOREAN TRIPLETS    #################\n')
import itertools
# Method I - With Only One variable :

print(list((a,b,c) for a,b,c in itertools.product(range(1, 100), repeat=3) if a<=b<=c and a**2 + b**2 == c**2))

# Method II - With Only One variable :

print(list(x for x in itertools.product(range(1, 100), repeat=3) if x[0]<=x[1] <=x[2] and x[0]**2 + x[1]**2 == x[2]**2))


print('------------------ RECURSIVE GENERATOR ------------------')

# RECURSIVE GENERATOR

def orduples(size, start, stop, step=1):
    if size == 0:
        yield ()
    elif size == 1:
        for x in range(start, stop, step):
            yield (x,)
    else:
        for u in orduples(size - 1, start, stop, step):
            for x in range(u[-1], stop, step):
                yield u + (x,)
if __name__ == "__main__":
    print(list(orduples(3, 0, 5)))


