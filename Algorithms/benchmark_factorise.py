import pyprimes
import sympy

import random, functools, operator, time

test_nr= functools.reduce( operator.mul,  [  (random.randint(100000,500000)) for i in range(10) ] )
print(test_nr)



print('\n------------------ 1  ----------------')
t1  = time.time()


print( list( pyprimes.factorise(test_nr))  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2 ------------------')
t1  = time.time()


print( sympy.factorint(test_nr) )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################


print('\n----------- PAIR FACTORING OF A NUMBER -------------------')


def pair_Factors(n):
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                todo += (n//i, i, combi+[i]),
            i += 1
    return combis

def pair_Factors_rec(n):
    def factor(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                factor(n//i, i, combi+[i], combis)
            i += 1
        return combis
    return factor(n, 2, [], [])




# n = 16*15*49*13*27
n = 16*15*498*28

print('\n------------------ 1  ------    pair_Factors  ----------')
t1  = time.time()


print('pair_Factors_rec : ',  pair_Factors(n)  ,'\n', len(pair_Factors(n)))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2  ---   pair_Factors_rec ---------------')
t1  = time.time()


print('pair_Factors_rec : ',len(pair_Factors_rec(n))  ,'\n', pair_Factors_rec(n))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#################### #####################

