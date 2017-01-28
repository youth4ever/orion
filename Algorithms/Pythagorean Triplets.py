
from itertools import count, product
from math import gcd

def Pythagorean_Triples_gen(plim):          ### ( ͡° ͜ʖ ͡°)  ### Last Modif  by Bogdan Trif @ 2017-01-21, 20:45
    ''':Description: Generator for Pythagorean Triplets with their multiples until an up_limit, plim
        which is the Perimeter of the triangle.
        :Formulas used: :
    a^2 + b^2 = c^2     ;
        a = m^2 - n^2       ;
    b = 2mn     ;
        c = m^2 + n^2        ;
            k [ a + b + c = p = 2 * m * ( m + n ) ]     ;

    :Usage: >>> next(pythagorean_triple(30))
    Pythagorean triplets with this property that the greatest common divisor of
    any two of the numbers is 1 are called primitive Pythagorean triplets.
        :param: **plim** --> int,  limit of the perimeter of the triangle
    '''
    m = 1
    while 2*m**2 < plim:
        for n in range( 1 + m%2, m, 2):
            if gcd(m, n)==1:
                p = 2 * m * (m+n)
                a, b, c = m**2-n**2  ,    2*m*n ,     m**2+n**2
                for k in range(1, plim//p + 1):
                    yield (k*a, k*b, k*c)
        m+=1

P = Pythagorean_Triples_gen(100)
for i in P:    print( i)

print('\n---------------------------------')
######################################



print('\n---------------------------------')

##########################################

def Pythagorean_primitive_triplets_gen():    # by Bogdan Trif @ 2017-01-21, 16:30     ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ###
    ''':Usage:      >>> pyt = Pythagorean_primitive_triplets_gen()
                        # >>> next(pyt)
                        # >>> for i in Pythagorean_primitive_triplets_gen(): print(i)
    :param i:   i
    :param j:   j
    :return:    a,b,c - primitive pythagorean triplet
    '''
    m = 1
    while True :
        for n in range(1, m):           ### range(1,m) as we need only a > 0 !!!!!!!!
            a = m**2-n**2
            b = 2*m*n
            c = m**2 + n**2
            if gcd(a,b) ==1 :           #   Assure that we generate ONLY primitive Pythagorean triplets
                # print(' m, n = \t',m, n,'            a,b,c =\t',sorted((a,b,c)))
                yield a,b,c
        m+=1

PT = Pythagorean_primitive_triplets_gen()
cnt=0
for i in range(100) :
    cnt+=1
    print(str(cnt)+'.     ',next(PT))


print('\n-----------------------------------------------------\n')

##################################################




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


print('\n#########   LIST COMPREHENSIONS METHODS TO GENERATE PYTHAGOREAN TRIPLETS    #################\n')
import itertools
# Method I - With Only One variable :

print(list((a,b,c) for a,b,c in itertools.product(range(1, 100), repeat=3) if a<=b<=c and a**2 + b**2 == c**2))

# Method II - With Only One variable :

print(list(x for x in itertools.product(range(1, 100), repeat=3) if x[0]<=x[1] <=x[2] and x[0]**2 + x[1]**2 == x[2]**2))




