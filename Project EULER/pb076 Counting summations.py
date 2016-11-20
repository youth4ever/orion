#!/usr/bin/python3
# Solved by Bogdan Trif @   Completed on Mon, 17 Oct 2016, 00:19
#The  Euler Project  https://projecteuler.net
'''
                                                Counting summations     -       Problem 76
It is possible to write five as a sum in exactly six different ways:
                                                                4 + 1
                                                                3 + 2
                                                                3 + 1 + 1
                                                                2 + 2 + 1
                                                                2 + 1 + 1 + 1
                                                                1 + 1 + 1 + 1 + 1
How many different ways can one hundred be written as a sum of at least two positive integers?
'''
#       TEST VALUES :
# 1, 1, 2, 3, 5, 7, 11, 15, 22, 30,         0:9
# 42, 56, 77, 101, 135, 176, 231, 297, 385, 490,        10:19
# 627, 792, 1002, 1255, 1575, 1958, 2436, 3010, 3718, 4565,         20:29
# 5604, 6842, 8349, 10143, 12310, 14883, 17977, 21637, 26015, 31185,        30:39
# 37338, 44583, 53174, 63261, 75175, 89134, 105558, 124754, 147273, 173525      40:49
import time

def coins(value=5):
        #value = 5
        coins = [1,2,5,10,20,50,100,200]

        ways = [1] +[0]*value
        ways[0] = 1
        print(ways)

        while coins[-1] > value  :
            del(coins[-1])

        for i in range(len(coins)) :
            for j in range(coins[i], value+1):
                #print(i,j, end=' ;  ')
                ways[j] += ways[ j - coins[i] ]
                #print(ways)
        print(ways[-1])

coins(5)

total = 5
combinations = [1] + [0]*total
monies = [1,2,5,10,20,50,100,200]

for x in monies:
	for i in range(x, total+1):
		combinations[i] += combinations[i-x]

print (combinations[total])

print('\n--------------------------NUMBER PARTITION RECURSIVE FUNCTION')
def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
            #print(answer)
    return answer

print(partition(4))




val = 20
partitions = [1] +  [0]* val
cons = [i for i in range(1,val+1)]
#print([i for i in range(1,val+1)])

for i in cons:
    for j in range (i, val+1):
        #print(i, j , partitions)
        partitions[j] +=  partitions[j - i]


print('\n',partitions)
print(partitions[-1])


####################################
print('\n----------------MY OWN SOLUTION, with Ideas taken from Coin Partitions - Pb031 Coins Sums -------------------------')
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

print('\nOur desired Result  : ',number_partition(100)-1)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 ,  froycard , Venezuela --------------------------')

def euler76(z):
    p = [1]+[0]*z
    for c in range(z+1):
        for x in range(c,z+1):
            p[x] += p[x-c]
            #print(p)
    return p[z]//2-1
n=10
print(euler76(n))




print('\n--------------------------SOLUTION 2 , RECURSION  sadraddini , USA --------------------------')
# The answer is equivalent to the number of solutions of the equation :
# nx_n + (n−1)x_(n−1) + ... + x_1=n      , where x's are integers.
# This can be recursively programmed. I also use a dictionary to memorize the recursion. Takes 0.62 seconds in Python.

Q={}
def q(a,n):
    if (a,n) in Q.keys():
        return Q[(a,n)]
    else:
        A=a
        if n==1 or a==1:
            return 1
        elif a==0:
            return 1
        else:
            sum=0
            while a>=0:
                sum+=q(a,n-1)
                a-=n
            Q[(A,n)]=sum
            return sum

print (q(100,100)-1)


print('\n--------------------------SOLUTION 3 , RECURSION with MEMOIZATION, VERY FAST utkarsh_23 , India --------------------------')

def change(n,tup):
    if n < 0:
        return 0
    elif n == 0 or tup == (1,):
        return 1
    elif (n,tup) in D:
        return D[(n,tup)]
    else:
        f = change(n - tup[0],tup) + change(n,tup[1:])
    D[(n,tup)] = f
    return f
