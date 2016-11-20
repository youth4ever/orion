#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on  Mon, 10 Oct 2016, 19:50
#The  Euler Project  https://projecteuler.net
'''
Spiral primes       -       Problem 58
Starting with 1 and spiralling anticlockwise in the following way, a
square spiral with side length 7 is formed.

                           37 36 35 34 33  32  31
                           38 17 16 15 14  13  30
                           39 18  5  4   3   12  29
                           40 19  6  1   2   11  28
                           41 20  7  8   9   10  27
                           42 21 22 23 24 25  26
                           43 44 45 46 47 48  49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
'''
import time

def is_prime(n):
    # Function which checks if a number is prime
    for i in range(2, int(pow(n,1.0/2))+1):
        if n%i==0:
            return 0
    return 1

print('\n------------------  MY SOLUTION ALGORITHM  ---------------------------\n')
t1  = time.time()

DIAGS = [1]
primes, percent =0, 1
L, i = 1 ,0
All = 1

while percent > 0.1 :
    i += 1
    for j in range(1,5):
        L  += 2 * i
        DIAGS.append(L)
        #print(L, end='  ')
        if is_prime(L) == 1:
            primes += 1
            #print('Prime: ',L, 'Total : ', primes)
    All += 4                        # Here we increment with the numbers analyzed from both diagonals
    #print(All)
    #print('\n',primes ,'/' , len(DIAGS), DIAGS)
    #percent = primes / (len(DIAGS))
    percent = primes / All
    #print(str(i)+'.     -->',percent, '         ', primes ,'/' , len(DIAGS), (len(DIAGS)-1)/2 )
    #print(str(i)+'.     -->',percent, '         ', primes ,'/' , All, (All)/2 )


print('\n\n', len(DIAGS) ,DIAGS[0:100])
print('\n','Square Dim :  ' , (len(DIAGS)+1)/2)                 # The Answer is : 26241
print('\n','Square Dim :  ' , (All + 1)/2)                 # The Answer is : 26241

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms\n')

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 , markus.obi, Germany --------------------------')

t1  = time.time()

import itertools, math

def sieve(upper_bound):
    # sieve of Eratosthenes
    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag]
    return primes

def is_prime(n, primes):
    sq = math.sqrt(n)
    for prime in primes:
        if prime > sq:
            break
        if n % prime == 0:
            return False
    return n > 1

def solve():
    prime_counter = 0
    primes = [2] # must be non-empty
    for i in itertools.count():
        if i == 0:
            continue
        l = 1 + i * 2
        sq = l * l
        step = l - 1
        if primes[-1] < l:
            primes = sieve(l*2)
        prime_counter += sum(1 for diagonal in range(sq - step, sq - 4 * step, -step) if is_prime(diagonal, primes))
        checked = 4 * i + 1
        if float(prime_counter) / checked < 0.1:
            print(l)
            return

def main():
    import time
    start = time.time()
    solve()
    end = time.time()
    elapsed = end - start
    print("elapsed: {:.1f} ms".format(elapsed * 1000))

main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms\n')                       #Completed in : 4.50 s



print('\n--------------------------SOLUTION 2 , mathman, Sweden --------------------------')

t1  = time.time()

def is_prime(n):
    # Function which checks if a number is prime
    for i in range(2, int(pow(n,1.0/2))+1):
        if n%i==0:
            return 0
    return 1

i = 1
inc = 2
prime_count = 0
total_count = 1

while i == 1 or (float(prime_count) / total_count) >= 0.4:

    i += inc
    if is_prime(i):
        prime_count += 1
    i += inc
    if is_prime(i):
        prime_count += 1
    i += inc
    if is_prime(i):
        prime_count += 1
    i += inc

    total_count += 4
    inc += 2

print (inc - 1)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms\n')

print('\n--------------------------SOLUTION 3 , THE FASTEST ,  Francky, France --------------------------')

t1  = time.time()

def PE058(percent= 10, lim = 27000):
  u = [n*n+1 for n in range(lim)]
  v = [n*n-n+1 for n in range(lim)]
  for n in range(3, lim, 2): u[n]//=2

  n0 = 2
  while n0<lim:
    p = u[n0]
    ini = p+n0
    if p!=1 and ini<lim:
      for n in range(ini, lim, p):
        while not(u[n]%p): u[n]//=p
    p = v[n0]
    ini = p+n0
    if p!=1 and ini<lim:
      for n in range(ini, lim, p):
        while not(v[n]%p): v[n]//=p
    n0+=1

  # =========  TESTS ======
  #for k, a in enumerate(v):
    #if k>1:
      #assert (a==1+k*k-k)==bool(is_prime(1+k*k-k)), (k, a)
  #for k, a in enumerate(u):
    #if k>1 and k&1:
      #assert (a==1+k*k)==bool(is_prime(1+k*k)), (k, a)
  # =======================

  a = 1
  aa = -4
  b = 1
  bb = 0
  cpt = 0
  tot = 1
  k = 0
  try:
    while 1:
      k+=1
      aa+=8
      a+=aa
      if a==u[2*k]: cpt+=1
      bb+=2
      b+=bb
      if b==v[2*k]: cpt+=1
      bb+=2
      b+=bb
      if b==v[2*k+1]: cpt+=1
      tot+=4
      if 100*cpt<percent*tot: return 2*k+1
  except:
    return "WRONG assumption, lim is too low"

print(PE058())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms\n')


print('\n--------------------------SOLUTION 3 ,  FAST ,  richwsas, USA --------------------------')

t1  = time.time()


def is_composite(a,d,r,n):
    x = pow(a,d,n)
    if x==1:
        return False
    for i in range(r):
        if pow(a,2**i*d,n)==n-1:
            return False
    return True

def miller_rabin(n):
    #per wikipedia, these witnesses are good for n < ~2.1T
    small_number_witnesses = [2,3,5,7,11]
    if n%2==0:
        return False
    d = n-1
    r = 0
    while d%2==0:
        d /= 2
        r += 1

    for a in small_number_witnesses:
        if is_composite(a,int(d),r,n):
            return False

    return True

primes_on_diagonal = 3
numbers_on_diagonal = 5

ratio = primes_on_diagonal/float(numbers_on_diagonal)

i = 5
while ratio >= 0.1:
    inc = i-1
    numbers_on_diagonal +=4
    for j in range(1,4):
        if miller_rabin(i**2-inc*j):
            primes_on_diagonal+=1
    ratio = primes_on_diagonal/float(numbers_on_diagonal)
    i += 2

#checks ratio at the beginning of the loop, so we went 2 too far
print(i-2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms\n')