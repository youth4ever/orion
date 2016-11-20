import time
from math import sqrt

print('\n------------------ MY ALGORITHM ----------------')
t1  = time.time()

def number_partition(n):
    partitions = [1] +  [0]* n
    cons = [i for i in range(1,n+1)]
    #print([i for i in range(1,val+1)])

    for i in cons:
        for j in range (i, n+1):
            #print(i, j , partitions)
            partitions[j] +=  partitions[j - i]
    return partitions[-1]

print(number_partition(100))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n---------------OTHERS------------------')
t1  = time.time()


number = 4996


def pent(n):
    return (n * (3 * n - 1)) / 2

def dyf(num):
    if num < 0:
        return 0
    elif num in memo:
        return memo[num]
    else:
        f = 0
        for a in range(len(L)):
            f += L[a][0] * dyf(num - L[a][1])
    memo[num] = f
    return f

global L, memo
memo = {0:1}
n = 1
L = []

while True:
    sign = 1
    if n % 2 == 0:
        sign = -1
    if number - pent(n) >= 0:
        L.append((sign , pent(n)))
    else:
        break
    if number - pent(-1 * n) >= 0:
        L.append((sign , pent(-1 * n)))
    else:
        break
    n += 1
L = L[::-1]

print (dyf(number) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')