global D
D = {}
print (change(100,tuple(range(99,0,-1))) )

print('\n--------------------------SOLUTION 4 ,  THE FASTEST, VERY FAST utkarsh_23 , India --------------------------')
# Using this relation:
# p(n)=∑(−1)**k−1 * p(n−g_k) , where g_k is the k-th pentagonal number
# Refer to this article: Relation with partitions, https://en.wikipedia.org/wiki/Pentagonal_number_theorem#Relation_with_partitions
# A very efficient code using dynamic programming..

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
global L,memo
memo = {0:1}
number = 100
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

print (dyf(number) - 1)


print('\n--------------------------SOLUTION 5 , 2D MATRIX, INTERESTING   robsimpson , England --------------------------')
# I investigated the sequence with smaller numbers and found a summation series.
#
# I used a 2 x 2 matrix to store the values to sum.

n=10
matrix = [[0 for i in range(n + 1)] for j in range(n + 1)]
matrix[0][n] = 1
matrix[1][1] = 1

for i in range(2, n + 1):
    for j in range(1, i + 1):
        matrix[i][j] = sum(matrix[i - j][j:])

print (sum(matrix[n]) - 1)



print('\n--------------SOLUTION 6 , 1 ROW MATRIX, ITERATION , THE SIMPLEST CODE, SLOWER THAN MINE,  kenkamau , Kenya --------------------------')


ways = [0] * 101
ways[0] = 1

for i in range (1,100):
    for j in range(i, 101):
        ways[j] = ways[j] + ways[j - i]

print(ways[100])

print('\n--------------------------SOLUTION 7 , 1 ROW MATRIX, ITERATION ,   wakemecn , China --------------------------')
# It is the same solution for coins sum question. https://projecteuler.net/problem=31
limit = 100
matrix = list()
for i in range(limit+1):
    matrix.append([0] * limit)
matrix[0] = [0] + [1] * (limit-1)

# matrix[i][j] reprents that how to sum to i by using number <= j
for i in range(1, limit + 1):
    matrix[i][1] = 1
    for j in range(2, limit):
        cnt = 0
        ti = i
        while ti >= 0:
            cnt += matrix[ti][j-1]
            ti -= j
        matrix[i][j] = cnt

print (matrix[limit][limit-1])


print('\n--------------------------SOLUTION 8 , 1 ROW MATRIX, COMPLICATED RECURSION with MEMOIZATION ,   mbh038 , England --------------------------')
# I tried this using the partition recursion formula, and it zips through in about 4 μμs for n=100.
# Notice that I only sum kk to n√n, since the arguments to the partition functions within the main line of code
# will be negative, and hence return zero, beyond about that point.
from math import sqrt

def pb76(n,memo={}):
    if n<0:
        return 0
    if n==0:
        return 1
    try:
        return memo[n]
    except:
        result=sum([(-1)**(k-1)*(pb76(n-k*(3*k-1)//2, memo)+pb76(n-k*(3*k+1)//2,memo) ) for k in range(1,int(sqrt(n))+1)])
        memo[n]=result
        return result

n=100
print(pb76(n)-1)

# Without memoization, this already takes several seconds for n=25.
# As posted, the code even does p(10000) in 25 μμs, when the kernel doesn't die, '
# which it seems to do as I try to adapt this code for Problem 78. The default recursion limit in Python is 1000,
# which is a bit of a stumbling block. I can set it to a higher value, but the consensus seems to be that that is a bad idea.
# So what to do?


print('\n--------------------------SOLUTION 12 , RECURSION without MEMOIZATION, VERY SLOW wangzhenassd , Germany --------------------------')


s = 0

def get_factor(n,n2 = 10):
    global s
    for item in range(min(n,n2),0,-1):
        if n-item > 0:
            get_factor(n-item,item)
        elif n - item == 0:
            s += 1

if __name__ == "__main__":
    get_factor(10)
    print(s-1)