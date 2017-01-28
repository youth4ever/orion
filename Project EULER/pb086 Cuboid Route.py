#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 5 Nov 2016, 20:56
#The  Euler Project  https://projecteuler.net
'''
                                Cuboid route        -       Problem 86
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner.
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions,
up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100.

This is the least value of M for which the number of solutions first exceeds two thousand;
the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
'''
import time
import itertools
from math import sqrt, gcd
from itertools import count

print('--------------------------- TESTS ----------------------------------')
lim = 3
C = list(itertools.combinations_with_replacement( [i for i in range(1,lim+1)],3 ))
print(len(C),C[0:100])

digit=[1,2,3]
cnt = 0
BASIC_SET = []
for x in range(len(digit)):
    for y in range(x, len(digit)):
        for z in range(y, len(digit)):
            cnt += 1
            print(str(cnt)+".  ",digit[x] ,digit[y],digit[z], end='    ')
            BASIC_SET.append((digit[x] ,digit[y],digit[z]))
print('\n',BASIC_SET)
print('\nNr of Combinations with Replacement as 3 :', cnt)
EXTENDED_SET=BASIC_SET[:]
print('We extend the set with one element, we compute only the difference elements. Not all again :')
cont=0
for x in range(4 ,4+1 ):
    for y in range(1, 4+1):
        for z in range(y, 4+1):
            cont+=1
            print(str(cont)+".  ",x , y, z, end='    ')
            EXTENDED_SET.append((x,y,z))
print('\nIf we extend the set with an additional element the Nr of Combinations ONLY for the element  with Replacement as 3 :', cnt)
print('Total Elements of the Extended SET will be :', len(EXTENDED_SET), EXTENDED_SET)


print('\n==========  My FIRST SOLUTION, BRUTE FORCE, VERY very Slow - 3 hours of run  ===============\n')
t1  = time.time()

M = 30
init_counter = 0
iter=0

for x in range(1, M+1):
    for y in range(x, M+1):
        for z in range(y, M+1):
            x_y__z =  ((x+y)**2 + z**2 )**0.5
            z_y__x = ((z+y)**2 + x**2 )**0.5
            x_z__y = ((x+z)**2 + y**2 )**0.5
            if min (x_y__z, z_y__x, x_z__y) % 1 == 0 :
                init_counter+=1
                # iter+=1
                # print(x,y,z,' .     ',  x_y__z, z_y__x, x_z__y)
            # if iter % 1e6 ==0 : print(iter)
print(M, init_counter)
# M=1310 500157  ;   1446 619720; 1647 810743   ;   1817 999850
counter=init_counter
# while counter < 1e6 :
#     M+=1
#     for t in range(M ,M+1 ):
#         for u in range(1, M+1):
#             for v in range(u, M+1):
#                 t_u__v =  ((t+u)**2 + v**2 )**0.5
#                 v_u__t = ((v+u)**2 + t**2 )**0.5
#                 t_v__u = ((t+v)**2 + u**2 )**0.5
#                 if min (t_u__v, v_u__t, t_v__u) % 1 == 0 :
#                     counter+=1
#     print(M, counter)

print('\nCounter : ',counter, '  for the least value of M : ', M)       # Counter :  1000457   for the least value of M :  1818

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

