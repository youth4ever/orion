import time


###############   SIEVE - DIGITAL ROOT FACTORIZATION  ##############


t1  = time.time()


# ==== Tue, 26 Mar 2013, 14:16, tom.wheldon, England
# Similar to quite a few others - uses a sieve to store a list of divisors up to √n for each n,
# then steps through again to calculate the mdrs for each n using the divisor list
# and the values already calculated.  Runs in under 7s in Python.

N = 1000

D = {n: [] for n in range(2,N)}

for i in range(2, int((N-1)**0.5)+1):
    for j in range(i*i, N, i):
        D[j].append(i)

for n in range(2,N):
    a = n%9
    mdrs = a if a else 9
    if D[n]:
        for div in D[n]:
            mdrs = max(mdrs, D[div] + D[n//div])
    D[n] = mdrs

print(sum(D.values()))


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')



############### BUILD OF SIEVE OF FACTORS, SIEVE FACTORIZATION ##############
print('\n -------------------------SIEVE FACTORIZATION ------------------------ ')

# Here we want to keep in a sieve the direct factorizations, factors like [2,2,3], [2,2,3,3,5] and so on such
# that we have a complete list of number factorizations up to a limit
# This is accomplished as follows :
# 1. Use a prime sieve, prime number generator

def sieve(n):       # SECOND FASTEST        o(^_^)o
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

# STEP 1 - First construct a sieve only with single prime to some power like : 32,64, 27,81,....
# and put them in a list

F = []
lim =1000
for p in [2,3,5,7,11] :
    e = 1
    while p**e < lim :
        p1 = p**e
        F.append(p1)
        e+=1
    print(F)

print('\n---------Step 2---------------')
# STEP 2 - Now make combinations of those on the run, by using the list F
# at each step and combining it with the new bigger factors
# We will use a dictionary as this is fastest for indexing as it has hash mapped
# But the idea is not that we have all factors out there .
# The idea is that we calculate ON THE RUN exactly what we want
import  time, gmpy2
t1  = time.time()

# Actually is takes FOREVER TO RUN, MUST CHANGE IT !!!!!!!!!!!!

D={}
F = []
lim = 10**2
primes = sieve(lim//6)
for p in primes :           #[2,3,5,7,11] :
    e = 1
    tmp=[]
    while p**e < lim :
        p1 = p**e
        tmp.append(p1)
        D[p1] = (p**((e+1)*2)-1)//(p**2-1)               # Here we calculate Sigma_2
        for q in F :
            if p1*q <= lim :
                tmp.append(p1*q)
                D[q*p1] = D[q]*(p**((e+1)*2)-1)//(p**2-1)     # Calculate Sigma_2 for composites numbers
            if p1*q > lim : break
        e+=1

    F.extend(tmp)
    F.sort()
    print(F)
    print('length F :\t',len(F))

print(len(F),'\n', sorted(F)[:100])
# print('\n',D)
print(D[42])


squares = [ v for v in D.values() if gmpy2.is_square(v) ]
print('Squares : ' , len(squares), squares)
print('\nTotal Sum : ', sum(squares) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')



############# DIVISOR SQUARE SUM ,  ELEGANT &  FAST SIEVE ##############

from math import sqrt

def divisor_square_sum_sieve(n):
    sieve = [0] * (n + 1)
    limit =  int(sqrt(n)) + 1
    for i in range(1, limit):
        sieve[i * i] += i * i
        temp = i + 1
        for j in range(i * i + i, n + 1, i):
            sieve[j] += i * i + temp * temp
            temp += 1
    print(sieve)
    return sieve

divisor_square_sum_sieve(100)