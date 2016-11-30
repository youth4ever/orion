#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                                Product-sum numbers     -       Problem 88

A natural number, N, that can be written as the sum and product of a given
set of at least two natural numbers, {a[1], a[2], ... , a[k]} is called a product-sum number:
N = a[1] + a[2] + ... + a[k] = a[1] * a[2] * ... *a[k].

For example, 6 = 1 + 2 + 3 = 1 * 2 * 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

                    k=2:    4 = 2 * 2 = 2 + 2
                    k=3:    6 = 1 * 2 * 3 = 1 + 2 + 3
                    k=4:    8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
                    k=5:    8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
                    k=6:    12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12= 30;
note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12  is  {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2k12000?
'''
import time
import gmpy2
import pyprimes
from itertools import combinations
import functools, operator



def sieve(lower, upper_bound):
    ''':Description:        SIEVE OF ERATOSTHENES ALGORITHM  , SECOND FASTEST
    :param:      :lower: = lower_integer including
                     :upper_bound: = upper integer excluding
    :returns:   a list containing all primes between lower and upper bound
    :Usage:             Example:    primes = sieve(2, 100)                    '''
    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag and i > lower ]
    return primes

print(sieve(11000, 12001))

print(gmpy2.is_prime(11))
print(gmpy2.next_prime(8))



# for i in pyprimes.awful_primes():    print(i)
for i in pyprimes.nprimes(25):    print(i, end='  ')
#
# def get_divisors(nr):
#     '''Made by Bogdan Trif @ 2016-11-09, based on itertools.combinations module
#     and with a little help on list(functools.reduce(operator.mul, i) for i in comb)
#     2-4 times slower because of the factorize method. Must improve it
#     :param nr:  int
#     :return: a list with the divisors    '''
#     from itertools import combinations
#     import functools, operator
#
#     def factor_pyprimes(n):
#         ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
#         from pyprimes import factorise
#         return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
#
#     if gmpy2.is_prime(nr) == True or nr == 1 :
#         return [1]    # Must be adjusted to [1] if you change on list
#     else :
#         all_factors = factor_pyprimes(nr)
#         # set_factors=list(set(all_factors))
#         comb= set()
#         # print(all_factors)
#         for i in range(1, len(all_factors)):
#             c = set(combinations(all_factors, i) )
#             comb.update(c)
#             comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
#             comb_prod.sort()
#         return  comb_prod[::-1]   # sum([1]+ comb_prod)   !!!!!!!! Remember to change on  return [1]  for isprime case


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
            return [1]    # Must be adjusted to [1] if you change on list
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
        return  comb_prod[::-1]   # sum([1]+ comb_prod)   !!!!!!!! Remember to change on  return [1]  for isprime case


print('\nUsing the method divisors from within the class GET_DIVISORS : ', GET_DIVISORS().divisors(90) )
print('Using the method factor_pyprimes from within the class  GET_DIVISORS: ', GET_DIVISORS().factor_pyprimes(90)  )


# def product_sum_k(n):
#     ''':Description: Function which finds the **k**'s of a sum-product number
#     :Example1:  product_sum_k(15)    returns [9] because :
#
#         :k=9: :  3*5*1*1*1*1*1*1*1  = 3+5+1+1+1+1+1+1+1 = 15
#     :Example2:  product_sum_k(16)    returns [8,10] because :
#
#         :k=8: :  2*8*1*1*1*1*1*1  = 2+8+1+1+1+1+1+1 = 16
#         :k=10: :  4*4*1*1*1*1*1*1*1*1  = 4+4+1+1+1+1+1+1+1+1 = 16
#     :param: :n:   *int*, number for which *k* is calculated
#     :return:    *list* containing all the **k**'s that a number n can have
#     '''
#     div = GET_DIVISORS().divisors(n)
#     F = GET_DIVISORS().factor_pyprimes(n)
#     p =  functools.reduce(operator.mul, F)    # Taking all terms
#     ks = [ p-sum(F) + len(F) ]
#     # p = list( functools.reduce(operator.mul, i) for i in div)   # Taking all terms
#     for i in range( len(div)//2+1 ) :
#         a = n/div[i]
#         # print('a=',a, end='    ')
#         o = a* div[i] - (a+div[i])
#         # print('o=',o)
#         # if int(o+2) not in ks : ks.append( int(o+2) )
#         ks.append( int(o+2) )
#
#     def inner_terms(n):
#         kin=[]
#         F = GET_DIVISORS().factor_pyprimes(n)
#         comb=set()              # This CODE WORKS for inner cases : Ex 90 : 6 + 3 +5  ,  9 + 2+5, 10 + 3 +3
#         if len(F) > 3 :
#             for i in range(2, len(F)-1):
#                     C = set(combinations(F, i) )
#                     comb.update(C)
#                     # print(comb)
#                     # C_sum = list( functools.reduce(operator.add, i) for i in comb)
#                     C_prod = list( functools.reduce(operator.mul, i) for i in comb)
#             # print('\n',comb)
#             # print('C_sum : ',C_sum)
#             # print('C_prod : ',C_prod)
#             comb = list(comb)
#             for j in range(len(C_prod)):
#                 A = F.copy()
#                 # p1 = C_prod[j]
#                 # p2 = n/C_prod[j]
#                 for m in comb[j]: A.remove(m)
#                 # print(A)
#                 s1 = C_prod[j]
#                 s2 = sum(A)
#                 o1 = n - (s1+s2 ) + len(A) +1
#                 kin.append(o1)
#                 # print('p1=', p1 ,  '   p2=', p2,'     s1=',s1 , '    s2=',s2, '   ', o1, '  ' ,list(comb)[j] )
#             return list(set(kin))
#         else : return []
#     kin = inner_terms(n)
#     return sorted(list(set(ks+kin)))           # this is the returned k

def product_sum_k(n):
    ''':Description: Function which finds the **k**'s of a sum-product number
    :Example1:  product_sum_k(15)    returns [9] because :

        :k=9: :  3*5*1*1*1*1*1*1*1  = 3+5+1+1+1+1+1+1+1 = 15
    :Example2:  product_sum_k(16)    returns [8,10] because :

        :k=8: :  2*8*1*1*1*1*1*1  = 2+8+1+1+1+1+1+1 = 16
        :k=10: :  4*4*1*1*1*1*1*1*1*1  = 4+4+1+1+1+1+1+1+1+1 = 16
    :param: :n:   *int*, number for which *k* is calculated
    :return:    *list* containing all the **k**'s that a number n can have
    '''
    div = GET_DIVISORS().divisors(n)
    F = GET_DIVISORS().factor_pyprimes(n)
    p =  functools.reduce(operator.mul, F)    # Taking all terms
    ks = [ p-sum(F) + len(F) ]
    # p = list( functools.reduce(operator.mul, i) for i in div)   # Taking all terms
    for i in range( len(div)//2+1 ) :
        a = n/div[i]
        # print('a=',a, end='    ')
        o = a* div[i] - (a+div[i])
        # print('o=',o)
        # if int(o+2) not in ks : ks.append( int(o+2) )
        ks.append( int(o+2) )

    def inner_terms(n):
        kin=[]
        F = GET_DIVISORS().factor_pyprimes(n)
        comb=set()              # This CODE WORKS for inner cases : Ex 90 : 6 + 3 +5  ,  9 + 2+5, 10 + 3 +3
        if len(F) > 3 :
            for i in range(2, len(F)-1):
                    C = set(combinations(F, i) )
                    comb.update(C)
                    # print(comb)
                    # C_sum = list( functools.reduce(operator.add, i) for i in comb)
                    C_prod = list( functools.reduce(operator.mul, i) for i in comb)
            # print('\n',comb)
            # print('C_sum : ',C_sum)
            # print('C_prod : ',C_prod)
            comb = list(comb)
            for j in range(len(C_prod)):
                A = F.copy()
                # p1 = C_prod[j]
                # p2 = n/C_prod[j]
                for m in comb[j]: A.remove(m)
                # print(A)
                s1 = C_prod[j]
                s2 = sum(A)
                o1 = n - (s1+s2 ) + len(A) +1
                kin.append(o1)
                # print('p1=', p1 ,  '   p2=', p2,'     s1=',s1 , '    s2=',s2, '   ', o1, '  ' ,list(comb)[j] )
            return list(set(kin))
        else : return []
    kin = inner_terms(n)
    return len(list(set(ks+kin))) , sorted(list(set(ks+kin)))           # this is the returned k



print('\n------------------------ TESTS---------------------------')

# n=8100   # 10500
class GET_ALL_KEYS(object) :

    def factorize_all(self, n):
        F = GET_DIVISORS().factor_pyprimes(n)
        # print('F:  ',F,'\n')
        comb=set()
        ALL = [F]
        # THE SIMPLE TERMS
        Comb = list(combinations(F, len(F)-1 ))     # only the len(F)-1 terms
        # print(Comb )
        C_prod = list( functools.reduce(operator.mul, i ) for i in Comb)
        # print(C_prod)
        for i in C_prod :
            # print([i, n//i ], end='    ')
            ALL.append([i , n//i])
        ######   INNER TERMS      <= 2 and < len(F)-1   ######
        for i in range(2, len(F)-1):                       # If you don't want the last element of the list :     range(len(A))
            for j in  range(1, len(F)+1) :
                Comb = list(combinations(F[0:j],i))
            # print(i,' combinations')
            C_prod = list( functools.reduce(operator.mul, i ) for i in Comb)
            # print(C_prod)
            for k in range(len(Comb)) :                         # FIRST PAIR
                G = F.copy()
                for m in Comb[k]:   G.remove(m)
                H = G.copy()
                ALL.append([C_prod[k],  functools.reduce(operator.mul, H)] )
                G.insert(0, C_prod[k])
                ALL.append(G)
                # print('  G:' , G , '  H:',H,  end = '         ')
                if len(H) > 2 :                                             # SECOND PAIR
                    for n in range(2, len(H)) :
                        Comb2 = list(combinations(H , n))
                        C_prod2 = list( functools.reduce(operator.mul, i ) for i in Comb2)
                        # print('Comb2: ',Comb2, '  C_prod2:  ',C_prod2)
                        for o in range(len(Comb2)) :
                            I = H.copy()
                            for a in Comb2[o]:   I.remove(a)
                            J = I.copy()
                            # print(J )
                            ALL.append([C_prod[k] , C_prod2[o],  functools.reduce(operator.mul, J)] )
                            I = [C_prod[k] , C_prod2[o] ] +I
                            ALL.append(I)
                            # print( '  H:' ,H , '  I:',I , end='  ')
                            if len(J) > 2 :                                     # THIRD PAIR
                                for p in range(2, len(J)) :
                                    Comb3 = list(combinations(J , p))
                                    C_prod3 = list( functools.reduce(operator.mul, i ) for i in Comb3)
                                    # print('Comb3: ',Comb3, '  C_prod3:  ',C_prod3)
                                    for q in range(len(Comb3)) :
                                        K= J.copy()
                                        for a in Comb3[q]:   K.remove(a)
                                        L = K.copy()
                                        ALL.append([C_prod[k] , C_prod2[o], C_prod3[q] , functools.reduce(operator.mul, L)] )
                                        K = [ C_prod[k] ,C_prod2[o], C_prod3[q] ] + K
                                        ALL.append(K)
                                        # print( '  J:' ,J , '  K:',K , end='  ')
                                        if len(L) > 2 :                                     # FOURTH PAIR
                                            for r in range(2, len(L)) :
                                                Comb4 = list(combinations(L , r))
                                                C_prod4 = list( functools.reduce(operator.mul, i ) for i in Comb4)
                                                # print('Comb4: ',Comb4, '  C_prod4:  ',C_prod4)
                                                for s in range(len(Comb4)) :
                                                    M = L.copy()
                                                    for a in Comb4[s]:   M.remove(a)
                                                    N = M.copy()
                                                    ALL.append([C_prod[k] , C_prod2[o], C_prod3[q] , C_prod4[s] , functools.reduce(operator.mul, N)] )
                                                    M = [ C_prod[k] ,C_prod2[o], C_prod3[q], C_prod4[s] ] + M
                                                    ALL.append(M)
                                                    # print( '  L:' ,L , '  M:',M , end='  ')
        return ALL

    def compute_keys(self, n) :
        KEYS = []
        ALL = self.factorize_all(n)
        for i in range(len(ALL)):
            suma =  functools.reduce(operator.add, ALL[i] )
            k = n - suma + len(ALL[i])
            # print(suma, '       ', len(ALL[i]) ,ALL[i] , '      ' ,k)
            KEYS.append(k)
        KEYS = sorted(list(set(KEYS)))
        return KEYS

# ALL = FACTORIZE_ALL(n=8100)
#
# print('\n\nALL List containing all the possible factorizations : \n', len(ALL), ALL)


# print('\n\ncompute_keys Function Test : ',compute_keys(n=8100))

# print('--------------  CHECK  ----------------')
# C_sum = list( functools.reduce(operator.mul, i) for i in Comb)

# for i in range(len(ALL)) :
#     prod =  functools.reduce(operator.mul, ALL[i] )
#     print(prod, end='  ')

print('\n------------- TESTING THE CLASS -------------')

#     C = set(combinations(F, i) )
#     comb.update(C)
#     # print(comb)
#     C_sum = list( functools.reduce(operator.add, i) for i in comb)
#     C_prod = list( functools.reduce(operator.mul, i) for i in comb)
# print(comb)
# print('C_sum : ',C_sum)
# print('C_prod : ',C_prod,'\n')
# comb = list(comb)
# print(comb)
# for j in range(len(C_prod)):
#     A = F.copy()
#     p = C_prod[j]
#     for m in comb[j]:
#         A.remove(m)
#     print(A, end='          ')
#     s = sum(A)
#     sp= sum(list(comb)[j])
#     o = n - (p +s ) + len(A) +1
#     K.append(o)
#     print( list(comb)[j]   , '       p=', p , ' ,    A=' ,A  , ', s=' , s , ' ,  sp=' , sp ,'       k=', o  ,'\n')
#
# # p =  functools.reduce(operator.mul, F)    # Taking all terms
# # single = [ p-sum(F) + len(F) ]
# print( len(list(set(K))) ,sorted(list(set(K))))

print('Class Test Method factorize_all : ', GET_ALL_KEYS().factorize_all(420) )

print('Class Test Method compute_keys: ', GET_ALL_KEYS().compute_keys(420) )
print('Class Test Method factorize_all : ', GET_ALL_KEYS().factorize_all(128) )

t1  = time.time()

print('Class Test Method compute_keys: ', GET_ALL_KEYS().compute_keys(512) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
print('\nproduct_sum_k  Function Test :    \n',product_sum_k(420))

# I still don;t have all the terms !!!!!!!!!! This is the real problem
#
# def inner_terms(n):             # This CODE WORKS for inner cases : Ex 90 : 6 + 3 +5  ,  9 + 2+5, 10 + 3 +3
#     kin, C_prod = [], []
#     F = GET_DIVISORS().factor_pyprimes(n)
#     # print(F)
#     comb=set()
#     if len(F) > 3 :
#         for i in range(2, len(F)-1):
#                 C = set(combinations(F, i) )
#                 comb.update(C)
#                 # print(comb)
#                 # C_sum = list( functools.reduce(operator.add, i) for i in comb)
#                 C_prod = list( functools.reduce(operator.mul, i) for i in comb)
#         print('\n',comb)
#         # print('C_sum : ',C_sum)
#         print('C_prod : ',C_prod)
#         comb = list(comb)
#         for j in range(len(C_prod)):
#             A = F.copy()
#             p1 = C_prod[j]
#             p2 = n/C_prod[j]
#             for m in comb[j]: A.remove(m)
#             # print(A)
#             s1 = C_prod[j]
#             s2 = sum(A)
#             o1 = n - (s1+s2 ) + len(A) +1
#             kin.append(o1)
#             # print('p1=', p1 ,  '   p2=', p2,'     s1=',s1 , '    s2=',s2, '   ', o1, '  ' ,list(comb)[j] )
#         return list(set(kin))
#
#     else :
#         return []
#
# # print('\nInner terms function test : ' , inner_terms(90))
# print('\nInner terms function test : ' , inner_terms(8))
# print('\nInner terms function test : ' , inner_terms(23400))

print('\n----------------------')


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


# n=2310
def unique_factors(n):
    G=[]
    F = GET_DIVISORS().factor_pyprimes(n)
    for i in partitions(len(F)):
        print(i)
        # prod = list( functools.reduce(operator.mul, i ) for i in F[])
        # functools.reduce( operator.mul ,F)

    return F

I left here to fix the partition function to not show the last single number . FUCKING SHIT !!!!!!!!!!!!!

print('\nTesting the unique_factors Function : ', unique_factors(64))
print('Class Test Method factorize_all : ', GET_DIVISORS().divisors(512) )



# for i in range(1, len(F)+1):
#     comb=set()
#     C = set(combinations(F , i))
#     print(set(combinations(F , i)) , end='   ' )
#     for j in range(len(C)) :
#         # print()
#         comb_sum = list(functools.reduce(operator.add, j) for j in C)


# print('\nfactor_pyprimes Test :        ', GET_DIVISORS().factor_pyprimes(23400) )
# print('\nfactor_pyprimes Test :        ', GET_DIVISORS().factor_pyprimes(90) )
# print('\nproduct_sum_k  Function Test :    ',product_sum_k(630))
# print('\nproduct_sum_k  Function Test :    ',product_sum_k(16))
# print('\nproduct_sum_k  Function Test :    ', product_sum_k(8))
# print('product_sum_k  Function Test :    ',product_sum_k(15))
# print('product_sum_k  Function Test :    ',product_sum_k(12))
# print('product_sum_k  Function Test :    ',product_sum_k(32))

# nr=22428
# print('\nfactor_pyprimes Test  of ',n , ' :        ', GET_DIVISORS().factor_pyprimes(nr) )
# print('\n divisors Function Test of ', n, ' :        ', GET_DIVISORS().divisors(nr ) )
# print('\nproduct_sum_k  Function Test of ', n,' :    ',product_sum_k(nr ))
















print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()




def pb_088(up_range):
    BIG_K={}
    for i in range(4, up_range+1):      # up_range = 23400
        if gmpy2.is_prime(i) == False :
            p_s = GET_ALL_KEYS().compute_keys(i)
            print( 'P-S: ', i, '       key: ', p_s )
            for k in p_s :
                # k_min = min(product_sum_k(i))
                if k not in BIG_K and k <=12000 :   #12000
                    BIG_K[k] = i
                # if k_min < k :
                #     BIG_K[k_min] = i
                # print('-> EVOLUTION :   key ',k, '     P-S: ', i)
            #         if k < BIG_K[k]:
            #             BIG_K[k] = i
    return BIG_K

# BIG_K  = pb_088(up_range = 12000 )        # 23400
# BIG_K = dict(zip(BIG_K.values(), BIG_K.keys()))     # Reverse the dictionary keys <=> values
# print('\nThe BIG_K Dictionary ', len(BIG_K) ,   BIG_K )     #  !!!  len(BIG_K)  = 11999 for a correct answer, up_range=23500  !!!
# print('\nAnswer:  ', sum(set([ v for v in BIG_K.values() ] ) ),'\n')
# print('\nThe Set of P-S obtained : ', sorted(list(set([ v for v in BIG_K.values() ] ) )),'\n')
# print('Max value in set' ,max(set([ v for v in BIG_K.values() ] ) ),'\n')
#
# print('\nFinal Checks :   \nObtained here : ',sum([i for i in BIG_K.keys()]), '\nReal keys sum that should be : ', (12000*12001/2)-1 )

#        LOG
# 2016-11-16, 18:00 # One day full worked, not succedeed. TO DO: Must identify the problem of :
# product_sum_k(63) and many others. It does not add to P-S 63 the correct value 41 which is the minimum. There are
# two keys k=49 : 63 & k=53 : 63 but not 41. k=41 corresponds to a different P-S k=41:48.
# Actually P-S 63 should not exist because the lowest key k=41 has already a value associated P-S 48. THIS IS THE PROBLEM !!!!
# 2016-11-19, 14:00 --> Still no success !

# print( set([ v for v in BIG_K.values() ])   )

# Tried : 18175719

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



















# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()