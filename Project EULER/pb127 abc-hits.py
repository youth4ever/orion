#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Mon, 16 Jan 2017, 22:33
#The  Euler Project  https://projecteuler.net
'''
abc-hits        -       Problem 127

The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

1.      GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
2.      a < b
3.      a + b = c
4.      rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

1.      GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
2.      5 < 27
3.      5 + 27 = 32
4.      rad(4320) = 30 < 32

It turns out that abc-hits are quite rare and there are only 31 (thirty-one) abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.

'''
import time, gmpy2
from math import gcd, log, sqrt
from pyprimes import factorise
import functools, operator
from itertools import count

def get_factors(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def prime_generator(n):         # HIghly Efficient !!!!         THE FASTEST, The BEST , The ONE
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.     """
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2
    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (n // cand[i]) - (n // (2 * cand[i])) - 1 )
    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]


def binary_search(n, List):        # VERY FAST ALGORITHM
    ''':Description: Search for an element in the list and returns the index of it. If it not finds it returns
        the index of the element closest to its left, the smaller number.
    :param: **n**- integer, the number to find
                **List** - lst type, the list to search for
    :returns:   int, the index of the element
    '''
    left = 0
    right = len(List) -1

    while left <= right:
        midpoint = (left+right)//2
        if List[midpoint] == n: return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint
    else: return (midpoint-1)

prm = prime_generator(350)
def find_base_pwr(n, prm):
    ''':Description: Returns a tuple in the form (base, power). Depends on pre-generated primes up to sqrt(n)
            :param: **n**  - int, searching for number
            :param: **prm**  - the list of primes generated before
            :return: tuple(base, power)    '''
    # prm = [2,3,5,7,11]

    for i in prm :
        if  0 <= abs( log(n , i) - round(log(n , i)) ) %1 <= 1e-9 :
            return i, round(log(n , i))
    return n


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

P = prime_generator(120000)
print(len(P), P[-100::],'\n')
print('Factorise Test :  ', list(factorise(32)) )

print('There are exactly C{11414,3}: ' , gmpy2.comb(11414, 3),'   unique combinations' )
print(' Test the power', gmpy2.is_prime(491 ) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


t1  = time.time()

print('Test for the function find_base_pwr :\t',find_base_pwr(815730721, prm) )
print('Test for the function find_base_pwr :\t',find_base_pwr(17**4, prm) ,'\n')

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

def rad_abc( lst ):
    ''':Description:   find the rad of three numbers where rad is :
     For example:     504 = 2**3 × 3**2 × 7, so rad(504) = 2 × 3 × 7 = 42  ;  Second example :

     a= 125 = 5^3,  b= 50176=2^10*7^2,  c= 50301 = 3^7 *23   => rad(a,b,c) = 5*2*7*3*23 = 4830 '''
    L = set()
    for i in lst :
        k = [ j[0] for j in factorise(i) ]
        L.update(k)
    return  functools.reduce(operator.mul, L)


print('Test for the rad_abc Function : \t ',rad_abc( [2, 241, 243 ] ) )
print('Test for the rad_abc Function : \t ',rad_abc( [ 90, 210, 143 ] ) )

t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n------------ Construction of the Initial List------------\n')
t1  = time.time()

def generate_composites(up_limit , factor_nr ) :
    ''':Description: Generate composite numbers    '''
    primes = prime_generator( int( sqrt(up_limit)) * 4 )
    D = { x: x  for x in primes }
    print(primes,'\n')
    PS = []
    D[1] = 1 ; D[759]=759       # We need 1 , and 759 is the only number of the form [p1, p2,p3]
    for i in primes :                   # powers of a single digit
        for j in count(2) :       # Very Important, We need only composite numbers in our list
            n = i**j
            if n > up_limit : break
            PS.append(n)
            D[i**j] = i

    PS.sort()
    print(len(PS), PS[0:300],'\n')
    # print(D)

    for h in range(1, factor_nr):
        id = binary_search( (up_limit-1)//2, PS)
        # print('binary_search Function : \tindex : ', id,'     the number:  ' ,PS[id] ,'\n'  )
        tmp = []
        for i in range(0, id + 1):
            for j in range(i+1, id +1):
                m = PS[i] * PS[j]
                if m >= up_limit : break
                tmp.append(m)
                # print( PS[i], PS[j], m )
                if m not in D :
                    e= gcd(PS[i], PS[j])
                    if e != 1 : D[m] = (D[PS[i]] * D[PS[j]]) // D[e]
                    if e == 1 : D[m] = D[PS[i]] * D[PS[j]]
                    # print( PS[i], PS[j], m, '     ', D[PS[i]], D[PS[j]] ,  e ,'    ' , D[m], '      -->', h)

        # print('tmp',tmp)
        # print('Dictionary : ', D)

        for k in primes :           # Here we add composite numbers having a single prime
            for l in PS :
                o = k*l
                if o < up_limit :
                    tmp.append(o)
                    # print( k, l ,o, '       ', D[k], D[l] )
                    if o not in D :
                        g= gcd(k, l)
                        if g != 1 : D[o] = D[k]*D[l] //D[g]
                        if g ==1 : D[o] = D[k]*D[l]
                        # print( k, l , o, '       ', D[k], D[l] , '     gcd=', g, '     value',D[o] ,'     --- >    ', len(PS) )
        PS.extend(tmp)

        PS = set(PS)
        PS = sorted(PS)
        # print(len(PS), PS)
    # We finally add to the dictionary some numbers = [ p1, p2 ]
    for i in range(len(primes)):
        for j in range(i+1, len(primes)) :
            p1p2 = primes[i]*primes[j]
            D[p1p2] = p1p2
    return PS, D

Comp = generate_composites(1.2*10**3, 4)
print('\nTotal length : ', len(Comp[0]),'\n', Comp[0][0:300])
print('\nDictionary : ', len(Comp[1]),'\n')
print(759 in Comp[1])

######################



#######################

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('---------------------------\n')
t1  = time.time()



# @ 2016-12-22, 19:50, for some reason I get only 12 out of 31 results for c<1000 !!!! Must find the cause !
# Must rethink it becase  it seems that I can have composed numbers like 96 [2,2,2,2,2,3] and must re-do the abc hit function
# to acomodate this
#                       CORRECT ABC-HITS :
#                   a = 1, b = 675, c = 676
#                   a = 343, b = 625, c = 968
#                   a = 1, b = 224, c = 225

# 1.   n= 48000    a= 3 [3]    b= 125 [5, 5, 5]     c=  128    r=  30
# 2.   n= 4320    a= 5 [5]    b= 27 [3, 3, 3]     c=  32    r=  30
# 3.   n= 808704    a= 13 [13]    b= 243 [3, 3, 3, 3, 3]     c=  256    r=  78
# 4.   n= 72    a= 1 [1]    b= 8 [2, 2, 2]     c=  9    r=  6
# 5.   n= 60500    a= 4 [2, 2]    b= 121 [11, 11]     c=  125    r=  110
# 6.   n= 72    a= 8 [2, 2, 2]    b= 1 [1]     c=  9    r=  6
# 7.   n= 4320    a= 27 [3, 3, 3]    b= 5 [5]     c=  32    r=  30
# 8.   n= 127008    a= 32 [2, 2, 2, 2, 2]    b= 49 [7, 7]     c=  81    r=  42
# 9.   n= 29679104    a= 169 [13, 13]    b= 343 [7, 7, 7]     c=  512    r=  182
# 10.   n= 127008    a= 49 [7, 7]    b= 32 [2, 2, 2, 2, 2]     c=  81    r=  42
# 11.   n= 29679104    a= 343 [7, 7, 7]    b= 169 [13, 13]     c=  512    r=  182
# 12.   n= 808704    a= 243 [3, 3, 3, 3, 3]    b= 13 [13]     c=  256    r=  78
# 13.   n= 60500    a= 121 [11, 11]    b= 4 [2, 2]     c=  125    r=  110
# 14.   n= 48000    a= 125 [5, 5, 5]    b= 3 [3]     c=  128    r=  30
# 2, 4, 8, 16 ,....
# 1. Obtain all the needed numbers for b &c , make a list
# 2. combinations of b and c and then obtain a
# the list must not contain
# Because the biggest can't be > 120.000 and gcd(a,b,c) == 1 I need only combinations of 4 primes
# b,c,a = (4 primes, 1, 1) but it also could be that I would need 5 1 1 where the last one a=1
# That last case 5 1 1 could be in the case that 5 primes_multipled - 1 prime**some power ==1

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# filter
'bogdan'.startswith('b')

# print('\n-------------- BRUTE FORCE Search Testing -----------')
#
t1  = time.time()

def brute_force(up_limit):
    cnt, itr, c_sum = 0, 0, 0
    for b in range(3, up_limit) :
        for c in range(b+1, up_limit):
            a = c-b
            # if a > b : break
            if a < b:
                if gcd(a, b) ==1 and gcd(b, c) ==1 and gcd(a,c) ==1 :
                    rad = rad_abc([a, b, c])
                    if rad < c :
                        cnt+=1
                        c_sum += c
                        print(str(cnt)+'.       a=' ,a,'     b=' ,b, '     c=',c , '    rad=',rad ,'     b=',  get_factors(b) ,'      c=', get_factors(c) )

    return print('\nSum of C :\t', c_sum)               # Very expensive : Completed in : 8981.513739 ms

brute_force(10)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n================  My FIRST SOLUTION,   SLOW, 4 min  ===============\n')
t1  = time.time()


def solution_composites(up_limit, factor_nr ):
    G = generate_composites(up_limit, factor_nr )
    T, D = G[0], G[1]
    print('Total length : ',len(T), len(D) )
    cnt, itr, c_sum = 0, 0, 0
    for i in range(len(T)):
        for j in range(i+1, len(T)) :
                if gcd(D[T[i]], D[T[j]]) == 1 :
                    b, c = T[i], T[j]
                    a = c - b
                    # itr+=1
                    # print(str(itr)+'.      ' , b, c,'       ', a,'    ' ,get_factors(a))
                    if a > b : break
                    elif a in D :
                        # if gcd(a,b) ==1 and gcd(a,c) ==1 :
                        rad = D[a]*D[b]*D[c]
                        if rad < c :
                            cnt+=1
                            c_sum += c
                            A, B, C = get_factors(a), get_factors(b), get_factors(c)
                            print(str(cnt)+'.       a=' ,a,'     b=' ,b, '     c=',c , '    a=',A, '      b=',  B, '      c=', C , '       ',
                                  len(set(A)),  len(set(B)),  len(set(C))  )


    return print('\nSum of C-s :\t', c_sum, '\n' )


# solution_composites(1.2*10**5, 4)           # Sum of C-s :	 18407904

#       WRONG SOLUTIONS :
#       Sum of C-s :17769088    with 3 composites
#         Sum of C-s :	 17851430  with 4 composites
#       Sum of C-s :	    17851430
#       Sum of C-s :	 18407904       with 4 composites, primes to 1200
# Sum of C-s :	 18407904       : FINALLY CORRECT


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')        #   Completed in : 265.499186 s


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 0, FASTEST & VERY ELEGANT & FAST , 2 seconds  --------------------------')
t1  = time.time()

# ==== Thu, 16 Oct 2014, 21:45, HuggyHermit, Scotland
# Posting this, since about a second in Python seems to be fairly good for this problem. :)
# It uses a sieve to calculate a table of radicals, then sorts them into radical order.
#     Then it iterates over c and "a" using this sorted list, relying on
#
# rad(abc) = rad(a)*rad(b)*rad(c) < c (for a,b,c coprime),
# which means rad(a)*rad(b) < c/rad(c)
#
# From this, it follows that the smaller of rad(a) and rad(b) must be below sqrt(c/rad(c)).
# Thus, it searches through the sorted list for an a (< c) within this bound, accepting that we have possibly violated a < b.
# However, this will still catch all the hits.
# Then, it's just a case of calculating b and checking whether we have a hit or not.
#
# One small annoyance is that this sometimes calculates the same hit twice
# (if both rad(a) and rad(b) are below sqrt(c/rad(c))), so it has to check for this.


from math import gcd, sqrt

limit = 120000
rad = [1+(x%2) for x in range(limit)]
for n in range(2, limit, 2):
    if rad[n] == 1:
        for m in range(n, limit, n+1):
            rad[m] *= n+1

total, sumtotal = 0, 0
radsort = sorted(zip(rad, range(1, limit+1)))[:limit//2]
for crad, c in radsort:
    if crad >= c/2:
        continue
    target = c/crad
    starget = int(sqrt(target))
    solutions = []
    for arad, a in radsort:
        if arad > starget:
            break
        if a > c:
            continue
        b = c - a
        if rad[b-1]*arad <= target and a not in solutions and gcd(a,b) == 1:
            total += 1
            sumtotal += c
            solutions.append(b)

print (total, sumtotal)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 1, VERY ELEGANT & FAST , 8 sec  --------------------------')
t1  = time.time()

# ==== Sat, 14 Nov 2015, 23:05,hornemann55, Denmark
# This was quite callenging to get to run fast, but I'm rather sattisfied with the result. Short and clean, runs in 7 seconds:

from pyprimes import  primes_below

def abchits(N):
   # from primes import atkin
   primes = primes_below(N)
   fact = [1]*(N+1)
   for p in primes:
      for j in range(1,N//p+1):
         fact[p*j]*=p
   s,n = 0,0
   F = sorted(enumerate(fact), key = lambda x:x[1])
   C = sorted(enumerate(fact),key= lambda x:x[0]/x[1], reverse=True)

   def CP(A,B):
      while (B > 0):
         A,B = B,A % B
      return A == 1

   for c, fc in C:
      if c < fc+fc+3: break
      for  a, fa in F :
            if fa*fc*2 > c:break
            if   a+a < c and fa*fc*fact[c-a] < c  and CP(a,c):
               n+=1
               s+=c
   return(n,s)

# print(abchits(120000))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  18 sec --------------------------')
t1  = time.time()

# ==== Fri, 23 May 2014, 20:30, superbit, Israel
# took me a while with this one, glad i finally solved it :)
# code runs in ~20 sec.

import timeit
from math import gcd

rad_dict	= {}		# quick rad result
rad_list	= []		# sorted rad list
prime_factors 	= {}		# prime factors dictionary
primes_list 	= []		# sorted primes - loop trough
primes_set 	= set()		# check if prime

def sieve(N):
	"""
	Sieve of Eratosthenes
	"""
	prime_set = set()
	primes = [True]*N
	primes[0] = primes[1] = False
	for i in range(2, N):
		if primes[i]:
			prime_set.add(i)
			j = 2*i
			while j < N:
				primes[j] = False
				j += i
	return prime_set

def factors(num):
	global prime_factors
	result = []
	original = num

	if num in prime_factors:
		return prime_factors[num]

	if num in primes_set:
		prime_factors[num] = [num]
		return prime_factors[num]

	i = 0
	while i < len(primes_list) and 1 < num:
		while 0 == num % primes_list[i]:
			result.append(primes_list[i])
			num /= primes_list[i]
		if num in prime_factors:
			prime_factors[original] = result + list(prime_factors[num])
			return prime_factors[original]
		i += 1

	prime_factors[original] = result
	return result

def rad(num):
	global rad_dict, rad_list

	if num in rad_dict:
		return rad_dict[num]

	result = 1
	for prime in set(prime_factors[num]):
		result *= prime

	rad_dict[num] = result
	rad_list.append((result, num))
	return result

def binary_search(value, last, start, end):
	global rad_list
	cur_index = (start+end)//2
	if value == rad_list[cur_index][0] or (start,end) == last:
		return cur_index
	elif rad_list[cur_index][0] < value:
		return binary_search(value, (start,end), cur_index, end)
	return binary_search(value, (start,end), 0, cur_index)

def solve(N):
	global primes_set, primes_list, rad_list

	print ('finding all hits for c < {0}'.format(N))

	primes_set = sieve(N)
	primes_list = list(primes_set)
	primes_list.sort()

	rad_dict[1] = 1
	rad_list.append((1,1))

	for i in range(2, N):
		factors(i)			# prime factors sieve
		rad(i)				# rad sieve, updates rad_list

	rad_list.sort()
	hits = []

	for c in range(1, N):
		if c > rad(c):
			# rad(a) * rad(b) < c/rad(c), so each of them is less than c/2rad(c)
			bound = c / (2 * rad(c))
			index = binary_search(bound + 1, -1, 0, len(rad_list))
			for current in rad_list[:index]:
				a = current[1]
				if a<c/2 and gcd(a, c-a)==1 and gcd(a, c)==1 and gcd(c-a, c)==1:
					if rad(a) * rad(c-a) * rad(c) < c:
						hits.append((a, c-a, c))

	return sum(hit[2] for hit in hits)


start = timeit.default_timer()		# start timing
print ('calculating solution...')
answer = solve(120000)

print ('Answer	 : {0}'.format(answer))
print ('Run time : %.3f'% (timeit.default_timer() - start) +'s')

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 5,  FAST , 13 sec --------------------------')
t1  = time.time()

# ===== Mon, 25 Feb 2013, 21:10, tom.wheldon, England
# Struggled to get this to run in a reasonable time even with all kinds of optimisation until I used sorted
# radicals in the loop instead of numbers - annoying,
# because that had been my first thought but I hadn't followed it through.
# That got the running time down to 22s in Python but could have been better
# if I'd spotted that I only needed gcd(a,b).

from math import gcd

limit = 120000
rads = [[1,n] for n in range(limit)]
for n in range(2,limit):
    if rads[n][0] == 1:
        for i in range(n, limit, n):
            rads[i][0] *= n

radssort = sorted(rads)
del radssort[0]
rads = [x[0] for x in rads]


sumc = 0
nc = 0
for c in range(3,limit):
    radsc = rads[c]
    d = c//2
    for x in radssort:
        if x[0]*radsc > d:
            break
        if x[1] >= d:
            continue
        a = x[1]
        b = c-a
        if (gcd(a,b) == 1 and radsc*rads[b]*rads[a] < c):
            nc += 1
            sumc += c

print(nc, sumc)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 7,  SLOW --------------------------')
t1  = time.time()

# === Sun, 26 Jul 2015, 15:11, arnet95, Python, Norway
# I found this problem quite easy.
# The two basic insights are that rad(abc) = rad(a)rad(b)rad(c) since a,b,c are all relatively prime and
# that if we precompute the radicals up to 120000, we're pretty good.

#Project Euler 127: abc-hits
from pyprimes import primes_below
from math import gcd
primes = primes_below(120000)
def rad(n):
    """dynamic radical up to n"""
    l = [1]*(n+1)
    for prime in primes :
        for i in range(prime, n+1, prime):
            l[i] *= prime
    return l

def main(n):
    s = 0
    radicals = rad(n)
    for c in range(3, n):
        if radicals[c] < c:
            for a in range(1, c//2+1):
                if radicals[a]*radicals[c-a]*radicals[c] < c:
                    if gcd(a, c) == 1 and gcd(a, c-a) == 1:
                        s += c
    return s

# print (main(120000))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 8,  20 sec --------------------------')
t1  = time.time()

# # === Tue, 17 Jan 2017, 08:22, mbh038, England
# About 21s in Python. Like many others, I realised that if a,b and c are co-prime,
# then rad(abc)=rad(a)rad(b)rad(c).
# Thus, for each c we need only consider as or bs for which c/rad(c)>rad(a)rad(b).
# Further, it is sufficient to check that one pair from aa,bb,cc is co-prime.
# Using these ideas, I pre-computed all rad values then, for each possible c value,
# shifted through possible a,ba,b pairs, looking for a hit, the trick being to fail as fast as possible
# if a hit was not to be found and leave time consuming stuff (find GCD, search through large array) until last.


import math
import numpy as np

def p127(limit):

    rads=rsieve(limit+1)
    count=0
    csum=0
    for c in range(1,limit):
        crads=rads[:c+1]
        crad=crads[c,1]
        radpair=crads[crads[:,1]<c/crad]
        if not c%2:
            radpair=radpair[radpair[:,0]%2==1]
        if len(radpair)<2:
            continue
        for a in radpair:
            b=c-a[0]
            if b<a[0]:
                break
            brad=rads[b,1]
            if a[1]*brad*crad>=c:
                continue
            if math.gcd(a[0],b)>1:
                continue
            if b not in radpair[:,0]:
                continue
            csum+=c
            count+=1

    print(count,csum)


def rsieve(limit):
    """returns array of tuples (n,rad(n))"""
    rsieve=np.ones(limit+1,dtype=int)
    nz=np.arange(0,limit+1, dtype=int)
    for i in range(2,limit+1):
        if rsieve[i]==1:
            rsieve[i::i]*=i
    rads = np.vstack(([nz.T], [rsieve.T])).T
    return rads

rsieve(120000)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 9,  30 min --------------------------')
t1  = time.time()

# ===== Tue, 14 Jul 2015, 00:16, Conceity
# Code takes roughly 30 min to run ugh, not quite sure why it takes so long to run, but looking into it.
#
# Code Summary:
# Uses Euclidean Algorithm to determine if two numbers are coprime
# Generate a list of primes up to the sqrt(120 000) using the Sieve of Eratosthenes
# Use the list of primes to generate and store the rad values of the first 120 000 numbers
# Loop a, b with a starting from 1 and b starting from a + 1 while still satisfying c < 120 000
# For each pair of (a, b) I check first if rad(a)*rad(b)*rad(c) < a + b, and then check if gcd(a, b) = 1.
# I found that rad(a)*rad(b)*rad(c) < a + b is faster to check than gcd(a, b) = 1
# I also made the simplifications that gcd(a, b) = gcd(rad(a), rad(b)) and that gcd(a, b) = 1 is enough
# to guarantee that a, b, c are pairwise coprime
# Edit: Hmm... I had not seen/done Problem 124 before attempting this one as I was jumping around.
# Seems like it would have helped.

def slow_soln():
    primes = []

    def EuclideanAlg(a,b):
        if a <= b:
            a,b = b, a
        if (b == 0):
            return a
        if (b == 1):
            return 1
        else:
            return EuclideanAlg(b, a - b*(a//b))

    def findPrimes(p, n):
        allNums = []
        for i in range(2, n + 1):
            allNums.append([i, 1])
        for i in range(2, n+1):
            if allNums[i-2][1] == 1:
                p.append(i)
                for j in range(2, (n+1)//i + 1):
                    allNums[j*i-2][1] = 0
        return p

    def rad(n, p):
        prod = 1
        iter = 0
        while (iter < len(p)):
            if n%p[iter] == 0:
                prod = prod*p[iter]
            while (n % p[iter] == 0):
                n = n/p[iter]
            iter = iter + 1
        prod = prod * n
        return prod

    n = 120000
    findPrimes(primes, 346)
    radArr = [0]
    for i in range(1, n+1):
        radArr.append(rad(i, primes))

    totalC = 0
    for i in range(1, n//2):
        #print(i)
        for j in range(i+1, n-i):
            if (radArr[i]*radArr[j]*radArr[i+j] < (i+j)):
                if EuclideanAlg(radArr[i], radArr[j]) == 1:
                    print(i, j, i+j)
                    totalC = totalC + i + j
    print(totalC)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')