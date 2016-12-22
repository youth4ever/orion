#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Exploring Pascal's triangle     -       Problem 148

We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:


                                                                1
                                                            1     1
                                                         1     2     1
                                                      1     3     3     1
                                                   1     4     6     4     1
                                                1     5    10   10    5     1
                                            1     6    15    20    15    6    1
                                         1     7   21    35    35    21   7     1


However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one billion (10**9) rows of Pascal's triangle.


'''

import copy
import time, math
from pyprimes import factorise

def prime_generator(lower, upper):      ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]


def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def generate_Pascal_Triangle(row_nr) :
    '''**©** Made by Bogdan Trif @ 2016-12-20, 21:20.

        :Description: Generates the Pascal Triangle , Binomial Coefficients
        :param row_nr: int, the row number, int
        :return: nested list, matrix in the form of Pascal's Triangle       '''
    blueprint = [1]*(row_nr+1)
    Pascal= [blueprint]
    for i in range(row_nr) :
        tmp=[]
        for j in range(0, row_nr-i) :
            tmp.append(sum(Pascal[-1][0:j+1]) )
        # print(tmp)
        Pascal.append(tmp)
    return Pascal


def non_sevens_mechanically(row_nr):
    Pascal = generate_Pascal_Triangle(row_nr-1)
    cnt = 0
    L = [val for sublist in Pascal for val in sublist]
    for n in L:
        if n %7 != 0 :
            cnt+= 1
    return print('Number of NON-Se7ens :\t',cnt)




print('\n--------------------------TESTS------------------------------')

print( 'Math Log 7 Test : \t' , math.log(1000, 7 ))
print( 'Math Modulo 343 Test : \t' , 1000%343   )
print('\n--------------------------TESTS------------------------------')


row_nr = 13

print('\nTest for the function non_sevens_mechanically : ' ) ; non_sevens_mechanically(row_nr)
# t1  = time.time()
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1),6), 's')

#### MECHANICAL COUNT FUNCTION CONSTRUCTION
# row_nr =  1000
# Pasc = generate_Pascal_Triangle(row_nr-1)
#
# # for i in range(len(Pasc)) :
# #     print(Pasc[i] )
#
# Se7en = copy.deepcopy(Pasc)
#
# for i in range(len(Se7en)):
#     for j in range(len(Se7en[i])):
#         if (Se7en[i][j]) %7 == 0 :
#             Se7en[i][j] = 7
#         else : Se7en[i][j] = 0
#
#
# # filename = "pb150 blueprint.txt"
# # f = open(filename, "w")
# # for i in range(len(Se7en)) :
#     # f.write( str( Se7en[i])+'\n' )
#     # print(Se7en[i] )
#
# L = [val for sublist in Pasc for val in sublist]
# # print(L, sum(L),'\n')
#
# cnt = 0
# for n in L:
#     if n %7 != 0 :
#         cnt+= 1
#         # print(n, end=' ,  ' )
# print('\nNumber of NON-Sevens :\t',cnt)

def get_non_sevens(row_nr) :
    memo = {}
    ml = math.log(row_nr, 7)
    iml = math.floor(math.log(row_nr, 7))
    if ml <= 1 :
        return (row_nr*(row_nr+1))//2
    elif ml > 1 :
        a = row_nr // (7**iml)
        b = row_nr%(7**iml)
        A = (a*(a+1)//2)* get_non_sevens(row_nr- b)
        B = (a+1) * get_non_sevens(b)
        return A+B


print('\n MAIN TEST for the Function get_non_sevens :\t', get_non_sevens(row_nr))


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
