
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



print('\n---------------- Triangle Primitive Triplets of 90 degrees ------------------ ')

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



def compute_triangle_angles( sides ):   # o(^_^)o #  Made by Bogdan Trif @ 2017-02-19, 12:20
    ''':Description: given a triangle with sides a,b,c the function computes all its angles.
        It uses the LAW OF SINES , where A,B,C are the angles opposed to corresponding sides a,b,c
        sin(A)/a =sin(B)/b =sin(C)/c
        and the LAW OF COSINES c**2 = a**2 + b**2 - 2*a*b * cos(C)
    :returns: A,B,C, the three corresponding angles    '''
    from math import sqrt, cos, sin, pi, acos, asin
    a, b, c = sides[0], sides[1], sides[2]
    C = acos((a**2+b**2-c**2)/(2*a*b) )*180/pi
    A = asin(( a*sin(C*pi/180) )/c )*180/pi
    B = asin(( b*sin(C*pi/180) )/c )*180/pi
    return A, B, C

print('\ncompute_triangle_angles :\t', compute_triangle_angles( (19, 261, 271) )  )


print('\n---------------- Triangle Primitive Triplets of 120 degrees ------------------ ')

def triangle_primitive_triplets_120_gen(  ) :      # o(^_^)o #  Made by Bogdan Trif @ 2017-02-19, 13:10
    ##### 120 degree TRIANGLES GENERATOR
    # http://www.geocities.ws/fredlb37/node9.html
    ''':Description: GENERATOR for Triangle primitive triplets of 120 degrees
    :param up_lim: integer, the limit to which the sum of sides a,b,c is up to
    :return: the sides of the 120 degree triangle , p ,q, r   '''
    from math import gcd
    # cnt=0
    m, n = 1, 1
    while True :   # If needed we can set a limit based on m**2-n**2
        for n in range(1, m) :      ### range(1,m) as we need only p > 0 !!!!!!!!
            if gcd(m,n)==1 and (m-n)%3 !=0  :         #!!!! if we omit the %3 condition we will get duplicates !!!
                p = (m**2-n**2)
                q = (2*m*n+n**2)
                r = (m**2+n**2+m*n)
                if p > 0 :
                    # cnt+=1
                    # print(str(cnt)+'.         '  , p, q, r ,'       sum =',  p+q+r ,'            m,n =',m, n)#, compute_triangle_angles( [ p, q, r ] )  )
                    yield p,q, r
        m+=1

TPT = triangle_primitive_triplets_120_gen(  )
for i in range(40):
    print(next(TPT))


print('\n---------------- Triangle Primitive Triplets of 60 degrees ------------------ ')

def triangle_primitive_triplets_60_gen(  ) :      # o(^_^)o #  Made by Bogdan Trif @ 2017-02-21, 16:10
    ##### 60 degree TRIANGLES GENERATOR
    # http://www.geocities.ws/fredlb37/node9.html
    ''':Description: GENERATOR for Triangle primitive triplets of 60 degrees
    :param up_lim: integer, the limit to which the sum of sides a,b,c is up to
    :return: the sides of the 60 degree triangle , p ,q, r   '''
    from math import gcd
    cnt=0
    m, n = 1, 1
    while True :   # If needed we can set a limit based on m**2-n**2
        for n in range(1, m) :      ### range(1,m) as we need only p > 0 !!!!!!!!
            if gcd(m,n)==1 and (m-n)%3 !=0  :         #!!!! if we omit the %3 condition we will get duplicates !!!
                a = 2*m*n + m**2
                b = 2*m*n + n**2
                c = m**2+n**2+m*n
                cnt+=1
                # print(str(cnt)+'.         '  , a, b, c ,'       sum =',  a+b+c ,'            m,n =',m, n)
                yield a, b, c
        m+=1

TPT60 = triangle_primitive_triplets_60_gen(  )
for i in range(40):
    f = next(TPT60)
    print(f,'     angles : ', compute_triangle_angles(f))


##################################################
print('\n-----------------------------------')



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


print('\n########### MATRIX METHOD TO GENERATE PYTHAGOREAN TRIPLETS ##########\n')
########### MATRIX METHOD TO GENERATE PYTHAGOREAN TRIPLETS ##########
# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
# https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples


def vecprod(M,V):
  nlM=len(M)
  return [sum([l[j]*V[j] for j in range(nlM)]) for l in M]

pmax=10**2
A=[[1,-2,2],[2,-1,2],[2,-2,3]]
B=[[1,2,2],[2,1,2],[2,2,3]]
C=[[-1,2,2],[-2,1,2],[-2,2,3]]
listmat=(A,B,C)

liste=[[3,4,5]]
compte=0

while liste:
    list2=[]
    for t in liste:
        for m in listmat:
            t2=sorted(vecprod(m,t))
            p=sum(t2)
            if p<pmax:
                list2.append(t2)
    liste=list(list2)
    print(liste)


