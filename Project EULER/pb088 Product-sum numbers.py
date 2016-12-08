#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Sat, 3 Dec 2016, 19:28
#The  Euler Project  https://projecteuler.net
'''
                                Product-sum numbers     -       Problem 88

A natural number, N, that can be written as the sum and product of a given
set of at least two natural numbers, {a[1], a[2], ... , a[k]} is called a product-sum number:
N = a[1] + a[2] + ... + a[k] = a[1] * a[2] * ... *a[k].

For example, 6 = 1 + 2 + 3 = 1 * 2 * 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

                    k=2:    4 = 2 * 2 = 2 + 2
                    k=3:    6 = 1 * 2 * 3 = 1 + 2 + 3
                    k=4:    8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
                    k=5:    8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
                    k=6:    12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12= 30;
note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12  is  {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2k12000?
'''
import time
import gmpy2
import pyprimes
from itertools import combinations, permutations
import functools, operator
import math

################# FUNCTIONS #####################


class GET_DIVISORS(object):
    '''Made by Bogdan Trif @ 2016-11-15, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)

    :param nr:  int
    :return: a list with the divisors    '''

#     def __init__(self, nr):   # We don't want to initialize the class with a number
#     self.nr = nr

    def factor_pyprimes(self, nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(nr)] for val in sublist]

    def divisors(self, nr):
        from itertools import combinations
        import functools, operator, gmpy2
        if gmpy2.is_prime(nr) == True or nr == 1 :
            return [1]    # Must be adjusted to [1] if you change on list
        else :
            all_factors =  self.factor_pyprimes(nr)
            # set_factors=list(set(all_factors))
            comb= set()
            # print(all_factors)
            for i in range(1, len(all_factors)):
                c = set(combinations(all_factors, i) )
                comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
                comb_prod.sort()
        return  comb_prod[::-1]   # sum([1]+ comb_prod)   !!!!!!!! Remember to change on  return [1]  for isprime case


print('\nUsing the method divisors from within the class GET_DIVISORS : ', GET_DIVISORS().divisors(90) )
print('Using the method factor_pyprimes from within the class  GET_DIVISORS: ', GET_DIVISORS().factor_pyprimes(90)  )


def product_sum_k(n):       # It is not used in the current code. I just left it here
    ''':Description: Function which finds the **k**'s of a sum-product number
    :Example1:  product_sum_k(15)    returns [9] because :

        :k=9: :  3*5*1*1*1*1*1*1*1  = 3+5+1+1+1+1+1+1+1 = 15
    :Example2:  product_sum_k(16)    returns [8,10] because :

        :k=8: :  2*8*1*1*1*1*1*1  = 2+8+1+1+1+1+1+1 = 16
        :k=10: :  4*4*1*1*1*1*1*1*1*1  = 4+4+1+1+1+1+1+1+1+1 = 16
    :param: :n:   *int*, number for which *k* is calculated
    :return:    *list* containing all the **k**'s that a number n can have
    '''
    div = GET_DIVISORS().divisors(n)
    F = GET_DIVISORS().factor_pyprimes(n)
    p =  functools.reduce(operator.mul, F)    # Taking all terms
    ks = [ p-sum(F) + len(F) ]
    # p = list( functools.reduce(operator.mul, i) for i in div)   # Taking all terms
    for i in range( len(div)//2+1 ) :
        a = n/div[i]
        # print('a=',a, end='    ')
        o = a* div[i] - (a+div[i])
        # print('o=',o)
        # if int(o+2) not in ks : ks.append( int(o+2) )
        ks.append( int(o+2) )

    def inner_terms(n):
        kin=[]
        F = GET_DIVISORS().factor_pyprimes(n)
        comb=set()              # This CODE WORKS for inner cases : Ex 90 : 6 + 3 +5  ,  9 + 2+5, 10 + 3 +3
        if len(F) > 3 :
            for i in range(2, len(F)-1):
                    C = set(combinations(F, i) )
                    comb.update(C)
                    # print(comb)
                    # C_sum = list( functools.reduce(operator.add, i) for i in comb)
                    C_prod = list( functools.reduce(operator.mul, i) for i in comb)
            # print('\n',comb)
            # print('C_sum : ',C_sum)
            # print('C_prod : ',C_prod)
            comb = list(comb)
            for j in range(len(C_prod)):
                A = F.copy()
                # p1 = C_prod[j]
                # p2 = n/C_prod[j]
                for m in comb[j]: A.remove(m)
                # print(A)
                s1 = C_prod[j]
                s2 = sum(A)
                o1 = n - (s1+s2 ) + len(A) +1
                kin.append(o1)
                # print('p1=', p1 ,  '   p2=', p2,'     s1=',s1 , '    s2=',s2, '   ', o1, '  ' ,list(comb)[j] )
            return list(set(kin))
        else : return []
    kin = inner_terms(n)
    return len(list(set(ks+kin))) , sorted(list(set(ks+kin)))           # this is the returned k


def partitions(n):
    '''     Taken from http://code.activestate.com/recipes/218332-generator-for-integer-partitions/
            Created by David Eppstein on Wed, 27 Aug 2003
    :What it is:    A generator of number partition
    :Usage:     Example:    for i in partitions(5):    print(i)
    :param n:   the number you want the partitions
    :return:    set of lists with all the possible combinations                                                 '''
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return
    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]

