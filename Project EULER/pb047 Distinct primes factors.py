#!/usr/bin/python3
# Solved by Bogdan Trif @       Sun, 2 Oct 2016, 17:46
#The  Euler Project  https://projecteuler.net
'''
Distinct primes factors     -       Problem 47
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''
import time
t1  = time.time()

def detect_prime(n):
    i = n
    while(i <= n):
        j = 2
        while(j <= (i/j)):
            if not(i%j):
                return False
                break
            j = j + 1
        if (j > i/j) : return True
        i = i + 1

'''
def factor_split(nr_to_check):
    primes=[]
    n = nr_to_check
    i = 2
    while(i < n):
        j = 2
        while(j <= (i/j)):
            if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
            j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
        if (j > i/j) : primes.append(i)    #     print( i, end= ' ')     # If j > i/j means that the number is not already in the list, therefore must be another prime
        i = i + 1

    factors=[]
    for x in primes:
        while n % x == 0 :
            n = n / x
            factors.append(x)
    if len(factors) != 0:
        return factors #print('\nThe factors of ',nr_to_check ,'are : ' ,factors, end = '')
    #else : return False #print('    ',nr_to_check,' is prime   ')
'''
'''
def factor_split(n):
    nr_to_check = n
    factors=[]
    i, j = 2, 2
    while ( i<=n ) :
        while ( j < i/j ):
            if not (i%j) : break
            j +=1
        if (j > i/j) :
            if n % i == 0 :
                n = n / i           # Update n
                factors.append(i)
        if n % i != 0 :
            i += 1
    if len(factors) > 1:
        return factors                     # print('The factors of ',nr_to_check ,'are : ' ,factors, end = '')
    #else : print(nr_to_check,' is prime')
