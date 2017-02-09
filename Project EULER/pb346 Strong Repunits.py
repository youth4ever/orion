#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Sat, 4 Feb 2017, 00:18
#The  Euler Project  https://projecteuler.net
'''
                    Strong Repunits     -   Problem 346

The number 7 is special, because 7 is 111 written in base 2, and 11 written in base 6
(i.e. 7_10 = 11_6 = 111_2). In other words, 7 is a repunit in at least two bases b > 1.

We shall call a positive integer with this property a strong repunit.
It can be verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}.

Furthermore, the sum of all strong repunits below 1000 equals 15864.

Find the sum of all strong repunits below 10**12.

'''
import time, math


def toStr(n, base):
   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn"
   # print(len(convertString))
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print()
convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef"
print(len(convertString))


def convert_repunit( ones, base ) :
    return sum([ base**i for i in range(len(str(ones))) ])

print('convert_repunit :\t', convert_repunit(111, 7) )
print('convert_repunit :\t', convert_repunit(1111, 19) ,'\n')

print('\n--------------------------INITIAL VERIFICATION TEST------------------------------')
t1  = time.time()

def initial_verification_test( up ) :
    s = {1,7,13,15,21,31,40,43}         # First 50
    print(sum(s), '    ',s, '\n')
    S = sum(s)
    for n in range(2, up ) :
        # print('\nnr = ', n, end ='       ')
        for b in range(2, 43) :
            n0 = toStr(n, b)
            if set(n0) == {'1'} :
                S+=n
                print(str(n)+'.       ', toStr(n, b), '    ',b)

    return print('\nInitial verification : ',S)

# initial_verification_test(10**4)

# up_range = 1000
# S = 1
# for n in range(2, up_range+1) :
#     tmp = []
#     for b in range(2, 11) :
#         s = toStr(n, b)
#         l =  list(s)
#         if  len(set(l)) == 1 and l.count('1') >= 1    :
#             tmp.append(s)
#             print( n, b , s   )
#     if len(tmp) >=2 :
#         S += n
#
#     # print('--------')
#
# print('\n\nAnswer :\t', S)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print(' ---------------- the inverse procedure ------------- ')
# for i in range(2, 43) :
#     s = toStr(11, i)
#     l =  list(s)
#     if  len(set(l)) == 1 and l.count('1') >=1    :
#         print( i, s  , l  )
# print(toStr(42**3+42**2+42**1+42**0, 42))

# below 10**12
# print(10**12)


# @ 2016-12-17, 13:30 - My initial calibration failed. I can't find the maximum allowable base. I found 43 for <50
# but when I verify for the first 1000 numbers to be the sum S = 15864 I fail. I obtain only the numbers bellow 50
# TODO : I need to find what is the maximum allowable base and re-do the calibration !

# SOLUTION :
# We only test from length 111 up, because any number like 7 in base 6 = 11, sau 10 in base 9 = not 11...etc..
# Therefore any number can have a single repunit of the form 11
# Our task becomes simple : if for a number we find that forms a repunit with length > 111 in a lower base
# than n-1 ==> and we find this repunit ==> er alread y have 2 repunits and that number is valid
# Example :
# Take number 15 :  15 in base 14 = 11 ;  15 in base 2 = 1111 ==> We only search for repunits >=111 of length.async
# More than that : the base search space is limited.
# 3 digits  111 we have sqrt(10**12) = 10**6 up range
# 4 digits , 1111 ---> 10**4  (**1/3)
# 5 digits , 11.111 ---> 10**3  (**1/4)
# 6 digits , 111.111 ---> 521  (**1/5)
# 7 digits , 1.111.111 ---> 100  (**1/6)
# 8 digits , 1111.1111 ---> 52   (**1/8)
# 9 digits , 111.111.111 ---> 32  (**1/9)




print('\n================  My FIRST SOLUTION,  8 sec  ===============\n')
t1  = time.time()


def strong_repunits(UP) :
    r_max_length = math.ceil(math.log2(10**12))
    P = {1}
    cnt = 0
    for length in range(3, r_max_length+1 ) :
        r = (10**length-1)//9
        up_lim = math.ceil( (UP)**(1/(length-1)) )
        print(r,'      ' ,up_lim)
        for b in range(2, up_lim+2 ) :
            cnt+=1
            c = convert_repunit(r, b)
            if c <= UP :
                P.add(c)
        # print(r , '      ',c,'       b=', b)
    P = list(P)
    P.sort()
    print('\n', cnt - len(P), ' numbers were above the up range' )
    print('Total numbers : \t', len(P), '\n', P[-200:] )

    return print( '\n\nAnswer : ',  sum(P) )

# strong_repunits(10**12)                     #       Answer :  336108797689259276



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, 3 sec  --------------------------')
t1  = time.time()

# ====== Thu, 1 Dec 2016, 22:32, zinger_13, Canada
# similar code to those above.  runtime is 1.3s

ans = {1}
nmax = 10**12

