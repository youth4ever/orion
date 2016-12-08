#!/usr/bin/python
import time
from math import  gcd
# The Most basic

# Prime numbers GENERATOR
print('---'*20,'PRIME NUMBERS GENERATOR - METHOD 1','---'*20)
t1  = time.time()

i = 2                              #Set the starting Prime, First Prime in the list, MAIN VARIABLE
END = 100                               #Set the END Prime, First Prime in the list, MAIN VARIABLE
while(i < END):                 # Set the last Prime Number - the Upper Limit
    j = 2
    while(j <= (i/j)):              # This condition checks in the lower list
        if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
        j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) : print( i, " is prime", end= ';   ')           # If j > i/j means that the number is not already in the list, therefore must be another prime
    i = i + 1
print ("Good bye!")
print('------'*25)

t2  = time.time()
print('\n',END ,' primes generated in :', round((t2-t1)*1000,4), 'ms\n')


print('---'*20,'PRIME NUMBERS GENERATOR - FAST & ELEGANT WAY','---'*20)
t1  = time.time()

def primes(n):
    from math import sqrt
    count = 3
    while count < n:
        isprime = True

        for x in range(2, int(sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break
        if isprime:
            print (count, end=' ')
        count += 1

primes(1000)

t2  = time.time()
print('\n' ,' primes generated in :', round((t2-t1)*1000,4), 'ms\n')


print('---'*20,'SIEVE of ERATOSTHENES :  Efficient PRIME GENERATOR algorithms','---'*20)
t1  = time.time()

def prime_generator(n):         # HIghly Efficient !!!!         THE FASTEST, The BEST , The ONE
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



def gen_primes(limit):                                  # THIRD
    ''' SIEVE of ERATOSTHENES :  Efficient PRIME GENERATOR algorithms       THIRD FASTEST
    Code by David Eppstein, UC Irvine, 28 Feb 2002,     http://code.activestate.com/recipes/117119/ '''
    D = {}
    i = 2
    while i <= limit:
        if i not in D:
            yield i
            D[i * i] = [i]
        else:
            for p in D[i]:
                D.setdefault(p + i, []).append(p)
            del D[i]
        i += 1

p = gen_primes(1000)
primus = [i for i in p]
print (primus)


t2  = time.time()
print('\n' ,' primes generated in :', round((t2-t1)*1000,4), 'ms\n')

t1  = time.time()

def sieve(lower, upper_bound):
    ''':Description:        SIEVE OF ERATOSTHENES ALGORITHM  , SECOND FASTEST
    :param:      :lower: = lower_integer including
                     :upper_bound: = upper integer excluding
    :returns:   a list containing all primes between lower and upper bound
    :Usage:             Example:    primes = sieve(2, 100)                    '''

    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag and i > lower ]
    return primes

print(sieve(11900, 12000))

t2  = time.time()
print('\n' ,' primes generated in :', round((t2-t1)*1000,4), 'ms\n')

###################################

print('\n---------------------------------DETECT PRIME --------------------------------')

print('\n---------------------- Fastest Method to check for a prime is gmpy2 Module --------------')
import gmpy2
# print('gmpy2 is prime Test ',gmpy2.is_prime( 18014398241046527))
print('gmpy2 is prime Test - THE FASTEST tested :  ',gmpy2.is_prime( 10000079 ) )


def isprime(n):
    ''' SLOWER METHOD. But Does not depend on a pre-generated sieve or on other module !'''
    if n == 1:
        return False
    for i in range(2, int((n**0.5)+1)):
        if not n % i:
            return False
    return True

# print(isprime(100000980001501))
print('isprime  Function Test:    ',isprime(10000079))


# primes = sieve(2,10000079)     # MUST BE Generated outside of the function for EFFICIENCY !
primes = sieve(2,1000)     # MUST BE Generated outside of the function for EFFICIENCY !
def is_prime(num):
    ''' Second Fastest DETECT PRIME BUT Dependent on the pre-generated sieve(lower, upper_bound).
        Is efficient ONLY if uses a list of pre-generated primes outside the function.
    :Usage:     If you work with BIG primes, ASSURE that you have build a list up to the square root of that prime,
                    otherwise will generate errors !
    :Example:   If you work with : 100000980001501 = [10000019, 10000079] assure you have the UP Sieve > 10000079 '''
    root = int((num)**0.5 + 1)
    for i in primes:
        if i > root:
            break
        if num % i == 0:
            return False
    return True

# print('is_prime function test :  ',is_prime(100000980001501))

#X = 19791979197911             # Type the  number you want to check
X = 1979
# X = 6597326399323993

if is_prime(X) == 1 : print(X ,' IS a Prime !')
else : print('is_prime Function test  :   ',X,' NOT a Prime ')

'''
def detect_prime(n):                # Function which checks if a number is prime
    # Function which checks if a number is prime
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

if detect_prime(X) == True : print(X ,' IS a Prime !')
else : print(X,' NOT a Prime ')
'''


t1  = time.time()



t2  = time.time()
print('\n','Completed in : ', round((t2-t1)*1000,4), 'ms')
######################################################

print('------'*20)
print('---'*20,'PRIME NUMBERS GENERATOR - using FOR LOOP, THE MOST BASIC - SLOW','---'*20)

for n in range(2, 16):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n // x, end = ';  ')
             break
     else:
         print(n, 'is a prime number', end = ';  ')

print('-----'*20,'\n')

#############################################

# Prime numbers GENERATOR Function
def primes_gen(i=81, END=100 ):
    '''  Prime numbers GENERATOR Function
    i - Sets the starting Prime, First Prime in the list, MAIN VARIABLE
    END - Sets the END Prime, First Prime in the list, MAIN VARIABLE
    '''
    while(i < END):                 # Set the last Prime Number - the Upper Limit
        j = 2
        while(j <= (i/j)):              # This condition checks in the lower list
            if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
            j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
        if (j > i/j) : print( i, end=' ')           # If j > i/j means that the number is not already in the list, therefore must be another prime
        i = i + 1
primes_gen(100,250)

##################################################################
print('\n\n','=='*20,'    PERFORMANCE TESTS    ','=='*20)
import time

CHECK_NR = 1000               # Here you put the test number for both for and while cases

print('--------FOR LOOP TEST---------')
t1  = time.time()
tmp1=[]
for n in range(2, CHECK_NR):
     for x in range(2, n):
         if n % x == 0:
             #print(n, 'equals', x, '*', n // x)
             break
     else:
            tmp1.append(n)
            #print(n, end=' ')

t2  = time.time()
print('\n',len(tmp1) ,' primes generated in :', round((t2-t1)*1000,4), 'ms')            #9592  primes generated in : 166006.495 ms

###################################################

print('\n','-----'*20)
print('\n--------WHILE LOOP TEST, FAR MORE EFFICIENT THAN FOR---------')
t1  = time.time()
tmp2=[]

i=2
while(i < CHECK_NR):                 # Set the last Prime Number - the Upper Limit
    j = 2
    while(j <= (i/j)):              # This condition checks in the lower list
        if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
        j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) :  tmp2.append(i)  #   print( i, end= ' ')        # If j > i/j means that the number is not already in the list, therefore must be another prime
    i = i + 1

