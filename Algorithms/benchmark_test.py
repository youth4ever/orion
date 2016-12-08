import time


def primes_upto(k):
    is_prime = [True] * int(k+1)
    is_prime[0] = is_prime[1] = False
    for n in (n for n, prime in enumerate(is_prime) if prime):
        yield n
        if n*n > k: continue
        is_prime[n::n] = [False] * int(k/n)




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


######################################

t1  = time.time()

primes = set(primes_upto(10**7))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

############################

t1  = time.time()

primes = prime_generator(10**7)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

###############################

print('\n\n==============      ================')

t1  = time.time()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

###############################


t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')
