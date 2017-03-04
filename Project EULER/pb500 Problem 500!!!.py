#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Problem 500!!!      -       Problem 500

The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.

Find the smallest number with 2**500500 divisors.
Give your answer modulo 500500507.


'''
import time
import functools, operator

def sieve(n):       # SECOND FASTEST
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

from pyprimes import factorise
def factors(nr):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [i for i in factorise(nr)]

def  calculate_divisors(nr):
    '''**©** Made by Bogdan Trif @ 2016-12-08, 16:30.
        :Description: Functions which computes the number of divisors of a number.
                It uses the Numbers of Divisors Theorem :which says : if N=a**x*b**y*c**z => divisors_nr=(x+1)(y+1)(z+1)
            Example: N = 216 = 2**3 * 3**3 => divisors_nr = (3+1)(3+1) = 16
    :param nr: int, nr
    :return: int, divisors_number                   '''
    import functools, operator
    from pyprimes import factorise
    def factors(nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        return [i for i in factorise(nr)]
    N = factors(nr)
    return  functools.reduce( operator.mul , [ (i[1]+1) for i in N ])

n = 2**1 * 3**1 * 5**1 * 7**1 * 11**1
print('calculate_divisors : \t',n ,calculate_divisors(n ))
n = 2**3 * 3**3 * 5**1   #* 7 * 11
print('calculate_divisors : \t',n  ,calculate_divisors(n ))
n = 2**3 * 3**3 * 5**1
print('calculate_divisors : \t',n ,calculate_divisors(n ))

n =  2**3*3*1*5**1
print('\ncalculate_divisors : \t', n ,'    ',calculate_divisors(n))



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

primes = sieve(10**3)
print(len(primes), primes[:100] )

Prim=[]
divisors = 10

for p in primes[:divisors+1] :
    Prim.append( [p,1] )

Prim.pop()

print('\nThe list : \t', Prim)

for i in range(len(Prim)-2, -1, -1) :
    # print ( Prim[i] )
    n , k = Prim[i][0], Prim[i][1]
    if n**(k+1) < Prim[-1][0]** Prim[-1][1] :
        j, e = 1, 1
        print('init :   ',n,j)
        print( 'check' ,n, j+2**(e+1)-1, j+2**(e+1) )
        A = Prim[:]
        last_index = len(Prim)-1
        while n**(2**e ) < Prim[last_index][0]** Prim[last_index][1] :
            print('comparison : ',n**(2**e ) ,  Prim[last_index][0]** Prim[last_index][1]  )
        # while n**(j ) < Prim[-1][0]** Prim[-1][1] :

            j+=2**e
            e+=1
            print(e, j, n,      '    test : ', n**j, '     target :',Prim[-1][0]** Prim[-1][1] )
            # if n**j < Prim[-1][0]** Prim[-1][1] :
            Prim[i].pop(1)
            Prim[i].append(j)
            Prim.pop(last_index)
            last_index-=1

print('\nModified list',Prim)

P =  functools.reduce(operator.mul,  [i[0]**i[1] for i in Prim ] )
print('\nAnswer : \t', P)

@2017-02-22, 11:00 --> Need to fix the above algorithm !!!

##### BRUTE FORCE CHECK   #####
print('\nRedundant check :', P, calculate_divisors(P),'\n' )

target = 2**10
for i in range(0, 10**9, 30030) :
    u = calculate_divisors(i)
    if u == target :
        print(i,'    <--' , factors(i) )
        break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
