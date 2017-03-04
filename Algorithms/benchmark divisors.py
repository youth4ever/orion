import time



############## SLOW ALGORITHM FOR LARGE n's - TO DELETE !!!!!!!!!!

t1  = time.time()

n = 1216036521


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

###################

t1  = time.time()



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


print( calculate_divisors(n))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')