print('\n==========  My SECOND SOLUTION,  Learnt Solution Using Pythagorean Triplets ===============\n')
# Idea from Roderic
def pythagorean_triple(plim):
    '''
    a^2 + b^2 = c^2
    a = m^2 - n^2
    b = 2mn
    c = m^2 + n^2
    k [ a + b + c = p = 2 * m * ( m + n ) ]

    >>> next(pythagorean_triple(30))
    Pythagorean triplets with this property that the greatest common divisor of
    any two of the numbers is 1 are called primitive Pythagorean triplets.
    '''
    for m in count(1):
        if 2*m**2 > plim:
            break
        for n in range( 1 + m%2, m, 2):
            if gcd(m, n)==1:
                p = 2 * m * (m+n)
                a, b, c = m**2-n**2  ,    2*m*n ,     m**2+n**2
                for k in range(1, plim//p + 1):
                    # print( str(iter)+'.    ',  (k*a, k*b, k*c))
                    yield (k*a, k*b, k*c)
lim=100

def pb086():
    ''' SUPER INTERESTING APPROACH

    'Very interesting approach here, Normally for 3,4,5 we need the sides (b,c) = (3,4) to decompose have 2 cases :
    case1: decompose 3 : gives only 1 possibility : (1,2) as  sides for the cuboid
    case2 : decompose 4 : => 2 possibilities (1,3) and (2,2) as sides for cuboid
    He observes that there is no need to calculate partition for 3 or 4 number because  the formulas he used gives this result.
        :Example:  we take the triplet :  12,16,20 =>

            :case1: a=12 partitioned in: (1,11), (2,10), (3,9), (4,8), (5,7), (6,6) <-- in total 6 possibilities => he adds  a//2
                giving the cuboids : (1,11,16), (2,10,16), (3,9,16), (4,8,16), (5,7,16), (6,6,16) which are all valid because i<=j<k
            :case2:  b=16 partitioned in ... b//2 = 8 possibilities (1,15), (2,14), (3,13), (4,12), (5,11), (6,10), (7,9), (8,8)
                giving the cuboids : (1,15,12), (2,14,12), (3,13,12), (4,12,12), (5,11,12), (6,10,12), (7,9,12), (8,8,12) from which only the last
                4 are respecting the constraint i<=j<k, specifically a<=b<c  imposed by the Pythagorean theorem a**2+b**2=c**2

                So, we must subtract the cases in which the condition are not met with : b//2 -(b-a)+1 : 16//2-(16-12)+1= 8-4+1=5.
                This is added to the already existing entry from the previous Pythagorean numbers, if you look in the table:
                previous = 4 , now =5 => 9
    '''
    lim = 10000
    table = [0] * lim
    iter = 0
    for a, b, c in map(sorted, pythagorean_triple(lim)):
        iter+=1
        table[a] += max(0, b//2 - (b-a) + 1)        # Very interesting approach here, Normally for 3,4,5 we need the sides (b,c) = (3,4) to
        table[b] += a//2                   #  decompose have 2 cases :       case1: decompose 3 : gives only 1 possibility : (1,2) as  sides for the cuboid
        print(str(iter)+'.  ',a,b,c,'   ',table[a], table[b], table[0:30])          # case2 : decompose 4 : => 2 possibilities (1,3) and (2,2) as sides for cuboid
    return next(M for M in range(lim) if sum(table[:M+1]) > 1E6)    # he observes that there is no need to calculate partition for 3 or 4 number because :
                                                                                            # the formulas he used gives this result.
print(pb086()) # MUST FINISH THIS IN MY WAY !!!!!!!!!!



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

print('\n--------------------------SOLUTION 1, VERY FAST, ,Using Pythagorean Triplets, Roderic, Canada --------------------------')
t1  = time.time()

# I found this one quite tough, but I like the final implementation

from itertools import count
from math import gcd

def pythagorean_triple(plim):
    '''
    a^2 + b^2 = c^2

    a = m^2 - n^2
    b = 2mn
    c = m^2 + n^2

    k [ a + b + c = p = 2 * m * ( m + n ) ]

    #>>> next(pythagorean_triple(30))
    '''
    for m in count(1):
        if 2*m**2 > plim:
            break
        for n in range( 1 + m%2, m, 2):
            if gcd(m, n)==1:
                p = 2 * m * (m+n)
                a, b, c = m**2-n**2, 2*m*n, m**2+n**2
                for k in range(1, plim//p+1):
                    yield (k*a, k*b, k*c)

def problem0086():
    ''' SUPER INTERESTING APPROACH
    'Very interesting approach here, Normally for 3,4,5 we need the sides (b,c) = (3,4) to decompose have 2 cases :
    case1: decompose 3 : gives only 1 possibility : (1,2) as  sides for the cuboid
    case2 : decompose 4 : => 2 possibilities (1,3) and (2,2) as sides for cuboid
    He observes that there is no need to calculate partition for 3 or 4 number because  the formulas he used gives this result.
        :Example:  we take the triplet :  12,16,20 =>

            :case1: a=12 partitioned in: (1,11), (2,10), (3,9), (4,8), (5,7), (6,6) <-- in total 6 possibilities => he adds  a//2
                giving the cuboids : (1,11,16), (2,10,16), (3,9,16), (4,8,16), (5,7,16), (6,6,16) which are all valid because i<=j<k
            :case2:  b=16 partitioned in ... b//2 = 8 possibilities (1,15), (2,14), (3,13), (4,12), (5,11), (6,10), (7,9), (8,8)
                giving the cuboids : (1,15,12), (2,14,12), (3,13,12), (4,12,12), (5,11,12), (6,10,12), (7,9,12), (8,8,12) from which only the last
                4 are respecting the constraint i<=j<k, specifically a<=b<c  imposed by the Pythagorean theorem a**2+b**2=c**2

                So, we must subtract the cases in which the condition are not met with : b//2 -(b-a)+1 : 16//2-(16-12)+1= 8-4+1=5.
                This is added to the already existing entry from the previous Pythagorean numbers
    '''
    lim = 10000
    table = [0] * lim
    iter = 0
    for a, b, c in map(sorted, pythagorean_triple(lim)):
        iter+=1
        table[a] += max(0, b//2 - (b-a) + 1)        # Very interesting approach here, Normally for 3,4,5 we need the sides (b,c) = (3,4) to
        table[b] += a//2                   #  decompose have 2 cases :       case1: decompose 3 : gives only 1 possibility : (1,2) as  sides for the cuboid
        # print(str(iter)+'.  ',a,b,c,'   ',table[a], table[b], table[0:30])          # case2 : decompose 4 : => 2 possibilities (1,3) and (2,2) as sides for cuboid
    return next(M for M in range(lim) if sum(table[:M+1]) > 1E6)    # he observes that there is no need to calculate partition for 3 or 4 number because :
                                                                                            # the formulas he used gives this result.
print(problem0086())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 2, chays --------------------------')
t1  = time.time()
# So I approached this using Pythagorean triples.
from math import ceil
from itertools import chain, combinations
import copy


def factor(n):
    #factors n
    Factors = {}
    if n%2 ==0:
        Factors[2]=1
        n = n//2
        while n%2==0:
            Factors[2]+=1
            n = n//2
    p=3
    while n>1:
        if n%p==0:
            Factors[p]=1
            n=n//p
            while n%p==0:
                Factors[p]+=1
                n=n//p
        else:
            p+=2
    return Factors

def PowerSet(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

def Split(n):
    # will return all ways to write n as kpq where p>q and (p,q)=1
    Factors = factor(n)
    ListFactors = []
    Splittings = set()

    for key in Factors:
        ListFactors.extend([key]*Factors[key])

    for Knumbers in PowerSet(ListFactors):
        PQfactors = copy.deepcopy(Factors)
        K = list(Knumbers)
        for i in Knumbers:
            PQfactors[i]-=1
            if PQfactors[i]==0:
                PQfactors.pop(i)
        for Pnumbers in PowerSet(PQfactors):
            P = []
            Q = []
            Qfactors = copy.deepcopy(PQfactors)
            for number in Pnumbers:
                P.extend([number]*Qfactors[number])
                Qfactors.pop(number)
            for number in Qfactors:
                Q.extend([number]*Qfactors[number])
            p = 1
            for i in P:
                p *= i
            q = 1
            for i in Q:
                q *= i
            if p>q:
                k = 1
                for i in K:
                    k *= i
                Splittings.add((k,p,q))
    return Splittings

def PythagoreanTriples(n):
    # want to return all m where m^2 + n^2 + p^2 is a pythagorean triple where m<n<p
    Triples = []
    if n%2 == 0:
        for s in Split(n//2):
            if s[0]*(s[1]**2 - s[2]**2) <= 2*s[0]*s[1]*s[2]:
                Triples.append(s[0]*(s[1]**2 - s[2]**2))
    else:
        for s in Split(n):
            if s[0]*(s[1]**2 - s[2]**2) <= 2*s[0]*s[1]*s[2]:
                Triples.append(s[0]*(s[1]**2-s[2]**2)//2)
    return Triples

N = 10**6
count = 0
n = 1
PT = {}

while count < N:
    for m in PythagoreanTriples(n):
        if n in PT:
            PT[n]+=m//2
        else:
            PT[n]=m//2
        if m in PT:
            PT[m]+=max([0,m-ceil(n/2)+1])
        else:
            PT[m]=max([0,m-ceil(n/2)+1])
    if n%2 == 0 and n//2 in PT:
       count+= PT[n//2]
    n+=1

print(n//2,count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 4447.254419 ms

'''     inamori, Japan - VERY GOOD Explanation
Let us take a right triangle. For example, (3, 4, 5).
Dividing one of 2 edges forming the right angle, we can make a cuboid.
Dividing 3 makes a cuboid (1, 2, 4).
Dividing 4 makes 2 cuboids (2, 2, 3), (1, 3, 3).

For M = 20, there are 6 triangles similar to (3, 4, 5).

(3, 4, 5), (6, 8, 10), ... (18, 24, 30)

But, Dividing 18 makes no cuboid. There are 5 triangles for dividing 3.
The number of cuboids is able to be calculated O(1).

For dividing 3,

1 + 3 + 4 + 6 + 7 = 21

For dividing 4,

2 + 3 + 4 + 5 + 6 + 7 = 27
'''
# The IDEA of solution:
# First let s look at the net of a cuboid with dimensions a x b x c, when a>=b>=c.
#  Then we can see, that the shortest path for this cuboid goes through the longest side 'a' and
# has the length equal to sqrt(a^2+(b+c)^2).
# Now, we need to check 2 things:
# 1) Whether the number sqrt(a^2+(b+c)^2) is an integer.
# 2) How many options do we have to write the sum "b+c" as a sum of two other positive integers, when c<=b<=a.
# In other words, we'll find all pairs of positive integers (c , b), such that c<=b<=a and their sum is equal to the integer "b+c" above.
# Here is realization in python:



print('\n--------------------------SOLUTION 3, , INCREDIBLE FAST, philiplu  , USA --------------------------')
t1  = time.time()
# 37 msec.  Generates Pythagorean triples, and binary searches for the correct M, same as many other submissions.
# Algorithm comments in the code header.

"""
So this is a problem of looking for pythagorean triples.

Consider a room of dimensions l by w by h.  There are three paths the spider
can take, which have the following lengths:

    h^2 + (w+l)^2
    w^2 + (h+l)^2
    l^2 + (w+h)^2

Assume, without loss of generality, that l >= w >= h.  Then those three paths
are in the order

    l^2 + (w+h)^2 <= w^2 + (h+l)^2 <= h^2 + (w+l)^2

The problem says the shortest of those must have an integer length, so we are
tasked with finding pythagorean triples (l, w+h, sqrt(l^2+(w+h)^2)), where l,
w, and h are <= M and h <= w <= l, w+h < 2*l.

Generate primitive triples (a, b, c), where a < b < c.  For each primitive
triple, handle two cases:

Case 1: Take a = l, b = w+h.  If w+h > 2*l, then ignore this triple (as either
w or h will be greater than l).  Otherwise, count the partitions of b which
assign different values to w and h, arbitrarily keeping w >= h to avoid
double-counting symmetries, and ignoring partitions where w or h > l.  This
gives us the partitions h = (b-l) (and w = l) through h = int(b/2).  Also count
the non-primitive triples (ka, kb, kc) for k in the range 2 up to min(int(M/a),
int(2*M/b)), counting partitions similarly.

Case 2: Take a = w+h, b = l.  There are int(a/2) partitions that contribute to
the count of shortest paths for the primitive tuples, and int(k*a/2) partitions
for the non-primitive multiple triples, for k up to min(int(2*M/a), int(M/b)).

To count the integral shortest paths for a given M, count the paths generated
by triples as described above.  Keep generating triples until all the primitive
tuples for a given value of u have no possible paths because the upper limit
for the k multiple in both cases is zero.  Use a binary search to find the M
corresponding to a desired count.
"""
import sys
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

def count_integral_shortest_paths(M):
    count = 0
    done = False
    prev_a = 0
    for a, b in primitive_triples():
        if a > prev_a:
            # ascending 'a' means the generator switched to a higher 'u'.  If
            # we never saw possible triples to test from the old value of 'u',
            # we're done.
            if done:
                break
            done = True
        prev_a = a
        if a > b:   # sort a < b for consistency
            a, b = b, a
        # Handle case where a=l, b=w+h
        if a <= M:
            kmax =  min(M//a, 2*M//b)
            if kmax > 0:
                done = False
                if b < 2*a:
                    for k in range(1, kmax+1):
                        count += (k*(2*a - b) + 2) // 2
        # Handle case where a=w+h, b=l
        if b <= M:
            kmax = min(2*M//a, M//b)
            if kmax > 0:
                done = False
                for k in range(1, kmax+1):
                    count += k * a // 2
    return count

def p86(desired_count = 1000000):
    # Find a starting range (M_1, M_2) where count(M_1) < desired < count(M_2)
    low = (1, 0)
    high = (250, count_integral_shortest_paths(250))
    # print(low, high)
    while high[1] < desired_count:
        new_high = 2 * high[0]
        low, high = high, (new_high, count_integral_shortest_paths(new_high))
        # print(low, high)
    if high[1] == desired_count:    # really unlikely, but check
        return high[0]
    # Binary search so M_1 + 1 = M_2 and count(M_1) < desired < count(M_2)
    while high[0] > low[0] + 1:
        mid = (high[0] + low[0]) // 2
        mid_count = count_integral_shortest_paths(mid)
        if mid_count == desired_count:
            return mid
        elif mid_count < desired_count:
            low = (mid, mid_count)
        else:
            high = (mid, mid_count)
        # print(low, high)
    return high[0]

print(p86(*(int(arg) for arg in sys.argv[1:])))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 4, oinil, China--------------------------')
t1  = time.time()

#!/usr/bin/env python

def int_cube(x0, y0):
    z2 = x0 * x0 - y0 * y0
    z1 = round(z2 ** 0.5)
    if z1 * z1 == z2:
        return z1
    else:
        return 0

def main(N):
    count = 0
    n = 1
    while True:
        n += 1
        for i in range(n + 1, int(5**0.5 * n) + 1):
            j = int_cube(i, n)
            if j == 0:
                continue
            for a in range(1, n + 1):
                b = j - a
                if 1 <= a <= b <= n:
                    count += 1
        if count >= N:
            break
    print(n)

import sys
N = 1e6             #N = int(sys.argv[1])
main(N)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n--------------------------SOLUTION 5, --------------------------')
t1  = time.time()
# The IDEA of solution:
# First let s look at the net of a cuboid with dimensions a x b x c, when a>=b>=c.
#  Then we can see, that the shortest path for this cuboid goes through the longest side 'a' and
# has the length equal to sqrt(a^2+(b+c)^2).
# Now, we need to check 2 things:
# 1) Whether the number sqrt(a^2+(b+c)^2) is an integer.
# 2) How many options do we have to write the sum "b+c" as a sum of two other positive integers, when c<=b<=a.
# In other words, we'll find all pairs of positive integers (c , b), such that c<=b<=a and their sum is equal to the integer "b+c" above.
# Here is realization in python:

from math import sqrt

m=3000
limit=pow(10,6)      # The limit on number of solution given in the problem

b_plus_c_values=[]          # This array keeps in how many ways it's possible to write a positive integer b+c (when c<=b<=a)
for i in range(0,2*m+1):    # as a sum of two other positive integers.
    b_plus_c_values.append(0)

#..........................................................................................................................

def is_it_integer(a,b):     # This function checks whether the square root of a^2+b^2 is an integer.
    temp=int(sqrt(a*a+b*b))
    if( temp*temp==a*a+b*b ):
        return 1
    return 0


#..........M  A  I  N......................................................................................................

number_of_solutions=0
flag=1      # The 'flag' will be up as long as the number of solution doesn't exceed the given limit.
a=0
while (a<m+1 and flag):
    a+=1
    for b in range(2,2*a+1):   # For every length 'a' of the longest dimension, let 'b' be the sum of two smallest dimensions.
                   # Because both of them are less than 'a', 'b'<=2*a. And we're going to fill the array:
        if(b<=a+1):  # If 'b' is less or equil to a+1, then the number of options for the sum is an integer part of b/2.
            b_plus_c_values[b]=b/2
        else:        # Otherwise, for every 'b'>a+1, the the number of options for 'b'=(a+1)+k is the same as the number
            b_plus_c_values[b]=b_plus_c_values[2*(a+1)-b]  # of options for 'b'=(a+1)-k.
        if(is_it_integer(a,b)):    # If the length is an integer, add the number of options above to the total number
            number_of_solutions+=b_plus_c_values[b]     # of the solutions.
            if(number_of_solutions>limit):
                flag=0
                break

print ("The least value of M such that the number of solutions first exceeds one million is", a)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, mmaximus, Portugal--------------------------')
t1  = time.time()
# Like most people. After noticing the unfolding (a+b)**2 + c**2 thing, it is simply a matter of iterating
# through pythagorean triples x < y < z, with an appropriate bound, and counting how many ways
# we can decompose x (or y) into a sum of two numbers keeping in mind that y (or x) has to be the largest
# in the cuboid, for the path to be minimal. Do that for every time the triple 'fits' into the MxMxM box after scaling.
#
# I could have written something to generate additional triples on demand + some bisection method to find the solution,
# but was lazy and just iterated manually until the solution was found.
#
# I used the generating method described here:
# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

from math import sqrt
import numpy as np

A = np.array([[1, -2, 2], [2, -1, 2], [2, -2, 3]])
B = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
C = np.array([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])

triplets = list()
def spawn_triplets(t, L):
    d = np.dot
    if t[2] <= L:
        for X in (A,B,C):
            new = d(X, t)
            if new[2] <= L:
                triplets.append(new)
                spawn_triplets(new, L)

M = 1818
L = sqrt(5) * M
spawn_triplets(np.array([3, 4, 5]), L)
triplets.append(np.array((3, 4, 5)))

n_solutions = 0
for t in triplets:
    x, y, _ = sorted(t)  # y is the biggest non-hypotenuse

    # Case 1: y is the larger side in the cuboid
    K = M // y  # This automatically takes care of the triplets that don't fit
    for i in range(K):
        n_solutions += ((i+1)*x) // 2

    # Case 2: x is the larger side in the cuboid
    if y <= 2 * x:
        K = M // x
        for i in range(K):
            n_solutions += ((i+1)*(2*x-y))//2 + 1

print(n_solutions)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,  Avi Levy, USA--------------------------')
t1  = time.time()

from math import sqrt

def p086():
  s = i = 0
  while True:
    i += 1
    for q in range(2,2*i+1):
      n = i**2+q**2
      if n == int(sqrt(n))**2:
        s += (q//2 - max(1, q-i) + 1)
        if s > 10**6:
          return i
print(p086())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 11147.637606 ms


print('\n--------------------------SOLUTION 8, zdkim  --------------------------')
t1  = time.time()
# I saw nice codes in this thread with the equivalent performance with this.
# But mine is the shortest and I think it's worth adding one more code. 22ms

#a, b, c = m**2-n**2, 2mn, m**2+n**2
#M >= l >= w >= h

M = 2000
big = {x:set() for x in range(1,M+1)}
for m in range(2,M):
    for n in range(1, min(m, int(M/m)+1)):
        wh, l = max(m*m - n*n , 2*m*n), min(m*m-n*n , 2*m*n)
        if wh <= 2*l:
            for i in range(1, int(M/l)+1):
                big[l*i].add(wh*i)
        wh, l = l, wh
        for i in range(1, int(M/l)+1):
            big[l*i].add(wh*i)

def prob86(big):
    rs = 0
    for l in range(1,M+1):
        for wh in big[l]:
            if wh > l: rs += l-(wh-1)/2
            else: rs += wh/2
            if rs > 1000000:
                return l
    return 0

print (prob86(big))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 9, hsiu, Taiwan--------------------------')
t1  = time.time()
# Binary search for the answer M...
# For a given M, go through all Pythagorean Triples whose two smallest numbers can break into 3 numbers smaller than M.

from math import sqrt
import time

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

lb = 0
ub = 5000
goal = 1000000

while ub-lb > 1: # binary search
    ans = 0
    mid = (ub + lb) / 2
    MAX = int(mid)
    for n in range(1, int(sqrt(MAX))):
        for m in range(n+1, MAX+1):
            a = m*m-n*n
            b = 2*m*n
            if gcd(a, b) != 1: continue
            if a > b: (a, b) = (b, a) # make sure a < b
            for k in range(1, MAX):
                bb = k*b
                if bb > 2*MAX:
                    break
                aa = k*a
                if bb <= MAX:
                    ans += aa/2 - max(0, aa-MAX-1)
                if bb < 2*aa and aa <= MAX:
                    ans += (aa+aa-bb + 2)/2
    if ans < goal:
        lb = mid
    else:
        ub = mid
    print( 'M =', MAX, '#int solution: ', ans)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')