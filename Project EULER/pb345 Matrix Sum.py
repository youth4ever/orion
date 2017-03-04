#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                    Matrix Sum      -       Problem 345

We define the Matrix Sum of a matrix as the maximum sum of matrix elements with each element being the only one in his row and column.
For example, the Matrix Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):

                                                              7  53 183 439 863
                                                            497 383 563  79 973
                                                            287  63 343 169 583
                                                            627 343 773 959 943
                                                            767 473 103 699 303

Find the Matrix Sum of:

                              7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
                            627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
                            447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
                            217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
                            960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
                            870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
                            973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
                            322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
                            445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
                            414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
                            184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
                            821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
                             34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
                            815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
                            813 883 451 509 615  77 281 613 459 205 380 274 302  35 805

'''
import time, heapq, itertools
from copy import deepcopy

f = open('pb345_matrix.txt', 'r')
# f = open('pb067_triangle.txt', 'r')
text = f.read()
f.close()
# Initialize and populate matrix
matrix = []
# print(text,'        ',type(text),'\n')

for row in text.split('\n'):
    matrix.append(list(map(int, row.split(' '))))         # This maps the strings into ints on the run, SMART TECHNIQUE

M = deepcopy(matrix)

# @2017-02-07
# find max on a column, then interesect with the row to confirm.
# if there as new maximum establish that maximum and go on next row.
#
# Also must keep track of already marked positions !!!


tmp = heapq.nlargest(8, M[0])
print( 'First 8  Largest elements in the list : ',heapq.nlargest(8, M[0]) )
print([ (j, M[0].index(j))   for j in  tmp ])

print('\n--------------------------TESTS------------------------------\n')
t1  = time.time()

A = []
for i in range(len(M)):
    tmp = [ ( j, M[i].index(j) ) for j in  heapq.nlargest(8, M[i]) ]

    print( M[i] , '        ' , tmp )
    A.append(tmp)

print('\n',A,'\n\n')

m = {x: 'A' + str(x) for x in range(15)}
D = {}
S_max, S = 0, 0
SEt = set()
for i in range(len(A)):
    print(A[i] )
    D[i]= A[i]

print('\n',D,'\n',D[0])

cnt, itr = 0, 0
for i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14  in itertools.product(range(1, 4+1), repeat=15):
    itr+=1
    # print(i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14)
    S = D[0][i0][0]+D[1][i1][0]+D[2][i2][0]+D[3][i3][0]+D[4][i4][0]+D[5][i5][0]+D[6][i6][0]+D[7][i7][0]+ \
            D[8][i8][0]+D[9][i9][0]+D[10][i10][0]+D[11][i11][0]+D[12][i12][0]+D[13][i13][0]+D[14][i14][0]

    SEt ={ D[0][i0][1], D[1][i1][1], D[2][i2][1], D[3][i3][1], D[4][i4][1], D[5][i5][1], D[6][i6][1], D[7][i7][1] ,
            D[8][i8][1], D[9][i9][1], D[10][i10][1], D[11][i11][1], D[12][i12][1], D[13][i13][1], D[14][i14][1] }
    # print(i0, i1, D[0][i0], D[1][i1]  ,SEt, '   ', S)
    if itr % 10**6 == 0 : print('----- iter ------', itr)
    if len(SEt) == 15 :
        if S_max < S :
            cnt+=1
            S_max = S
            print(str(cnt)+'.        ', S)

print('\nAnswer : \t', S_max )

# TRIED :       12365, 12457, 12475


# for i0, i1  in itertools.product(range(1, 3+1), repeat=2):
#     S = D[0][i0][0]+D[1][i1][0]
#     SEt ={ D[0][i0][1], D[1][i1][1]  }
#     print(i0, i1, D[0][i0], D[1][i1]  ,SEt, '   ', S)
#         if len(SEt) == 15 :
#             if S_max < S :
#                 S_max = S
#                 print(str(cnt)+'.      ', S)




# for i0 in range(len(A[0])):
#     memo = []
#     # e0 = A[0][i0]
    # memo.append(e0[1])
    #
    # A1 = [ a for a in A[1] if a[1] not in memo ]
    # # print(A1)
    # for i1 in range(len(A1)) :
    #     e1 = A1[i1]
    #     memo.append(e1[1])
    #     print(memo)
        # A2 = [ a for a in A[2] if a[1] not in memo ]
        # for i2 in range(len(A2)):
        #     e2 = A2[i2]
        #     memo.append(e2[1])
        #     print(memo,'        ' ,A1, A2)
        #









t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
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
