#!/usr/bin/python
# Solved by Bogdan Trif @
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



print('\n=================  My First Solution ====================')
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

# print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()

















# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
