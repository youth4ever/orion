
import time


######### SMART WAY TO BUILD A SIEVE OF ADMISSIBLE NUMBERS #######
# This code build numbers like powers of consecutive primes ONLY : [2**i, 3**j, 5**k, 7**l, ..... ]
# 2,4,6,8,12, 16, 18, 24, 30 ,...
# There were some mistakes in the algorithm as it does not add 30. I corrected it !!!!

limit = 10 ** 2
adm = []

primes = [3, 5, 7, 11, 13, 17, 19, 23]

A = []
exp = 1
new = 2 ** exp
while new < limit:
    adm.append(new)
    A.append(new)
    exp += 1
    new = 2 ** exp

start = 0
stop = len(adm)
for p in primes:
    for n in range(start, stop):
        exp = 1
        new_p = p ** exp
        new = adm[n] * new_p
        while new < limit:
            adm.append(new)
            A.append(new)
            exp += 1
            new_p = p ** exp
            new = adm[n] * new_p
    start = stop        # I corrected the index here
    stop = len(adm)-1

print(A)




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

############# DIVISOR SQUARE SUM ,  ELEGANT &  FAST SIEVE ##############


def divisor_square_sum_sieve(n):
    sieve = [0] * (n + 1)
    limit =  int( n**(1/2) ) + 1
    for i in range(1, limit):
        sieve[i * i] += i * i
        temp = i + 1
        for j in range(i * i + i, n + 1, i):
            sieve[j] += i * i + temp * temp
            temp += 1
    print(sieve)
    return sieve

divisor_square_sum_sieve(100)


#############     EULER TOTIENT SIEVE FAST ALGORITHM , first variant, slower  ##############


t1  = time.time()


def primes_up_to(n):
    # http://code.activestate.com/recipes/576640/
    nroot = int( n **(1/2) )
    sieve = [True] * (n+1)# range(n+1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, nroot+1):
        if sieve[i]:
            m = n/i - i
            sieve[i*i: n+1:i] = [False] * (int(m)+1)

    return [i for i in range(n+1) if sieve[i]]

def multiple_gen(modulus):
    """Generates the list of multiples of modulus."""
    count = 1
    while True:
        yield modulus * count
        count += 1

def fast_compute_totients(bound):
    """Simultaneously compute totients for all numbers
    up to and including n."""

    # Populate the initial list with the leading factor of n.
    results = list(range(0, bound+1))

    # Get the list of primes up to the bound.
    primes = primes_up_to(bound)

    for p in primes:
        for m in multiple_gen(p):
            if m > bound:
                break
            results[m] = (results[m] // p) * (p - 1)
    return print(sum(results), '\n',results[:100])

if __name__ == '__main__':
    fast_compute_totients(10**2)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')


########  EULER TOTIENT SIEVE FAST ALGORITHM , SECOND,  2x FASTER  ##############

def Euler_Totient_Sieve(n):
    ''' Constructs a SIEVE of totients up to n
    :param n: up range number
    :return: list, totients     '''
    phi = list(range(n+1))
    for i in range(2, n+1):
        if phi[i] == i:
            for x in range(i, n+1, i):
                phi[x] -= phi[x] // i
    return phi[1:][:100]            # Take care to remove the [:100], it is only for printing

print('Euler_Totient_Sieve :\n' , Euler_Totient_Sieve(100))


#########