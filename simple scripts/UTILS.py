
def counter_generator( up_nr, elem_nr ):    # o(^_^)o   ©Bogdan Trif @ 2017 -02-19, 14:00   ( ͡° ͜ʖ ͡°)
    ''':Generates a counter of a given elem_nr up to the up_nr
        Useful in finding common multiples of a list of primes numbers
    :param up_nr: int, up_power of the list
    :param elem_nr: int, nr of elements in the list
    :return: tuples, representing the   possible combinations                                             '''
    import itertools
    G=[]
    for k in itertools.product(*[range(1, up_nr+1)]*elem_nr):
        print( k )
        G.append(k)
    return G

counter_generator( 7 , 2 )