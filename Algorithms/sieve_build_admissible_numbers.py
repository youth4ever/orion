
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