#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Wed, 14 Dec 2016, 00:03
#The  Euler Project  https://projecteuler.net
'''
Singleton difference        -       Problem 136

The positive integers, x, y, and z, are consecutive terms of an arithmetic progression.
Given that n is a positive integer, the equation,

                x**2 − y**2 − z**2 = n,         has exactly one solution when n = 20:

                13**2 − 10**2 − 7**2 = 20

In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

How many values of n less than 5*10**7 ( fifty million ) have exactly one solution?

'''
from math import gcd, sqrt
from pyprimes import factorise
import time, sys
import functools, operator


def get_divisors(n):      ### o(^_^)o  FASTEST  o(^_^)o  ### !! FIRST FASTEST
  factors = set()
  for x in range(1, int(sqrt(n)) + 1):
    if n % x == 0:
      factors.add(x)
      factors.add(n//x)
  return sorted(factors)

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


def prime_generator(n):      ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.
    """
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (n // cand[i]) - (n // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]


def singleton_set(n):           # CALIBRATED
    B=[]
    for x in range(3*n//2, 1, -1) :
        for p in range(1, 2*n//3+1) :
            y , z = x-p, x-2*p
            if y>0 and z > 0 :
                if  ( x**2 - y**2 - z**2 == n )  :
                    B.append((n, x, y, z , p, x+y+z, gcd(n, x+y+z) ))
                    if len(B) ==2 : break
    return B

# (n, x, y, z , p,  x+y+z, gcd(n, x+y+z) ))
def get_xyz(n) :
    B=[]
    D = get_divisors(n)[1:]
    for y in D :
        p = (n+y**2)/(4*y)
        if p % 1 == 0 and y - p > 0 :
            p = int(p)
            x , z = y+p, y-p
            if  ( x**2 - y**2 - z**2 == n )  :
                B.append( (n, x , y, z, p,  x+y+z, y )  )
        if len(B) == 2 : break
    return B


def get_singleton(F):
    n = functools.reduce(operator.mul, F)
    if len(F) <= 2:
        y = F[-1]
    if 3 <= len(F) <=4 :
        y = F[-1]*2
    if len(F) > 4 :
        y = F[-1]*4

    p = (n+y**2)/(4*y)

    if p % 1 == 0 and y - p > 0 :
        p = int(p)
        x , z = y+p, y-p
        # if  ( x**2 - y**2 - z**2 == n )  :
        return True #return (n, x , y, z, p,  x+y+z, y )
    else:
        return ()


# primes = prime_generator(5*10**7)
# print(len(primes) , primes[-1] ,primes[0:100],'\n')


print('\n--------------------------TESTS------------------------------')

print('Test get_xyz :\t', get_xyz(284))
print('Test get_xyz :\t', get_xyz(1616))
print('Test get_xyz :\t', get_xyz(32))
print('Test get_xyz :\t', get_xyz(124))
print('Test get_xyz :\t', get_xyz(124))

print()

print('Test get_singleton :\t', get_singleton([2, 2, 71]))
print('Test get_singleton :\t', get_singleton([2, 2, 2, 2, 101]))
print('Test get_singleton :\t', get_singleton([2, 2, 2, 2, 2]))
print('Test get_singleton :\t', get_singleton([2, 2, 2, 2, 31]))
print('Test get_singleton :\t', get_singleton([2, 2, 31]))

print('\n-------------------------- INITIAL CALIBRATION SOLUTION------------------------------')
t1  = time.time()

def initial_calibration(up_range) :
    V =[]
    cnt=0           # SUCCESS
    for n in range(2, up_range):
        f = get_factors(n)
        s = get_xyz(n)
        r = get_singleton(f)
        if len(s) == 1 :
            cnt+=1
            print(str(cnt)+'.   ', f ,'      ',s ,'     ', r)
            V.append(n)
    return print('\nAnswer :\r', cnt)

# initial_calibration(8*10**4)

# @ 2016-12-13, 14:30 --> Observe that  [(39, 17, 13, 9)], 11.          [(44, 28, 22, 16)]          12.          [(48, 16, 12, 8)]   13.          [(51, 22, 17, 12)]
# the sum of x+y+z with n ==> gcd (n, x+y+z) != 1         !!!!!!!!!!!!!!!!!!!! WOW, Even more --> Watch the pattern :

    # (n, x, y, z , p, x+y+z, gcd(n, x+y+z) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def final_solution_pb136(up_range):
    # primes = [ prime for prime in prime_generator(up_range) if prime%4 ==3 ]
    primes = prime_generator(up_range)
    cnt=1
    for n in primes :
        s = get_singleton([n])
        if s == True : #len(s) > 1 :
            cnt+=1
            # print(str(cnt)+'.   '   , s)
        if n < up_range//16 :
            m = [2, 2, 2, 2, n]
            s = get_singleton(m)
            if s== True : # len(s) > 1 :
                cnt+=1
                # print(str(cnt)+'.   ' , f,'      ' , s)
        if 1 <n < up_range//4 :
            o = [2, 2, n]
            s = get_singleton(o)
            if s == True : #len(s) > 1 :
                cnt+=1
                # print(str(cnt)+'.   ' , f,'      ' , s)
        if cnt % 25445 ==0 :        # Progress Bar #
            h = cnt//25445
            # sys.stdout.write("\r%d%%-" %h )
            sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold
            # sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(100-h) +']' )         #  Calibri, Adjust the numbers, for the font of your configuration
            sys.stdout.flush()

            # print(  str(h)+'   %', end='\r' )
    # return print('\nAnswer :\t', cnt)

final_solution_pb136(5*10**7)           # Answer : 2544559
# final_solution_pb136(8*10**4)

# print('[',' '*220,']')
# print('-'*100)
# print('. '*100)
# print(';'*100)
# print('_'*100)
# print('#'*100)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 56510.23221 ms

# print('\n================  My SECOND SOLUTION,   ===============\n')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 56510.23221 ms


# print('\n-------------- COMPARISON OF LISTS --------------')
#
# print('V:', len(V),sorted(V))
# print('W:',len(W),sorted(W))









print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

### GENERAL IDEAS ####
# =====   Wed, 14 Dec 2016, 02:31, night.train, USA
#
# Like mentioned above, solutions are:
# 1) Any prime of form 3 mod 4
# 2) 4 * any odd prime (and 4 itself is a soln)
# 3) 16 * any odd prime (and 16 itself is a soln)
#
# My prime sieve on 50 MM numbers ran in 70 seconds. Not good enough! So I built a sieve that focused on 3 mod 4.
#
# I ran a general prime sieve to 12.5 MM (50 MM/4) which only took 1.5 seconds.
# From that prime list, I took only the primes that were of the form 3 mod 4.
# Any larger composite number of the form 3 mod 4 would have to be divisible by one of those primes,
# so I used those primes to sieve the numbers between 12.5 MM and 50 MM.
# Any untouched number that was 3 mod 4 had to be prime.
# I was pleasantly surprised by how fast it ran!


print('\n--------------------------SOLUTION 1,  SLOW --------------------------')
t1  = time.time()
# ====== Mon, 29 Apr 2013, 22:43, jbum, USA
# I noticed that the solutions formed spokes that are straight lines.  For each spoke S, the slope of the line is 4S. If a point in a spoke is (d,z)
# where n = (z+2d)**2 - (z+d)**2 - z**2
#
# then the next point in the spoke is (d+1,z+3) and it's value is n+4S
# I made a program that follows out each spoke, and spits out the root nodes of successive spokes as it finds them.
# Eventually, the spokes start above the limit, and we can stop.  This ran in about 106 seconds.

def jbum():
    dct = {}
    limit = 10**6*50

    spokes = {1:(1,2)}
    s = 1
    while s in spokes:
      (d,z) = spokes[s]
      delta = s*4
      n = (z+2*d)**2 - (z+d)**2 - z**2
      # print ("spoke",s,"d",d,"z",z,"+",delta,"n",n)
      if n >= limit:
        continue
      while n < limit:
        if not (s+1) in spokes and z > 1:
          spokes[s+1] = (d,z-1)
        dct[n] = dct.get(n,0) + 1
        n += delta
        d += 1
        z += 3

      s += 1

    tot = sum([1 for key,val in dct.items() if val == 1])

    return print ("tot",tot)

# jbum()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()
# ===== Thu, 13 Oct 2011, 22:19, BostonBear, USA
# I tried the algo on small amounts to find a pattern that would also me to chop down the time,
# it seemed like one was there but basically, brute force and way over the 1 min time lim.

def BostonBear():
    N = 5*10**7
    L = [0]*(N+1)
    summ = 0

    #primes = RofPrimes(2,N)

    for i in range(1,N+1):
      for j in range(int(i//3),N//2 + 1):

         n = (3 * j**2) + (2 * j*i) - (i**2)
         if n > 0:
            if n < N:  # and L[n]<4:  (falsely assumed that once an array slot value was high enough I could break out
               L[n] = L[n] + 1
            else:
               break

    for i in range(1, N+1):
       if L[i] == 1: summ +=1

    return print ("Answer is :", summ)

# BostonBear()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
print('\n--------------------------SOLUTION 8,  SLOW, 2 min  --------------------------')
t1  = time.time()

# ======  Mon, 6 Jun 2016, 04:03, azax1, USA
# It's not hard to work out that n satisfies this property iff n is a prime that is 3(mod4), OR nn is 4 or 16 times an odd prime.
# The vast majority of my code's runtime is due to sieving for so many primes.


def azax1() :
    count = 0
    limit = 5 * 10**7
    nums = [ i for i in range(limit)]
    for i in range(2, len(nums)):
        if nums[i] != i:
            continue

        if i % 4 == 3:
            count += 1
        if i < limit / 4:
            count += 1
            if i < limit / 16:
                count += 1

        m = i**2
        while m < len(nums):
            nums[m] = i
            m += i

    return print (count)

# azax1()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')