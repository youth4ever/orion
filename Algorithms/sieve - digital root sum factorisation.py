import time

t1  = time.time()


# ==== Tue, 26 Mar 2013, 14:16, tom.wheldon, England
# Similar to quite a few others - uses a sieve to store a list of divisors up to √n for each n,
# then steps through again to calculate the mdrs for each n using the divisor list
# and the values already calculated.  Runs in under 7s in Python.

N = 100000

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