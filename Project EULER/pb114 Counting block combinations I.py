#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Counting block combinations I       -       Problem 114

A row measuring seven units in length has red blocks with a minimum length of three units placed on it,
such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.
There are exactly 17 ways of doing this.

How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility,
in general it is permitted to mix block sizes.
For example, on a row measuring 8 units in length you could use red (3), black (1), and red (4).

'''
import time
import gmpy2

def partitions(n):
    '''     Taken from http://code.activestate.com/recipes/218332-generator-for-integer-partitions/
            Created by David Eppstein on Wed, 27 Aug 2003
    :What it is:    A generator of number partition
    :Usage:     Example:    for i in partitions(5):    print(i)
    :param n:   the number you want the partitions
    :return:    set of lists with all the possible combinations                                                 '''
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]

def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
    :Usage: list(unique_permutations([1,1,1,3]))
    :param lst: type list
    :return:    a list of lists containing all the permutations
    '''
    if len(lst) == 1:
        yield (lst[0],)
    else:
        unique_lst = set(lst)
        for first_element in unique_lst:
            remaining_lst = list(lst)
            remaining_lst.remove(first_element)
            for sub_permutation in unique_permutations(remaining_lst):
                yield (first_element,) + sub_permutation

print('\n--------------------------TESTS------------------------------')
# Here we need to use partitioning of numbers and get for
# a number of lengths length of >1 a  (number) -1 of length of 1
#     +
# the one which don't have length
#

# print(list(unique_permutations([1,1,1,3])))

print('\n----------TEST for VALID rods---------')
test = [ 1, 1, 1, 4, 3, 5]
def valid_rods_old(lst):
    lst = list(unique_permutations(lst))
    # print( len(lst), lst)
    l = len(lst[0])
    B = lst.copy()
    for i in range(len(lst)):
        for j in range(l-1):
            if  lst[i][j:j+2].count(1) == 0 :
                # print(lst[i])
                try : B.remove(lst[i])
                except : AttributeError
    return len(B)

print('\nTest for the valid_rods() Function :\t', valid_rods_old(test))

print('\n---------------MORE MECHANIC (MANUAL ) TESTING ----------------')

# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]  #	   1-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3]  #	   2-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 3, 5]         #     3-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 3, 4] 	                #     4-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3]             #     5-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3]         #     6-case
# L = [1, 1, 1, 1, 1, 3  4, 5, 6, 6]                                       #     custom case  three == one
# L = [1, 1, 1, 1,  3,  4, 5, 6, 6]                                       #     custom case  threes = ones + 1
L =  [1, 1, 1, 1, 1, 1, 1, 1, 3, 3]
# @ 2016-12-05, 20:00
# Am ramas ca trebuie sa fixez functia de recursie pentru cazurile >= 3

print( len(L), L)

threes = [i for i in L if i >= 3]
threes_nr = len(threes)
ones = L.count(1)
print('Threes :',threes, len(threes), '\t \tOnes :' ,ones,  )
M = list(unique_permutations(threes))
print(len(M), M)
S=0
if len(threes) == 1 :
    print(' ========== CASE 1 ============')
    print('\nAnswer', len(L))
if len(threes) == 2 :
    print(' ========== CASE 2 ============')
    S = ones*(ones+1)/2
    f = len(list(unique_permutations(threes)))
    print('\nAnswer', int(S*f)  )

if len(threes) == 3  :
    print(' ========== CASE 3 ============')
    for i in range(1, ones):
        S += i*(i+1)/2
        print( i*(i+1)/2, '      total: ', S)
    print('\nResult:\t', S*len(M))

if len(threes) == 4:
    print(' ========== CASE 4 ============')
    for i in range(1, ones):
        s=0
        for j in range(1, i):
            s += j*(j+1)/2
        S+=s
        print(i, '       partial: ', s)
    print('\nAnswer:\t',S)

if len(threes) == 5:
    print(' ========== CASE 5 ============')
    for i in range(1, ones):
        ss =0
        for j in range(1, i):
            s = 0
            for k in range(1, j):
                s += k*(k+1)/2
            ss += s
        print(i,  '        partial:  ',ss)
        S+=ss

        # print('||||')
    print('\nAnswer:\t',S)

