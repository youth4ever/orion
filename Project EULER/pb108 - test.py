import functools, operator
from pyprimes import factorise
from itertools import permutations, combinations
import gmpy2

def  calculate_divisors(nr):
    '''**©** Made by Bogdan Trif @2016-12-08, 16:30.
        :Description: Functions which computes the number of divisors of a number.
                It uses the Numbers of Divisors Theorem :which says : if N=a**x*b**y*c**z => divisors_nr=(x+1)(y+1)(z+1)
            Example: N = 216 = 2**3 * 3**3 => divisors_nr = (3+1)(3+1) = 16
    :param nr: int, nr
    :return: int, divisors_number
    '''

    def factors(nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        return [i for i in factorise(nr)]
    N = factors(nr)
    return  functools.reduce( operator.mul , [ (i[1]+1) for i in N ])


number = 114307200
F = [i for i in factorise(number)]
print('Factorise ',number,' : ' ,[i for i in factorise(number)])
print('calculate_divisors : ' ,calculate_divisors(number))
# print(len(list(unique_permutations(F[1:]))), list(unique_permutations(F[1:])))

for i in range(len(F)) :
    # print(F[i])
    for j in range(F[i][1] ) :
        print(F[i][0] , end='   ')

divisors = [1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20, 25, 30, 36, 45, 50, 60, 75, 90, 100, 150, 180, 225, 300, 450, 900]

X = []
for i in range(len(divisors)):
    for j in range(i, len(divisors)):
        frac = gmpy2.mpq(divisors[i], divisors[j])
        if frac.numerator != 1 :
            print(divisors[i], divisors[j], '    ', frac , frac.numerator )
            X.append(frac)

X = list(set(X))
print(len(X), X)