'''

def factor_split(a): ##outputs a list of the unique prime factors of its input
    b = 2
    d = []
    f = a
    while f > 1:
        while f % b != 0:
            b = b + 1
        d = d + [b]
        f = f / d[-1]
    if len(d) >1:
        return d
    #else: print(a,' is prime')



###################   END FUNCTIONS #########################


print('Test:   ',factor_split(1979),'\n')
test_list=factor_split(144)
test_list.count(2)

print('\n----------------------------MY SOLUTION-----------------------------')
FACTORS=[]
F8=[]


for i in range(134000  , 135100):
    F = factor_split(i)
    if ( F != None and len(F) >= 4)  :
        #print(i ,'  ',F)
        tt=[]
        for j in set(F):
            tt.append(j)
            tt.append(F.count(j))
            if len(tt) == 8 :
                  F8.append(tt)
                  if len(F8) >= 4 :
                         d = (F8[-4][0]**F8[-4][1]) * (F8[-4][2]**F8[-4][3]) * (F8[-4][4]**F8[3][5]) * (F8[-4][6]**F8[-4][7])
                         c = (F8[-3][0]**F8[-3][1]) * (F8[-3][2]**F8[-3][3]) * (F8[-3][4]**F8[-3][5]) * (F8[-3][6]**F8[-3][7])
                         b = (F8[-2][0]**F8[-2][1]) * (F8[-2][2]**F8[-2][3]) * (F8[-2][4]**F8[-2][5]) * (F8[-2][6]**F8[-2][7])
                         a = (F8[-1][0]**F8[-1][1]) * (F8[-1][2]**F8[-1][3]) * (F8[-1][4]**F8[-1][5]) * (F8[-1][6]**F8[-1][7])
                         #c = (F4[i-2][0]**F4[i-2][1]) * (F4[i-2][2]**F4[i-2][3]) * (F4[i-2][4]**F4[i-2][5]) #* (F4[i-3][6]**F4[i-3][7])
                         #b = (F4[i-1][0]**F4[i-1][1]) * (F4[i-1][2]**F4[i-1][3]) * (F4[i-1][4]**F4[i-1][5]) #* (F4[i-2][6]**F4[i-2][7])
                         #a = (F4[i][0]**F4[i][1]) * (F4[i][2]**F4[i][3]) * (F4[i][4]**F4[i][5]) #* (F4[i-1][6]**F4[i-1][7])
                         #print(len(F8), d, c, b, a)
                         if ( a-3 == b-2 == c-1  == d  ):
                            #if ( a-2 == b-1 == c  ):
                                print(d,'=',F8[-4],'  ;       ',c,'=',F8[-3],'  ;       ',b,'=' ,F8[-2]  ,'  ;       ',a,'=' ,F8[-1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's')

#####################################################
print('\n=============   OTHER SOLUTIONS FROM THE EULER FORUM   ===================')
print('------------------------    SOLUTION 1   --------------------------------')

t1  = time.time()

# distinct_primes_factors.py
# Find first occurrence of 4 consecutive integers
# such that all four have 4 distinct prime factors

# determine if exactly target number of prime factors
# if prime, add to prime list

def gen_prime_factors (num, prime_list):

    target_factors = 4
    factor_list = []
    factor_prod = 1

    for prime in prime_list:
        if num % prime == 0:
            index = 1
            test = num/prime
            while test % prime == 0:
                index += 1
                test = test / prime

            factor_prod *= (prime ** index)
            factor_list.append([prime, index])

        if factor_prod == num:
            if len (factor_list) == target_factors:
                return 1
            return 0
        if len (factor_list) == target_factors: # must be one more factor
            return 0

        if prime > (num ** 0.5):
            if len (factor_list) == 0: # num is prime
                prime_list.append (num)
                return 0
             # in this case, target minus one factor found,
             # must be exactly one more
            if len (factor_list) == (target_factors - 1):
                return 1
            return 0

prime_list = [2]
i = 3
consec_len = 0
consec_target = 4
while consec_len < consec_target:
    if gen_prime_factors (i, prime_list) == 1:
        consec_len += 1
    else:
        consec_len = 0
    i += 1

print (i - 4)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's')

print('\n------------------------    SOLUTION 2, SLOW,  thehunnybadge from Canada   --------------------------------')

t1  = time.time()

def is_prime(x):
    if x == 2:
        return True
    else:
        i = 2
        while i < int(x**0.5 +1):
            if x%i == 0:
                return False
                break
            else:
                i += 1
        else:
            return True

primes = []
for i in range(2, int(9999/2)):
    if is_prime(i) == True:
        primes.append(i)

def prime_divisors(num):
    prime_divisor_list = []
    for i in primes:
        if num%i == 0:
            if i != num/i:
                prime_divisor_list.append(i)
            else:
                prime_divisor_list.append(i)
    return prime_divisor_list

have_4_factors = False
num = 2*3*5*7 #product of first 4 consecutive primes
while have_4_factors == False:
    if len(prime_divisors(num)) == 4 and len(prime_divisors(num+1)) == 4 and len(prime_divisors(num+2)) == 4 and  len(prime_divisors(num+3)) == 4:
        print (num)
        have_4_factors = True
    else:
        num += 1

t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's')

print('\n------------------------    SOLUTION 3, INCREDIBLE, SafassThin from France   --------------------------------')
t1  = time.time()

def euler47(consecutives=4):
    """
    Using a factorisation generator.
    It creates a sort of on-going sieve to factorise numbers.
    """
    def factors():
        """
        Factorisation generator.
        (based on David Eppstein's prime number generator).
        """
        factors, n = {}, 2
        while True:
            if n not in factors:    # n is prime
                factors[n+n] = [n]  # start factorisation of n+n
                yield (n, [n])
            else:                   # n is composite
                for f in factors[n]:
                    factors.setdefault(f+n, []).append(f)
                yield (n, factors.pop(n))
            n += 1

    # Initialise loop
    found, f = 0, factors()

    while found < consecutives:
        n, fn = next(f)
        if len(fn) == consecutives:
            found += 1
        else:
            found = 0
    return n + 1 - consecutives

print(euler47())

t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's')


print('\n------------------------    SOLUTION 4, INCREDIBLE, THE FASTEST, mbh038 from England   --------------------------------')

t1  = time.time()

# very fast! based on Marcus Stuhr Tue, 26 Feb 2013, 16:27
def cp3(lim=200000,n=2):
    L=[0]*(lim+1)
    for i in range(2,int(lim/2+1)):
        if L[i]==0:
            for j in range(i,lim+1,i): L[j]+=1
    print (''.join(map(str,L)).find(''.join(str(n)*n)))

cp3(200000,4)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's')

print('\n------------------------    SOLUTION 5,  skasch  from France   --------------------------------')

t1  = time.time()

ps = [2,3,5]
from numpy import prod as prod
def nxtPrime(ps):

    n0 = ps[-1] + 2
    while any(n0 % p == 0 for p in ps if p*p <= n0):
        n0 += 2
    return ps + [n0]
n = 1
N = 4
r = 0
while r == 0:
    while ps[-1] < n // prod(ps[:N-1]):
        ps = nxtPrime(ps)
    if all(len([p for p in ps if (n+i) % p == 0]) == N for i in range(N)):
        r = n
    n+=1
print(r)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's')