print('\n--------COMPARATION TEST-----------')

S = valid_rods_old(L)
print('\nTRUE RESULT :\t', S)


print('\n------------------ BUILDING THE FUNCTION  -------------------')

class GET_ROD_VARIATIONS(object):
    ''':Description: depends on the unique_permutations function.
            *Made by Bogdan Trif @ 2016-12-06, 22:00*
    :param lst: the list to analyze
    :return: int, the final number of available configurations
    '''
    def __init__( self, lst ):
        self.lst = lst
        self.threes = [i for i in self.lst if i >= 3]
        self.threes_nr = len(self.threes)
        self.ones = self.lst.count(1)
        self.mark = 0
        self.M = []
        self.N = list(unique_permutations(self.threes ))
        self.up_range = len(self.lst)-2*(threes_nr-1)+1

    def get_multiplier(self) :
        return len(self.N)

    def count_unique_perm(self, ones, threes_nr ) :
        ''':Description: Recursion Function to count blocks separated by one tile.
        :param ones: int , the number of ones from the list
        :param threes_nr: int, numbers of threes(numbers >= 3 in the list)
        :return: int, the number of possible configurations
        '''
        tmp = []

        if self.threes_nr > 2 :
            self.threes_nr = self.threes_nr-1
            self.count_unique_perm(  self.ones , self.threes_nr )
            self.mark+=1
            for j in range(1, self.up_range):
                tmp.append( sum( self.M[self.mark-1][0:j] ) )
            self.M.append(tmp)
            # print(self.M)

        elif self.threes_nr == 2 :
            for i in range(1, self.up_range):
                tmp.append(i)
            self.M.append(tmp)
            # print(self.M)

        return sum(self.M[self.mark])

    def get_result(self):
        if self.threes_nr == 1 : return len(self.lst)
        if self.threes_nr -1 == self.ones :  return (1* self.get_multiplier() )
        if self.threes_nr  == self.ones :  return ( (self.ones +1 )* self.get_multiplier() )
        if self.threes_nr  == 0 :  return 1
        if self.ones  == 0 :  return 1

        else :
            return self.count_unique_perm(self.ones, self.threes_nr) * self.get_multiplier()


# # print('\n CLASS get_multiplier TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).get_multiplier() )
# print('CLASS TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).threes_nr )
# print('CLASS TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).ones )
# # print('CLASS count_unique_perm TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).count_unique_perm(ones, threes) )
print('\nCLASS get_result TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).get_result() )

print('\n\n------------------- INITIAL SOLUTION -----------------------')

# INITIAL SOLUTION


def slow_count_block_combinations(rod_length) :
    cnt = 0
    for I in partitions(rod_length):
        # if len(I) == 1  :
        #     print(I)
        if I.count(2) == 0 :
            ones = I.count(1)
            threes = len([ i for i in I if i>=3 ])
            if  threes <= ones +1 :
                v = valid_rods_old(I)
                print(v,'\t', I)
                cnt += v
    return print('\nAnswer : ', cnt)

slow_count_block_combinations(13)

print('\n---------------------CLASS BENCH TESTING ---------')
H =   [1, 1, 1, 1, 1, 1, 1, 1, 3, 3]
print('CLASS  GET_ROD_VARIATIONS, threes_nr : ',GET_ROD_VARIATIONS(H).threes_nr )
print('CLASS  GET_ROD_VARIATIONS, ones : ',GET_ROD_VARIATIONS(H).ones )
print('\nCLASS get_result TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(H).get_result() )


print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()


def count_block_combinations(rod_length) :
    cnt = 0
    for K in partitions(rod_length):
        if K.count(2) == 0 :
            ones = K.count(1)
            threes_nr = len([ i for i in K if i>=3 ])
            if  threes_nr <= ones +1 :
                beta = GET_ROD_VARIATIONS(K).get_result()
                print(beta,'\t', K)
                cnt += beta
    return print('\nAnswer : ', cnt)

count_block_combinations(13)

I have an error in the class and I must find it !!!!










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
