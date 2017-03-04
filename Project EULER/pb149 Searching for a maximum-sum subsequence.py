#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Thu, 9 Feb 2017, 13:54
#The  Euler Project  https://projecteuler.net
'''
Searching for a maximum-sum subsequence     -       Problem 149

Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction
(horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).

                                      −2	    5	    3	    2
                                        9	  −6	    5	    1
                                        3	    2	    7	    3
                                      −1     8	  −4      8
Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007*k**3] (modulo 1000000) − 500000.
For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.

Thus, s10 = −393027 and s100 = 86613.

The terms of s are then arranged in a 2000×2000 table, using the first 2000 numbers to fill the first row (sequentially),
the next 2000 numbers to fill the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).

'''
import time
import numpy as np

# # For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007*k**3] (modulo 1000000) − 500000.
# # For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.
# L =[]
# for k in range(1,56):
#     s = ((100003 - 200003*k + 300007*k**3) % 1000000) - 500000
#     print('s'+str(k)+'.  ',s)
#     L.append(s)
#
# print(L,'\n')
# for k in range(56, 401):    # Need until 4.000.001
#     s =  (( L[-24]+L[-55] +1000000 ) % 1000000) - 500000
#     L.append(s)
#     print('s'+str(k)+'.  ',s)

def Lagged_Fibonacci_Generator_gen():           # EFFICIENT GENERATOR
    '''
    For 1 ≤ k ≤ 55, Sk = [100003 - 200003*k + 300007*k**3] (modulo 1000000) - 500000
    For 56 ≤ k, Sk = [S_(k-24) + S(k-55)] (modulo 1000000) - 500000                      '''
    tmp=[]
    for k in range(1,56) :
        s = (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
        # print(k, s)
        tmp.append(s)
        yield s
    while True :
        s = (tmp[-24]+tmp[-55])%1000000 - 500000
        tmp.append(s)
        tmp.pop(0)
        # print(len(tmp) ,tmp)
        yield s

t1  = time.time()

Test_arr = [ -3, -45, 9, 34, -87, 23, 1, -3, 99, 456, -89, 34, -45, 90, -123, 300, 9, -12, -67, 200 ]

def Kadane_algo(arr):
    ''' KADANE's Algorithm
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    '''
    max_current = max_global = arr[0]
    # start, end= 0, 1
    for i in range(len(arr)):
        # if arr[i] > max_current+arr[i] :
        #     start = i
        #     print('new start index :', start,  '     ', arr[i], max_current+arr[i])
        max_current = max (arr[i], max_current+arr[i] )
        if max_current > max_global :
            max_global = max_current
            # end = i+1
    # print('\nStart end indexes : ',start, end , '         ', arr[start:end])
    return max_global

print('\n Kadane_algo : \t', Kadane_algo(Test_arr))

# # Just to verify the Kadane's Algorithm !!
# print()
# for i in range (len(Test_arr)):
#     print(i, '    ', sum(Test_arr[i:] ))


# @ 2016-12-23, 01:33, Must find a function to calculate diagonals of custom length.
# Also when calculating rows we need to calculate them with custom length

print('\n---------------------Numpy MAIN & SEOCNDARY DIAGONALS ----------------')

v1 = list(range(1, 6))
v2 = list(range(6, 11))
v3 = list(range(11, 16))
v4 = list(range(16, 21))
v5 = list(range(21, 26))

V = []
V.append(v1) ; V.append(v2) ; V.append(v3) ; V.append(v4) ; V.append(v5) ;
V = np.array(V)
print(V,'\t\t' ,type(V),'\n')
print(np.transpose(V),'\n')

main_diags = [V.diagonal(i) for i in range(len(V)-1, -len(V),-1)]
print ('main_diags : \t', [n.tolist() for n in main_diags ] )
sec_diags = [ V[::-1,:].diagonal(i) for i in range(-len(V)+1, len(V))]
print('sec_diags :\t', [n.tolist() for n in sec_diags ] )



print('\n=============  My First Solution, Kadane Algorithm,  30 sec ====================')
t1  = time.time()

max_res = 0
T = []
def make_matrix(T):
    global max_res
    LFG = Lagged_Fibonacci_Generator_gen()
    for i in range(1, 2000 +1):
        tmp = []
        for j in range(1, 2000 +1):
            lfg = next(LFG)
            tmp.append(lfg )
        T.append(tmp)
        res = Kadane_algo(tmp)
        if res > max_res :
            max_res = res

    # print('\n',len(T), len(T[0]),T[0][10-1], T[0][100-1])
    return T

T = np.array( make_matrix(T) )
print('\n' , len(T), len(T[0]), T[0][10-1], T[0][100-1], type(T))

print('\nMAX_res Normal Matrix : \t', max_res) ; T1 = max_res

max_res = 0
T_trans = np.transpose(T)           # Transpose matrix to find COLUMNS
for i in range(len(T_trans)):
    res = Kadane_algo(T_trans[i])
    if res > max_res :
        max_res = res

print('\nMAX_res TRANSPOSED Matrix : \t', max_res ) ; T2 = max_res

def main_diags(T) :
    max_res = 0
    main_diags = [T.diagonal(i) for i in range(len(T)-1, -len(T),-1)]
    for i in range(len(main_diags)) :
        res = Kadane_algo(main_diags[i])
        if res > max_res :
            max_res = res
            # print(main_diags[i])
    # print('\nMAX_res MAIN DIAGONALS Matrix : \t', max_res)
    return max_res


def sec_diags(T) :
    max_res = 0
    sec_diags = [ T[::-1,:].diagonal(i) for i in range(-len(T)+1, len(T))]
    for i in range(len(sec_diags)) :
        res = Kadane_algo(sec_diags[i])
        if res > max_res :
            max_res = res
            # print(sec_diags[i])
    # print('\nMAX_res SECONDARY DIAGONALS Matrix : \t', max_res)
    return max_res

print('\nMAX_res MAIN DIAGONALS Matrix : \t',  main_diags(T) ) ; T3 = main_diags(T)
print('\nMAX_res SECONDARY DIAGONALS Matrix : \t',  sec_diags(T) ) ; T4 = main_diags(T)

print('\nFinal Answer : ' , max(T1, T2, T3, T4 ) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

########### GENERAL IDEA ##############
# maximum sub-array problem (Kadane's algorithm)

# print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()



# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  30 sec  --------------------------')
t1  = time.time()

# ==== Thu, 8 Dec 2016, 20:31, tking42

def series_generator():
    values = [(100003 - 200003 * k + 300007 * k * k * k) % 1000000 - 500000 for k in range(1, 56)]
    i = 0
    while True:
        yield values[i]
        values[i] = (values[i - 24] + values[i]) % 1000000 - 500000
        i = (i + 1) % 55

def p149(size=2000):
    last = [[None] * 4 for _ in range(size)]
    current = [[None] * 4 for _ in range(size)]
    series = series_generator()
    max_sum = -1000000
    for r in range(size):
        for c in range(size):
            n = next(series)
            current[c][0] = n if c == 0 else max(n, current[c - 1][0] + n)
            current[c][1] = n if r == 0 else max(n, last[c][1] + n)
            current[c][2] = n if r == 0 or c == 0 else max(n, last[c - 1][2] + n)
            current[c][3] = n if r == 0 or c == size - 1 else max(n, last[c + 1][3] + n)
            max_sum = max(max_sum, max(current[c]))
        last, current = current, last
    return max_sum

# p149()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Sat, 17 Dec 2016, 21:07, Khalid, Saudi Arabia
# This one was easy, especially that the solution turned out to be a vertical line
# (I thought I'd try first with horizontal and vertical before bothering with implementing diagonal -
# which wouldn't be much harder, but would require lots of array manipulation).
#
# The algorithm runs in 13 seconds.

import numpy as np

def g_lagged_fib():
    mem = []
    for i in range(0, 55):
        k = i + 1
        r = (100003 - 200003 * k + 300007 * k * k * k) % 1000000 - 500000
        mem.append(r)
        yield k, r
    for i in range(55, 4000000):
        k = i + 1
        s24 = mem[-24]
        s55 = mem[0]

        r = (s24 + s55 + 1000000) % 1000000 - 500000

        mem.pop(0)
        mem.append(r)
        yield k, r

lagged_fib = g_lagged_fib()

def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

matrix = []
row = None
for k, lf in lagged_fib:
    if (k - 1) % 2000 == 0:
        row = []
        matrix.append(row)
    row.append(lf)


def matrix_max_subarray(M):
    t_max = 0
    M = np.array(M)
    for row in M:
        t_max = max(t_max, max_subarray(row))
    for i in range(len(M)):
        t_max = max(t_max, max_subarray(M[:, i]))
    return t_max

print (matrix_max_subarray(matrix))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  13 sec --------------------------')
t1  = time.time()

# ==== Wed, 26 Nov 2014, 06:45, wakkadojo, USA
# Not sure what all this business is about Kadane's method, but it seemed pretty straight-forward:
# keep a max running sum count, if your current running sum is negative cut off the sequence and start counting fresh.
# The premise is if the running count since the last count is positive,
# it will always contribute to making a higher sum subsequence.
# 10s in python on an i5, would run in 50ms if I wrote it in C

def prlist (n):
    mod = 1000000
    sub = int (mod/2)
    out = [0]*n*n
    for i in range (55):
        out[i] = (100003 - 200003*(i+1) + 300007*(i+1)**3) % mod - sub
    for i in range (55, n*n):
        out[i] = (out[i-24] + out[i-55] + 1000000) % mod - sub
    return [ [out[j + n*i] for j in range (n)] for i in range (n) ]

def maxRun (s):
    runningMax = s[0]
    runningCount = 0
    for x in s:
        runningCount += x
        runningCount = 0 if runningCount < 0 else runningCount
        runningMax = runningMax if runningCount < runningMax else runningCount
    return runningMax

n = 2000
s = prlist (n)

# rows
rmax = max (maxRun (x) for x in s)
cmax = max (maxRun (x) for x in [ [s[i][j] for i in range (n) ]\
     for j in range (n) ])
diag = [ [s[j][i+j] for j in range (n-i) ] for i in range (n) ] +\
    [ [s[i+j][j] for j in range (n-i) ] for i in range (n-1, 0, -1) ]
adiag = [ [s[j][n-1-i-j] for j in range (n-i) ] for i in range (n) ] +\
    [ [s[n-j-1][i+j] for j in range (n-i) ] for i in range (n-1, 0, -1) ]
dmax = max (maxRun (x) for x in diag)
admax = max (maxRun (x) for x in adiag)
print (max (rmax, cmax, dmax, admax))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, 23 sec  --------------------------')
t1  = time.time()

# ==== Tue, 30 Dec 2014, 17:53, fioi, France

def generate_grid():
	s = [0]
	for k in range(1, 56):
		s.append((100003 - 200003 * k + 300007 * k ** 3) % 1000000 - 500000)
	for k in range(56, 4000001):
		s.append((s[k - 24] + s[k - 55] + 1000000) % 1000000 - 500000)
	return [[s[i * 2000 + j + 1] for j in range(2000)] for i in range(2000)]

def max_subsum(grid, x, y, dx, dy):
	n = len(grid[0])
	ans, cur = 0, 0
	while x < n and x >= 0 and y < n and y >= 0:
		cur = max(0, cur + grid[x][y])
		ans = max(ans, cur)
		x += dx
		y += dy
	return ans

grid = generate_grid()
n = len(grid[0])
ans = 0
for x in range(n):
	ans = max(ans, max_subsum(grid, x, 0, 0, 1))
	ans = max(ans, max_subsum(grid, 0, x, 1, 0))
	ans = max(ans, max_subsum(grid, x, 0, 1, -1))
	ans = max(ans, max_subsum(grid, x, 0, -1, 1))
print(ans)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ==== Tue, 2 Nov 2010, 08:38, Melnofil, France
# 16sec without storing the matrix

def gen():
    v = [(100003 - 200003 * k + 300007 * (k ** 3)) % 1000000 - 500000 for k in range(1, 56)]
    for i in v:
        yield i
    while True:
        v.append((v[0] + v[31] + 1000000) % 1000000 - 500000)
        yield v[55]
        del v[0]

X = [0] * 2000
Y = [0] * 2000
A = [0] * 3999
M = [0] * 3999
R = range(2000)
res = 0
g = gen()
for y in R:
    for x in R:
        n = next(g)
        a = x + y
        m = 1999 + x - y
        X[x] = max(0, X[x] + n)
        Y[y] = max(0, Y[y] + n)
        A[a] = max(0, A[a] + n)
        M[m] = max(0, M[m] + n)
        if n > 0:
            res = max(res, X[x], Y[y], A[a], M[m])
print (res)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
