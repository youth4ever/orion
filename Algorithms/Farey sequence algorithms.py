import time

# https://en.wikipedia.org/wiki/Farey_sequence
# In mathematics, the Farey sequence of order n is the sequence of completely reduced fractions
# between 0 and 1 which when in lowest terms have denominators less than or equal to n,
# arranged in order of increasing size
# Example : F8 = { 0/1, 1/8, 1/7 ,1/6 ,1/5 ,1/4 ,2/7 ,1/3 ,3/8 ,2/5 , 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8, 1/1 }


############ METHOD 0 ######################

def farey( n, asc=True ):      ####  o(^_^)o  FASTEST  ( ͡° ͜ʖ ͡°)  ### !!! Best Farey Sequence
    ''':Description: Generates INCREASING FAREY SEQUENCE
        taken from http://pythonfiddle.com/farey-series-generator/
        Modified by Bogdan Trif @2017-02-28, 14:00     '''
    F=[]
    if asc:
        a, b, c, d = 0, 1, 1, n
    else:
        a, b, c, d = 1, 1, n-1, n
    i=1
#     print ("%d/%d" % (a,b),)
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
#         print ("%d/%d" % (a,b),end=' ')
        F.append((a,b))
        i+=1
    return F

print(farey(8))


# this is using the gmpy2 mpq fraction module
def farey_frac( n, asc=True ):      ####  o(^_^)o  FASTEST  ( ͡° ͜ʖ ͡°)  ### !!! Best Farey Sequence
    ''':Description: Generates INCREASING FAREY SEQUENCE
        taken from http://pythonfiddle.com/farey-series-generator/
        Modified by Bogdan Trif @2017-02-28, 14:00     '''
    from gmpy2 import mpq
    F=[]
    if asc:
        a, b, c, d = 0, 1, 1, n
    else:
        a, b, c, d = 1, 1, n-1, n
    i=1
#     print ("%d/%d" % (a,b),)
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
#         print ("%d/%d" % (a,b),end=' ')
        F.append( mpq(a,b) )
        i+=1
    F.pop(-1)
    return F

print(farey_frac(8))




########### METHOD I ###############

t1  = time.time()

def farey(limit):
    limit = limit + 1
    not_prime = [False] * limit
    ans = list(range (limit))
    for i in range(2, limit):
        if not_prime[i]:
            continue
        for f in range(i, limit, i):
            not_prime[f] = True
            ans[f] -= ans[f] / i
    return sum(ans) - 1

t2  = time.time()
print('\nCompleted in :', round( (t2-t1)*1000,4), 'ms')             # Completed in : 12685.7255 ms

########### METHOD II ###############

t1  = time.time()


def myfarey(n):
    a,b=1,3
    c0,d0=1,2
    c=c0+a*(n-d0)/b
    d=d0+b*(n-d0)/b
    count=0
    while d>2*c:
        k=int((n+b)/d)
        a, b, c, d = c, d, k*c-a, k*d-b
        count+=1
    print (count)

myfarey(12000)

t2  = time.time()
print('\nCompleted in :', round( (t2-t1)*1000,4), 'ms')

########### METHOD III ###############

t1  = time.time()

import math
def counted_quotients(n):
    """Generate pairs (distinct value, number of occurences ) for
    (n//k for k in range(2, n+1))

    """
    for k in range(2, int(math.sqrt(n)) + 1):
        yield (n//k, 1)
    for q in range(n//int(math.sqrt(n)) - 1, 0, -1):
        if n//q > n//(q+1):
            yield (q, n//q - n//(q+1))

def farey(n, memo={0:1,1:2}):
    if n in memo:
        return memo[n]
    result = n*(n+3)//2 -  sum(f*farey(q) for q, f in counted_quotients(n))
    memo[n] = result
    return result

farey(20)

t2  = time.time()
print('\nCompleted in :', round( (t2-t1)*1000,4), 'ms')


###################### METHOD 4   #########

t1  = time.time()
print('\nCompleted in :', round( (t2-t1)*1000,4), 'ms')

from fractions import Fraction


class Fr(Fraction):
    def __repr__(self):
        return '(%s/%s)' % (self.numerator, self.denominator)


def farey(n, length=False):
    if not length:
        return [Fr(0, 1)] + sorted({Fr(m, k) for k in range(1, n+1) for m in range(1, k+1)})
    else:
        #return 1         +    len({Fr(m, k) for k in range(1, n+1) for m in range(1, k+1)})
        return  (n*(n+3))//2 - sum(farey(n//k, True) for k in range(2, n+1))

if __name__ == '__main__':
    print('Farey sequence for order 1 through 11 (inclusive):')
    for n in range(1, 12):
        print(farey(n))
    print('Number of fractions in the Farey sequence for order 100 through 1,000 (inclusive) by hundreds:')
    print([farey(i, length=True) for i in range(100, 1001, 100)])

t2  = time.time()
print('\nCompleted in :', round( (t2-t1)*1000,4), 'ms')


###################  MY FAREY Sequence, Bogdan Trif #############
from math import gcd
import gmpy2
lim=12
for i in range(1,lim ):
    for j in range(i, lim ):
        if gcd(i,j) ==1 :
            print( gmpy2.mpq(i,j), end=' ')