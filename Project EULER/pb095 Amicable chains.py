#!/usr/bin/python3
# Solved by Bogdan Trif @       Completed on Thu, 10 Nov 2016, 14:34
#The  Euler Project  https://projecteuler.net
'''
                    Amicable chains     -       Problem 95

The proper divisors of a number are all the divisors excluding the number itself.
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14.
As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220,
forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains.
For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
'''
import  time
from itertools import combinations
import functools
import itertools
import operator



def factor_pyprimes(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def factor_split(a):
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
        return d
    #else: print(a,' is prime')

def isprime(n):
    ''' VERY FAST. Does not depend on a pre-generated sieve or on other module !'''
    if n == 1:
        return False
    for i in range(2, int((n**0.5)+1)):
        if not n % i:
            return False
    return True

def prime_generator(n):
    """  Sieve of Eratosthenes
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


print('\n---------------------TESTS-------------------')
print('Factor decomposition pyprimes : ',factor_pyprimes(32))

print(factor_split(28))

nrt=970200
factori = factor_split(nrt)
# print(factori)
comb_test=set()
for i in range(1, len(factori)):
    c = set(combinations(factori, i) )
    comb_test.update(c)
    print(c)
print('---------------')
comb_test_prod = list(functools.reduce(operator.mul, i) for i in comb_test)
print(comb_test_prod)
comb_test_prod.sort()
print(comb_test_prod)
print('===================================\n')

# pydiv=[i for i in factorise(nr)]
# print(pydiv)
# pydiv = sorted([val for sublist in pydiv for val in sublist])
# print('Pyprimes factorise : ', pydiv )
# C = list(combinations(list(set(divisors)), 2));        print(C)
# print ('\nUsing LIST COMPREHENSION count all elements : ',  [[x, factors.count(x)] for x in set(factors)]  )
# lst = [[x, factors.count(x)] for x in set(factors)]

def get_divisors(nr):
    '''Made by Bogdan Trif @ 2016-11-09, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)
    2-4 times slower because of the factorize method. Must improve it
    :param nr:  int
    :return: a list with the divisors

    '''
    if isprime(nr) == True or nr == 1 :
        return 1    # Must be adjusted to [1] if you change on list
    else :
        all_factors = factor_pyprimes(nr)
        # set_factors=list(set(all_factors))
        comb= set()
        # print(all_factors)

        for i in range(1, len(all_factors)):
            c = set(combinations(all_factors, i) )
            comb.update(c)
            comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
            comb_prod.sort()
        return  sum([1]+ comb_prod) # !!!!!!!! Remember to change on  return [1]  for isprime case

t1  = time.time()

print('\n-------------- Some other Tests -------------------')
print(factor_pyprimes(4))

print('\nDivisors sum: ', get_divisors(276) )
# print('\nDivisors sum: ', '\n', get_divisors(396) )
# print('\nDivisors sum: ', '\n', get_divisors(696) )
# print('\nDivisors sum: ', '\n', get_divisors(1104) )
# print('\nDivisors sum: ', '\n', get_divisors(1872) )
# print('\nDivisors sum: ', '\n', get_divisors(3770) )
# print('\nDivisors sum: ', '\n', get_divisors(3790) )
# print('\nDivisors sum: ', '\n', get_divisors(3050) )
# print('\nDivisors sum: ', '\n', get_divisors(2716) )
# print('\nDivisors sum: ', '\n', get_divisors(2772) )
# print('\nDivisors sum: ', '\n', get_divisors(465780) )
print('\nDivisors sum: ',  get_divisors(48208) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')


print('\n==========  My  FIRST SOLUTION,  SLOW  ===============\n')
t1  = time.time()

# up_range = 10**6

def Build_dictionary(up_range):
    global Div_sums
    Div_sums={}
    iter=0
    for i in range(1, up_range+1):       # Don't put low range >1 , because dictionary must have also the 1 key
        iter+=1
        if iter % 1e5 == 0 : print(iter)
        if isprime(i): Div_sums[i] = 1
        else:
            v = get_divisors(i)
            Div_sums[i] = v
        # print(i, v)
    return Div_sums

# test_dict = Build_dictionary(10**4)
# print('Test for Build_dictionary : ',test_dict[220],'\n')
# Div_sums = Build_dictionary(up_range)       # This must be arranged somehow !!!!!!

global memo
memo={}     # Must be global

def chain_factor(n):
    chain=[]
    if isprime(n) == True :         #START pre-loop checks
        memo[n] = 1             # We use a memorator dictionary to keep track of the already investigated numbers
        return (1, [n])                 # In this way we just drop the terms

    else :
        s = Div_sums[n]                    #get_divisors(n)   Div_sums[n]
        if s > int(up_range) :
            return (1, [n])
        elif s in memo:                 # case 25 --> 1+5 = 6 --> 1+2+3=6
            return (1, [n , s])
        elif n == s :
            memo[s] = s        # Here we want to exclude the numbers for which divisors sum = number itself
            return (1, [n, s] )
        elif isprime(s) == True :       # Second Prime Drop
            memo[s] = s
            return(1, [n, s, 1])            #END pre-loop checks
        # elif (n not in memo) and (s not in memo ):

        elif (n not in memo) or (s not in memo ):       # The main loop starts
            chain.extend([n,s])
            while s not in memo :
                s = Div_sums[s]                #Div_sums[s]         # THE MAIN LINE FROM THE WHILE LOOP

                if isprime(s) == True:      # No more stress with the primes
                    memo[n] = s
                    return(1, [n, 1])
                if s > up_range:            # Drop the chains which are bigger than up_range
                    memo[s] = s
                    return (1, [n , s ])
                if s in chain:          # Repeating pattern
                    memo[chain[0]] = chain[0]
                    chain.append(s)
                    if chain[0] == chain[-1]:           # Returns the AMICABLE CHAIN when first == last
                        return ( len(chain)-1, chain )
                    else:   return (1, chain)           # Drops the chain when the repeating numbers are part
                elif s < up_range  :                    # of another sequence
                    chain.append(s)
                # print(chain)
    return (1, chain)


# memo={}
# for i in range(1,10000):
#     print(i, chain_factor(i), memo)

print('\n-------------- Some other Tests -------------------')
# print('Chain test for :',chain_factor(12496))
# print('Chain test for :',chain_factor(13) )
# print('Chain test for :',chain_factor(73) )
# print('Chain test for :',chain_factor(6))
# print('Chain test for :',chain_factor(28))
# print('Chain test for :',chain_factor(9))
# print('Chain test for :',chain_factor(32))
# print('Chain test for :',chain_factor(4))
# print('Chain test for :',chain_factor(210))
# print('Chain test for :',chain_factor(220))
# print('Chain test for :',chain_factor(24))
# print('Chain test for :',chain_factor(25))
# print('Chain test for :',chain_factor(95))
# print('Chain test for :',chain_factor(16))
# print('Chain test for :',chain_factor(220))
# print('Chain test for :',chain_factor(276))
# print('Chain test for :',chain_factor(562))
# print('Chain test for :',chain_factor(1064))
# print('Chain test for :',chain_factor(5916))
# print('Chain test for :',chain_factor(48206))
# print('Chain test for :',chain_factor(48207))
# print('Chain test for :',chain_factor(48208))
# print('Chain test for :',chain_factor(14316))
# print(memo)

print('\n-------------')


def solve():
    global Div_sums, memo, up_range
    up_range = 10**6
    Div_sums = Build_dictionary(up_range)
    max_length, cnt, longest =0, 0, []
    memo={}                 # The dictionary MUST STAY OUTSIDE THE LOOP !!!
    for i in range(1, up_range):
        K = chain_factor(i)
        length = K[0]
        # print(K[0], K[1])
        cnt+=1
        if cnt % 1e5 == 0 : print(cnt)
        if K[0] != 1 and max_length < length :
            max_length = length
            longest = K
            print(K)
    print('Answer:  ',min(longest[1]),'      ', longest )                           #Answer :  14316

solve()         # Uncomment to execute the Code

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's')            # Completed in : 239.70171 s


# Vezi ca trebuie sa te asiguri ca seria chain se termina cu amicable, acelasi numar adica
# numai acelea trebuie considerate !!!!!!!!!!!!!! Atata mai ai facut !!!!!!
# 65 402170 --> ma indoiesc ca e amicabil !!!










print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, FAST,  Haroun , Algeria--------------------------')
# Took 10secs on Python 2.7 (7 seconds for creating the table of sum of divisors and three for the actual search) and only one second on Pypy.
# I stored all the tested numbers in a set to not recalculate them.
t1  = time.time()

def thesolution():
    L=10**6+1;
    sd=[0]*L;
    for i in range(1,L):
        for j in range(2*i,L,i):
            sd[j]+=i ;
    tested=set() ; max=0;
    for n in range(L):
        if n in tested :
            continue;
        m=sd[n] ; l=[n];
        while m<=L and m not in l and m>1:
            if m in tested :
                break;
            l.append(m);
            m=sd[m];
        for x in l :
            tested.add(x);
        if m in l :
            k=1;i=len(l)-1;
            while l[i]!=m:
                i-=1;
                k+=1;
            if k>max :
                max,sol=k,m
    print ("the number %d gives a cycle of length %d" % (sol,max))

# thesolution()                     # Uncomment to execute

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 6802.389145 ms


print('\n--------------------------SOLUTION 2, BRUTE FORCE, anumoshsad, Bangladesh --------------------------')
t1  = time.time()
# Brute forced it within 12 secs by calculating all chains under one million. Used a sieve for calculating sum of divisors.

def pe95():
    div = [1]*1000001
    for i in range(2,1000001):
        for j in range(2*i,1000001,i):
            div[j]+=i

    def f(n):
        x=n
        he=[x]
        while True:
            x=div[x]
            if x>1000000:
                return 0
            if x in he:
                if x == he[0]: return len(he)
                else: return 0
            he.append(x)
    result = 0

    for i in range(2,1000001):
        if f(i)>result: result = i

    print(result)

# pe95()              #Uncomment to execute

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, alex111, Netherlands --------------------------')
t1  = time.time()
# Not to many recursive solutions... This one runs in about 2s on an old dualcore:
from sympy import *

def propdiv(n):
    lst = list(divisors(n, generator=True))
    lst.remove(n)
    return lst

def findchain(r,n):
    s = sum(propdiv(n))

    if s == 1 or s == n or s > 1000000:
        return []
    elif s == r[0]:
        return r
    elif s in r:
        return []
    else:
        r.append(s)
        return findchain(r,s)

def main():
    sol = [0,0]
    for n in range(2,20000):
        l = findchain([n],n)
        sz = len(l)
        if sz > 0:
            if sz > sol[1]:
                sol[0]=n; sol[1]=sz
            print ("   Amicable for:", n, "(", sz,"):",)
            for e in l:
                print (e,end=' ')
            print
    print (sol)

# main()                                       # Uncoment to execute

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, utkarsh_23, India --------------------------')
t1  = time.time()

def utkarsh_23():
        lim = 1000000
        div = [0] * lim
        for i in range(1,lim):
            for j in range(2 * i, lim, i):
                div[j] += i
        def chain(a):
            summ = 0
            no = a
            count = 0
            L = []
            while True:
                count += 1
                summ = div[no]
                if summ > 1000000 or summ in L:
                    return 0
                elif summ == a:
                    return count
                no = summ
                L.append(summ)
        def find(b):
            summ = 0
            no = b
            L = [b]
            while True:
                summ = div[no]
                if summ == b:
                    return min(L)
                no = summ
                L.append(summ)
        greatest = 0
        nn = 0
        for q in range(2,1000000):
            if chain(q) > greatest:
                greatest = chain(q)
                nn = q
        print (find(nn))

utkarsh_23()        # Uncomment to execute

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')             #  Completed in : 20034.145832 ms

# print('\n--------------------------SOLUTION 5,  --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 6,  --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


