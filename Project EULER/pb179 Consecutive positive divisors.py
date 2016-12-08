#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                    Consecutive positive divisors       -   Problem 179

Find the number of integers 1 < n < 10**7, for which n and n + 1 have the same number of positive divisors.

For example, 14 has the positive divisors 1, 2, 7, 14   while   15 has  1, 3, 5, 15.
'''


import time
import gmpy2

class GET_DIVISORS(object):
    '''Made by Bogdan Trif @ 2016-11-15, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)

    :param nr:  int
    :return: a list with the divisors    '''

#     def __init__(self, nr):   # We don't want to initialize the class with a number
#     self.nr = nr

    def factor_pyprimes(self, nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(nr)] for val in sublist]

    def divisors(self, nr):
        from itertools import combinations
        import functools, operator, gmpy2
        if gmpy2.is_prime(nr) == True or nr == 1 :
            return [nr, 1]    # Must be adjusted to [1] if you change on list
        else :
            all_factors =  self.factor_pyprimes(nr)
            # set_factors=list(set(all_factors))
            comb= set()
            # print(all_factors)
            for i in range(1, len(all_factors)):
                c = set(combinations(all_factors, i) )
                comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
                comb_prod.sort()
        return  [nr]+comb_prod[::-1]+[1]   # sum([1]+ comb_prod)   !!!!!!!! Remember to change on  return [1]  for isprime case


def count_repetitions(lst):
    ''':Description: Counts how many consecutive occurences there are in a list
    '''
    pos = 0
    cnt=0
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            pos += 1
        if lst[i] != lst[i-1]:
            pos = 0
        # print(pos , end='  ')
        if pos == 1 : cnt +=2
        if pos == 2 or pos == 3 or pos ==4 : cnt +=1
    return cnt

print('\n--------------------------TESTS------------------------------')


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


L=[]
counter=2
up_range = 10**2
for i in range(2, up_range+1 ):
    if gmpy2.is_prime(i) == True or i == up_range :
        counter += count_repetitions(L)
        L=[]
        print(str(i)+'.   ' ,    '         Counter:'  ,counter)
    else:
        div = GET_DIVISORS().divisors(i)
        l = len(div)
        L.append(l)
        print(str(i)+'.   ' , div,'   ' , l  ,   '         Counter:'  ,counter)
    if i % 1e5 == 0 : print(i)


print('\nAnswer : ',counter)



# Tried : Answer :  1849079, ..81, ..83 , ..82, ..80, ..78, ..77, ..84, ..85,
# Tried : 986116, 986114, 986115









t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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
