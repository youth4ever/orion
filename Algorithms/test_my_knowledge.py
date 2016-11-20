import time

def sieve(lower, upper_bound):         # THE FASTEST  SIEVE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # SIEVE OF ERATOSTHENES
    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag and i > lower ]
    return primes


def isprime_test(n):
    if n == 1:
        return False
    # if n in [3, 5, 7, 11, 13, 17, 19]:
    #     return True
    # if not n % 3:     return False
    # if not n % 5:        return False
    # if not n % 7:        return False
    # if not n % 11:        return False
    # if not n % 13:        return False
    # if not n % 17:        return False
    # if not n % 19:        return False

    for i in range(2, int((n**0.5)+1)):
        if not n % i:
            return False
    return True


def is_prime(x):        ## justify whether an x is prime
    for n in range(2, int((x**0.5)+1)):
        if x%n == 0:
            return 0
    return 1


t1  = time.time()
print('Generate primes')
primes = sieve(2,10000200)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

def is_prime2(num):
    root = int((num)**0.5 + 1)
    for i in primes:
        if i > root:
            break
        if num % i == 0:
            return False
    return True



print(sieve(10000000,10000100))

###########################




t1  = time.time()
print(is_prime(100000980001501))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


t1  = time.time()

print(isprime_test(100000980001501))           # Completed in : 3336.190327 ms

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

t1  = time.time()

print(is_prime2(100000980001501))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