t2  = time.time()
print('\n',len(tmp2) ,' primes generated in :', round((t2-t1)*1000,4), 'ms')    #9592  primes generated in : 2366.1354 ms

######################################

print('\n\n=============  FACTOR DECOMPOSITION  ===================')

def factors(a):
    '''Outputs a list of the unique prime factors of its input; The Second Fastest Algorithm
    This Function is splitting a number in its factors, and detects also if the number is a prime. '''
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

factors(int(''.join(('1', '8', '9', '9', '3', '4', '3'))))          # The factors of  999997 are :  [757, 1321], The factors of  428571 are :  [3, 3, 3, 3, 11, 13, 37]


print('-------------- Using module pyprimes , FASTEST FACTOR DECOMPOSITION ---------------------------')

def factorise(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

print(factorise(1979197919791979))
#print(list(i[0] for i in list(factorise(3932273))))


def factor(n):
    '''  Factor as a dictionary. Must test the speed ...'''
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
factor(32)


#####################################################

#   CMMDC - Cel Mai Mare Divizor Comun - The Greatest Common Divisor - GCD
print('\n------------   CMMDC - Cel Mai Mare Divizor Comun - The Greatest Common Divisor - GCD ------------------')

def cmmdc(a, b):        # GCD
    '''a, b: positive integers     , cmmdc, c.m.m.d.c., Cel Mai Mare Divizor Comun
    returns: a positive integer,  The Greatest Common Divisor of a & b.   '''
    testValue = min(a, b)
    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1
    return testValue

def cmmdc_rec(a, b):        #  GCD, CMMDC Recursive
    '''    a, b: positive integers     , cmmdc, c.m.m.d.c., Cel Mai Mare Divizor Comun
        returns: a positive integer,  The Greatest Common Divisor of a & b.    '''
    if b == 0:
       return a
    else:
       return cmmdc_rec(b, a % b)

def gcd(a, b):      # GCD
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


print('Test for the GCD cmmdc Function :\t',cmmdc(1445468, 300173))
print('Test for the GCD cmmdc_rec Function :\t',cmmdc(1445468, 300173))
print('Test for the GCD math.gcd Function :\t',cmmdc(1445468, 300173))
print('Test for the GCD gcd Custom Function :\t',cmmdc(1445468, 300173))
print(cmmdc_rec(1445, 3005))
factors(197)


print('\n------------   CMMMC - Cel Mai Mic Multiplu  Comun - The Lowest Common Multiple LCM ------------------')

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

print('LCM, Cel Mai Mic Multiplu  Comun Test :  \t',lcm(120, 121))

print('\n--------------------------------CIRCULAR PRIMES -----------------------------------')
############################################################################
# Function CIRCULAR PRIMES, Check if the CIRCULAR permutations of a number are primes

def circulate_number(A):
      tmp=[]
      for v in range(len(str(A))):
            a , i , s =  str(A), len(str(A)), ''
            for c in range(i):
                  #print(a[(v+c) % j] ,end='  ')
                  s += str(a[(v+c) % i])
            #return s
            tmp.append(int(s))
            #print(s)
            v+= 1
      return tmp #print(tmp)


def circular_primes(n):
    '''Function which checks if the permutations of a number are primes
    Depends on the Function detect_prime & circulate_number'''
    counter=0
    for x in circulate_number(n):
            if (is_prime(x) == 1 ):
                counter+=1
                print(x, end=' ')
    if (len(str(n)) == counter): return True    #   print('YES, all permutations are prime !')
    else:  return False                                 #print('NO, only',counter,' are primes')

print(circulate_number(1234))
print(circular_primes(197))
###################################################

print('\n---------------------------- DIVISORS --------------------------------')

class GET_DIVISORS(object):
    '''Made by Bogdan Trif @ 2016-11-15, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)

    :param nr:  int
    :return: a list with the factors ( method factorise) or divisors (method divisors)
    :Usage:  >>> GET_DIVISORS().divisors(90)    # to obtain the divisors
                 >>>  GET_DIVISORS().factorise(90)   # to obtain the factors                      '''
#     def __init__(self, nr):   # We don't want to initialize the class with a number
#     self.nr = nr

    def factorise(self, nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(nr)] for val in sublist]

    def divisors(self, nr):
        ''':Description: Use the itertools, functools, operator, gmpy2 modules.
        In the case of multiple calls take the module imports outside the class and load only once => improved speed. '''
        from itertools import combinations
        import functools, operator, gmpy2
        if gmpy2.is_prime(nr) == True or nr == 1 :
            return [1]    # Must be adjusted to [1] if you change on list
        else :
            all_factors =  self.factorise(nr)
            # set_factors=list(set(all_factors))
            comb= set()
            # print(all_factors)
            for i in range(1, len(all_factors)):
                c = set(combinations(all_factors, i) )
                comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
                comb_prod.sort()
        return  comb_prod[::-1]   # sum([1]+ comb_prod)   !!! Remember to change on  return [1]  for isprime case !


print('Here we test the GET_DIVISORS CLASS :  ',GET_DIVISORS().divisors(90))