def single_factoring(lst_divisors) :
    D=[]
    for I in partitions(len(lst_divisors)):
        if len(I) > 1 :
            # print(I , end='    ' )
            first, last = 0, 0
            tmp=[]
            for a in I :
                last += a
                G = lst_divisors[first:last]
                H = functools.reduce( operator.mul ,G)
                # print(G, H , end=' ;  ' )
                first = last
                tmp.append(H)
            # print()
            D.append(tmp)
    return D

def multi_factoring(lst_divisors) :
    F = lst_divisors
    D=[]
    for I in partitions(len(F)):
        if len(I) > 1 :
            P = list(unique_permutations(F))
            for b in range(len(P)):
                first, last = 0, 0
                tmp=[]
                for a in I :
                    last += a
                    G = P[b][first : last]
                    H = functools.reduce( operator.mul ,G)
    #                 print(G, H , end=' ;  ' )
                    first = last
                    tmp.append(H)
                D.append(tuple(tmp))
    return D

def unique_permutations(lst):       # The master Function
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
    :param lst: type list
    :return:    a list of lists containing all the permutations
    '''
    if len(lst) == 1:
        yield (lst[0],)
    else:
        unique_lst = set(lst)
        for first_element in unique_lst:
            remaining_lst = list(lst)
            remaining_lst.remove(first_element)
            for sub_permutation in unique_permutations(remaining_lst):
                yield (first_element,) + sub_permutation


class GET_ALL_KEYS(object) :

    def factorize_all(self, n):
        F = GET_DIVISORS().factor_pyprimes(n)
        # print(F)

        if len(set(F)) == 1 :
            ALL=[]
            for I in partitions(len(F)):
                if len(I) > 1 :
                    first, last = 0, 0
                    tmp=[]
                    for a in I :
                        last += a
                        G = F[first:last]
                        H = functools.reduce( operator.mul ,G)
                        first = last
                        tmp.append(H)
                    ALL.append(tuple(tmp))

        elif len(set(F)) > 1 :
            ALL=[]
            for I in partitions(len(F)):
                if len(I) > 1 :
                    P = list(unique_permutations(F))
                    for b in range(len(P)):
                        first, last = 0, 0
                        tmp=[]
                        for a in I :
                            last += a
                            G = P[b][first:last]
                            H = functools.reduce( operator.mul ,G)
            #                 print(G, H , end=' ;  ' )
                            first = last
                            tmp.append(H)
                        ALL.append(tuple(tmp))

        return ALL

    def compute_keys(self, n) :
        KEYS = []
        ALL = self.factorize_all(n)
        for i in range(len(ALL)):
            suma =  functools.reduce(operator.add, ALL[i] )
            k = n - suma + len(ALL[i])
            # print(suma, '       ', len(ALL[i]) ,ALL[i] , '      ' ,k)
            KEYS.append(k)
        KEYS = sorted(list(set(KEYS)))
        return KEYS

############### END FUNCTIONS ####################

print('\n------------------------ TESTS---------------------------')

F = GET_DIVISORS().factor_pyprimes(6144)

# n=8100   # 10500


# ALL = FACTORIZE_ALL(n=8100)
#
# print('\n\nALL List containing all the possible factorizations : \n', len(ALL), ALL)


# print('\n\ncompute_keys Function Test : ',compute_keys(n=8100))

# print('--------------  CHECK  ----------------')
# C_sum = list( functools.reduce(operator.mul, i) for i in Comb)

# for i in range(len(ALL)) :
#     prod =  functools.reduce(operator.mul, ALL[i] )
#     print(prod, end='  ')

print('\n------------- TESTING THE CLASS -------------')

print('Class Test Method factorize_all : ', GET_ALL_KEYS().factorize_all(4608) )
print('Class Test Method compute_keys: ', GET_ALL_KEYS().compute_keys(4608) )

print('Class Test Method factorize_all : ', GET_ALL_KEYS().factorize_all(6144) )
print('Class Test Method compute_keys: ', GET_ALL_KEYS().compute_keys(6144) )


print('\n\n--------------------- BENCHMARK TEST --------------------')
t1  = time.time()

print('Class Test Method compute_keys: ', GET_ALL_KEYS().compute_keys(8192) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\nproduct_sum_k  Function Test :    \n',product_sum_k(420))

print('Class Test Method compute_keys: ', GET_ALL_KEYS().compute_keys(30) )
print('Class Test Method factorize_all: ', GET_ALL_KEYS().factorize_all(30) )

print('\n----------------------')

print('\nTesting the single_factoring Function : ', single_factoring([2,2,2,2,2,2,2,2,2,2,2,2,2]))
print('Class Test Method factorize_all : ', GET_DIVISORS().divisors(512) )
print('\nTesting the multi_factoring Function : ', len(list(set(multi_factoring([2,2,2,2,2,2,2,2,2,2,3,3,3])))) ,len(multi_factoring([2,2,2,2,2,2,2,2,2,2,3,3,3])), multi_factoring([2,2,2,2,2,2,2,2,2,2,3,3,3])  )


print('\n================  My FIRST SOLUTION, SLOW, 30 sec  ===============\n')
t1  = time.time()

def pb_088(up_range):
    BIG_K={}
    for i in range(4, up_range+250):
        if gmpy2.is_prime(i) == False :
            p_s = GET_ALL_KEYS().compute_keys(i)
            # print( 'P-S: ', i, '       key: ', p_s )
            for k in p_s :
                if k not in BIG_K and k <=12000 :   #12000
                    BIG_K[k] = i

    return BIG_K

# BIG_K  = pb_088(up_range = 12000 )
# BIG_K = dict(zip(BIG_K.values(), BIG_K.keys()))     # Reverse the dictionary keys <=> values
# # print('\nThe BIG_K Dictionary ', len(BIG_K) ,   BIG_K )
# print('\nThe Set of P-S obtained : ', sorted(list(set([ v for v in BIG_K.values() ] ) )),'\n')
#
# print('\nAnswer:  ', sum(set([ v for v in BIG_K.keys() ] ) ),'\n')      #     Answer:   7587457


#        LOG
# 2016-11-16, 18:00 # One day full worked, not succeeded. TO DO: Must identify the problem of :
# product_sum_k(63) and many others. It does not add to P-S 63 the correct value 41 which is the minimum. There are
# two keys k=49 : 63 & k=53 : 63 but not 41. k=41 corresponds to a different P-S k=41:48.
# Actually P-S 63 should not exist because the lowest key k=41 has already a value associated P-S 48. THIS IS THE PROBLEM !!!!
# 2016-11-19, 14:00 --> Still no success !
# Tried : 18175719 , 7629544, 7587457

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')


# IMPORTANT OBSERVATION : Fri, 16 May 2014, 09:59
# This one took me a whole night to figure out.
# I should have generated numbers from combinations of factors rather than factorising each number from 4 to 12200.
# Runs pretty slow though ~10s.


print('\n--------------------------SOLUTION 1,   THE SIMPLEST , VERY VERY FAST --------------------------')
t1  = time.time()

def recurse(p, s, n, start):
    k = n + p - s                   # HERE IS THE KEY OF THE PROBLEM
    if k > kmax: return
    if p < N[k]: N[k] = p
    for x in range(start, 2*kmax//p+1):
        recurse(p*x, s+x, n+1, x)

kmax = 12000
N = [3*kmax] * (kmax+1)
recurse(1, 0, 0, 2)
print (sum(set(N[2:])))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 2470.141411 ms



print('\n--------------------------SOLUTION 2,   FAST, tolstopuz, Russia --------------------------')
t1  = time.time()

import functools, operator

def it1(a, mx):
    yield a
    p = functools.reduce(operator.mul, a, 1)
    for i in range(a[-1], mx // p):
        for t in it1(a + [i], mx):
            yield t

def it(mx):
    for a in range(2, mx):
        for t in it1([a], mx):
            yield t

nmax = 12000

x = (nmax + 1) * [10**12]

for r in it(2 * nmax):
        p = functools.reduce(operator.mul, r, 1)
        a = p - sum(r) + len(r)
        if a <= nmax and p < x[a]:
            x[a] = p

print(sum(set(x[2:])))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 2470.141411 ms

print('\n--------------------------SOLUTION 3, BEST, VERY SMART & EFFICIENT, THE FASTEST, cantdance, Poland   --------------------------')
t1  = time.time()
print('I must analyze this !!!')

#
# I'm maintaining an array s of sets, where s[n] contains all possible values of f_1 * ... * f_k - k over factorizations of n.
#  Now if s[n] contains i, then n is a product-sum with k=n-i.
#
# The array s can be computed by DP. s[n] always contains n-1, which corresponds to the single factor decomposition.
# Now consider any decomposition into at least 2 factors and let d <= sqrt(n) be the smallest one.
# This kind of decomposition adds to s[n] the numbers  d+s[n/d]-1.
# And that is exactly what I am doing.
#
# The code below takes 1s to find the answer for N=12000

N = 12000
s = [ set([]) for i in range(2*N+1)]
sol = (N+1)*[0]
count = 0
n = 1
while count < N:
	s[n].add(n-1)
	d = 2
	while d*d <= n:
		if n % d==0:
			for snd in s[n//d]:
				s[n].add(d+snd-1)
		d = d+1
	for i in s[n]:
		if n-i >= 0 and n-i <= N:
			if sol[n-i] == 0:
				sol[n-i] = n
				count = count + 1
			elif sol[n-i] > n:
				sol[n-i] = n
	n = n+1
print (sum(set(sol[2:])))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 1172.067165 ms



print('\n--------------------------SOLUTION 4, WOW !!!  Slaunger, Denmark  --------------------------')
t1  = time.time()

# I was intrigued when I saw the dynamic programming approach shown by cantdance, which is also quite efficient (750 ms on my laptop).
# I have optimized it such that it runs on one third of that time (250 ms).
#
# To do that I have implemented an "anti-prime" sieve method for finding lists of all divisors ≤√n for an array n=1, ..., nmax.
# This method only involves one multiplication for each n up to √nmax

# with that method in place, cantdance's solution can be written as :

def sieve_low_divisors(nmax, excludeone = False):
    """
    Returns a list where the first index is
    n = 0...nmax
    the contents of that index is a list of the divisors
    up to sqrt(n).
    The lists will not have the otherwise mandatory '1'
    as its first entry if excludeone is set to True.
    If excludeone = True, an empty list
    will denote a prime number
    """
    if excludeone:
        result = [[] for n in range(nmax + 1)]
    else:
        result = [[1] for n in range(nmax +1 )]
        result[0] = []
    for n in range(2, int(math.sqrt(nmax)) + 1):
        for dl in result[n * n::n]:
            dl.append(n)
    return result


def problem_88():
    """
    Same approach as user cantdance, but optimized with respect to
    finding the divisors using dynamic programming and a few other
    details
    """
    kmin = 2
    kmax = 12000
    nmax = 2 * kmax
    low_divs = sieve_low_divisors(nmax, excludeone = True)
    S = [set([n-1]) for n in range(nmax + 1)]
    kn = [0] * (kmax + 1)
    solutions = 0
    for n, ds in zip(range(2, nmax + 1), (low_divs[2:])):
        for d in ds:
            for nminusk in S[n // d]:
                S[n].add(d - 1 + nminusk)
        for i in  S[n]:
            k = n - i
            if k <= kmax and not kn[k]:
                kn[k] = n
                solutions += 1
        if solutions == kmax:
            break
    result = sum(set(kn[kmin:]))
    return print(result)

problem_88()

# In this implementation, finding the divisors only takes 8 ms (3%), maintaining the S[n] takes 145 ms (58%)
# and updating the solutions array takes 85 ms (34%).
#
# Now, I was quite satisfied with this optimized solution until I tried to see what happens if I apply psyco.
#
# In that case, cantdance's original solution takes 94 ms, and mine 172 ms.


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 1172.067165 ms





print('\n--------------------------SOLUTION 5, LohenLein, FRANCE --------------------------')
t1  = time.time()

# YEAH :D At last I did it ! So proud ^_^
# I tried lots of ways but I finally found the same method than Euler's.
#
# Initialize a dict PS at PS[k]=2k for each value k∈[2,12000].
# Then you can compute all possible products of 2 terms, then of 3 terms, etc until the product of 14 terms.
# Compute them lexicographicaly and stop when it reaches 24000.
# For each product of n terms, let k=∏−∑+n and update PS[k] if necessary.
#
# Following code runs rather fast : 2.5s

PS={}
for k in range(1,12001):
    PS[k]=2*k

def prod(L):
    p=1
    for l in L:
        p*=l
    return p

def nextL(L):#compute the next product with same number of terms
    pos=len(L)-1
    L=L[:-1]+[L[-1]+1]
    while prod(L)>24000 and pos>0:
        pos-=1
        L=L[:pos]+[L[pos]+1 for i in range(pos,len(L))]
    return L

for power in range(2,16):
    L=[2 for i in range(power)]
    pr=prod(L)
    while pr<24001:
        k=pr-sum(L)+power
        if 1<k<12001 and pr<PS[k]:
            PS[k]=pr
        L=nextL(L)
        pr=prod(L)

LPS=set([PS[k] for k in PS.keys() if k>1])
print(sum(LPS))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, VET FAST , nanogyth, USA --------------------------')
t1  = time.time()

        ####   METHOD I  ####
# Factor numbers til k is full. 1.2s

def fact(n,start=2):
    for i in range(start,int(n**.5)+1):
        if n%i == 0:
            for out in fact(n//i,i):
                out.append(i)
                yield out
    yield [n]

def find_total_sum_prod(max, min=2):
    term_set = set()
    sum_prod_set = set()
    sum_prod = 2
    total = 0
    while True:
        for x in fact(sum_prod):
            #ones = sum_prod - sum(x)
            #terms = ones + len(x)
            terms = sum_prod - sum(x) + len(x)
            if terms not in term_set and min <= terms <= max:
                sum_prod_set.add(sum_prod)
                term_set.add(terms)
                total += 1
                if total == (max-min+1):
                    return sum(sum_prod_set)
        sum_prod += 1

print(find_total_sum_prod(12000))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, SUPER FAST , nanogyth, USA --------------------------')
t1  = time.time()

        ####   METHOD I I ####
# Creating factors instead of factorizing. 400ms

def find_total_sum_prod(MAX):
    def update_list(s=0,p=1,factors=0,start=2,sp_list=[2*MAX]*MAX):
        terms = p - s + factors     # THE KEY of solving the Problem !!!!!!!!
        if terms < MAX and sp_list[terms] > p:
            sp_list[terms] = p
        stop = 2*MAX if p == 1 else (MAX+s)//(p-1)
        for n in range(start,stop+1):
            update_list(s+n, p*n, factors+1, n)
        return sp_list

    return sum(set(update_list()[2:]))

print(find_total_sum_prod(12000))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 7, VERY SHORT, Avi Levy, USA, 30 seconds  --------------------------')
t1  = time.time()

from math import log, ceil

N = 12*10**3
maxLen = ceil(log(N, 2))

best = {}
queue = [([k],k,k,1) for k in range(2,N)]
while queue:
  l,p,s,length = queue.pop(0)
  if p > 2*N:
    continue
  q = p - s + length
  if q > N:
    continue
  if q not in best:
    best[q] = p
  if p < best[q]:
    best[q] = p
  if len(l) == maxLen:
    continue
  for i in range(l[-1],2*N//p):
    queue.append((l+[i],p*i,s+i,length+1))

print(sum(set(best.values()))-2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n--------------------------SOLUTION 7, THE LONGEST , philiplu , USA   --------------------------')
t1  = time.time()

# Fun problem.  Find all factorizations of all composites from 4 up.
# For each factorization, count the ones necessary to make a product-sum match.
# Save the result for the count of factors + count of ones if not already initialized.
# Once every item in the results list is initialized, we're done.  For this case, that happens once we hit 12,200.
# Takes about 6.1 secs.

################# FUNCTIONS ######################
# And here's primehelp.py that has the prime number sieve and factorization helper code that I use in several problems.
# This one required me to add the primehelp.factorizations generator.
# There's probably a faster implementation, but I like the way the recursive solution only generates each possible combination once.

class PrimeList:
    """
    Immutable list of primes optimized for fast access.  List of primes up to a
    limit created at initialization, after which list-style access is used,
    except that "n in prime_list" uses a set (created on demand) for faster
    access.

    Can be used for detecting primality for numbers up to the square of the
    initializing limit.
    """
    def __init__(self, limit = 1000000):
        self.limit = limit
        self.limit_sq = limit*limit
        self.list = [2]
        self.set = None
        multiples = set()
        sqrt = int(limit**0.5)+1
        for i in range(3, limit+1, 2):
            if i not in multiples:
                self.list.append(i)
                if i < sqrt:
                    multiples.update(range(i*i, limit+1, i))
    def __len__(self):
        return len(self.list)
    def __iter__(self):
        return iter(self.list)
    def __getitem__(self, key):
        return self.list[key]
    def __str__(self):
        return str(self.list)
    def __repl__(self):
        return str(self.list)
    def __contains__(self, item):
        try:
            result = item in self.set
        except:
            self.set = set(self.list)
            result = item in self.set
        return result

    def is_prime(self, n):
        """ Determine if n is prime.  Raises error if n > limit^2 """
        if n < self.limit:
            return n in self
        if n >= self.limit_sq:
            raise OverflowError("Can only test is_prime up to {0}".format(self.limit_sq))
        sqrt_n = int(n**0.5)+1
        for prime in self.list:
            if n % prime == 0:
                return False
            if prime > sqrt_n:
                break
        return True

def prime_factors(n, primes):
    """ Calculate prime factorization of n, given list of primes.
        Returns list of tuples, each tuple consisting of a prime
        factor and the power for that prime. """
    factors = []
    for prime in primes:
        if prime * prime > n:
            break
        count = 0
        while n % prime == 0:
            n //= prime
            count += 1
        if count > 0:
            factors.append((prime, count))
    if n > 1 or len(factors) == 0:
        factors.append((n, 1))
    return factors

def factors(n, primes):
    """ Calculate list of all factors of n, including 1 and n.
        'primes' is pre-computed list of primes.
        NOTE - the factors are not returned in sorted order, but 1 will always
        be the first factor, and n will always be the last. """
    pfs = prime_factors(n, primes)
    factors = []
    def helper(index, product):
        index -= 1
        prime, power = pfs[index]
        for i in range(power+1):
            if index > 0:
                helper(index, product)
            else:
                factors.append(product)
            product *= prime
    helper(len(pfs), 1)
    return factors

def factor_sum(n, primes):
    """ Find the sum of the proper divisors of n.  'primes' is the pre-computed
        list of primes. """
    return sum(factors(n, primes)[:-1])

def factorizations(n, primes, singleton=True):
    """ Generate all possible factorizations of n (not counting any with a 1
        as a factor).  'primes' is the pre-computed list of primes.  'singleton'
        is False if you want to suppress the factorization consisting of the
        number to factor by itself. """
    def helper(n, max_f):
        for factor in reversed(factors(n, primes)[1:]):
            if factor > max_f:
                continue
            new_n = n // factor
            if new_n > 1:
                for combo in helper(new_n, factor):
                    yield combo + [factor]
            else:
                yield [factor]
    for combo in helper(n, n if singleton else n-1):
        yield combo

def gcd(a, b):
    """ Find the greatest common divisor.  Not really prime-help, but useful. """
    while b != 0:
        a, b = b, a % b
    return a

"""
Note that a minimal product-sum number can't be prime, since we need at least
two factors (1 is already the minimal product-sum for k=1), and prime + 1 is
greater than prime * 1.

So, search the composite numbers in ascending order.  For each, generate all
combinations of factors that multiply to the original number.  Calculate the
number of ones to add so the sum of the factors plus the ones equals the
orignal composite.  Save that composite as the minimal product-sum for k = the
count of factors plus count of ones, unless there's a smaller existing value
for that k.

Keep searching through composites until we know nothing will be updated in the
list of minimal product-sums.  That happens when there are no empty slots in
the table.
"""

# --------------- SOLUTION ------------------------

import sys
import itertools as it


def p88(limit = 12000):
    primes = PrimeList(limit)
    results = [None] * (limit + 1)
    uninit_count = limit - 1
    for n in it.count(4):
        if uninit_count == 0:
            break
        for factors in factorizations(n, primes, singleton=False):
            n_sum = sum(factors)
            one_count = n - n_sum
            k = len(factors) + one_count
            if k <= limit and results[k] is None:
                uninit_count -= 1
                results[k] = n
    return sum(set(results[2:]))

print(p88(*(int(arg) for arg in sys.argv[1:])))           # Uncomment to Activate

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 7752.443314 ms