for b in range(2,10**6):  # check up to sqrt(nmax)
    n = b ** 2 + b + 1
    while n < nmax:
        ans.add(n)
        n = n*b + 1

print(sum(ans))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Mon, 31 Aug 2015, 20:36, Susie, Canada
# Not very special, but using Python's set type vastly reduced the time taken (versus making a list and manually checking for duplicates).


def p346():
    max_n = 10**12
    summed = set([1])
    b = 2
    while b * b + b + 1 < max_n:
        n = b * b + b + 1
        power = b * b * b
        while n < max_n:
            summed.add(n)
            power *= b
            n = (power - 1) / (b - 1)
        b += 1
    return sum(list(summed))

# p346()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ===== Sat, 16 Apr 2016, 15:43, Levi, USA
# Finding and summing all of the unique bases under target N. Takes 1.8s


def base_add(base, exp, num, target, collection):
    new = (base ** exp) + num
    if new > target:
        return 0
    elif new not in collection:
        collection.add(new)
        return new + base_add(base, exp + 1, new, target, collection)
    else:
        return base_add(base, exp + 1, new, target, collection)


def pe_346(target):
    total = 1
    collection = set()
    for n in range(2, int(target**0.5) + 1):
        total += base_add(n, 2, n + 1, target, collection)

    return total


if __name__ == "__main__":
    target = 10**12
    # print(pe_346(target))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ===== Sat, 7 Mar 2015, 03:59, ravoorheis, USA
# Brute force took about 3s in python.  I didn't recognize the 3-digit repunit fact that most others did,
# but I did realize that any n is 11 base n-1, and 111 will be greater than 10**12 for any base larger than 10**6.
#
# So for each n < 106, I started with 1, added consecutive powers of n less than 10**12, and if the result was less than 10**6,
# I kept track with a counter and added to a running sum exactly when there was a second hit.
# Any repunit n between 10**6 and 10**12 will also occur as a repunit base n-1, so I threw all those into a list.
# At the end, I added the running sum to the sum of the list.  Not pretty, but it worked. :D


from collections import defaultdict

SmallRepCount = defaultdict(int)
BigRepList = []
i = 2

s = 0
while i < 10**6:
    n = 1
    acc = 1
    while acc < 10**12:
        if acc <= 10**6:
            if SmallRepCount[acc] == 1:
                s+=acc
                SmallRepCount[acc]+=1
            if SmallRepCount[acc] == 0:
                SmallRepCount[acc]+=1

        if acc > 10**6:
            BigRepList.append(acc)
        n*=i
        acc+=n
    i+=1

print (s + sum(list(set(BigRepList))) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  2 sec --------------------------')
t1  = time.time()

# === Sat, 30 May 2015, 08:38, jbum, Python  , USA

limit = 10**12
srepunits = set([1])
for b in range(2,int((limit-1) ** .5)+1):
    p = b*b
    v = p + b + 1
    while v < limit:
        if v not in srepunits:
            srepunits.add(v)
        p *= b
        v += p
print ("Tot",sum(srepunits))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ===== Mon, 2 Sep 2013, 02:18, Oren, USA
# Like some of the other solutions, the key observation is that every n >= 3 can be written in at least one way as (11)_(n-1).
# Therefore we only need to search O(sqrt(N)) bases for a second repunit representation (instead of O(N) with a naive method).

def strong_repunits(N):
    '''Return the set of strong repunits < N.'''
    s = set([1])
    for b in range(2, int(((4 * N - 7) ** 0.5 - 1) * 0.5) + 1):
        x = b * b + b + 1
        while x < N:
            s.add(x)
            x = b * x + 1
    return s

if __name__ == "__main__":
    print (sum(strong_repunits(10 ** 3)) )# 15864
    print (sum(strong_repunits(10 ** 12))) # 336108797689259276

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   ORIGINAL--------------------------')
t1  = time.time()

# =====Wed, 8 Jan 2014, 02:52, gechhesy, USA
# I actually appreciate having some fairly easy but fun problems mixed in..
# Some of these take me 10's of hours and week of elapsed time. It's refreshing to have a relatively easy
# (that still requires  insight) once in a while.
# =============
#
# n is a repunit in base n-1. so just any number that is a repunit in any other base than n-1 counts!.
#
# Since the repunits of n=10**6 are either the trivial one (n-1) or > 10**12, no need to check bases larger than that.
#
# generating repunits in a given base is easy. Start with v = 1, then nextV=v*b+1.
# this grows quickly so the inner loop is fast enough to just run through them all.
#
# So just iterate over each base from 2 to 10**6 from (b+1)*b+1 < 10**12 and collect answers in a set.


from itertools import *

def gru(b):
    """
    add all of the repunits base b to s that are <= mx
    """

    v=1
    while True:
        yield(v)
        v=v*b+1

def q346(N):
    b=2
    s = set()
    s.add(1)
    for b in range(2, int(N**.5)+1):
        s.update(_ for _ in takewhile(lambda x: x< N, gru(b)) if _>b+1)
    return s
q346(10**3)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

