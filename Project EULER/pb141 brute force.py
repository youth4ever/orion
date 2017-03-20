from pyprimes import factorise

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


def brute_force (up_bound) :
    S = 0

    for d in range( 2, up_bound ) :
        for r in range(d-1, 0, -1 ) :
            if d/r > 12 : break
            n = d**3 /r + r
            # if r == 8 :   print( n ,(n**(1/2)) % 1 == 0  , (n**(1/2)) , up_bound**2  )
            if  (n**(1/2)) % 1 != 0 : continue

            if  (n**(1/2)) % 1 == 0 and n < up_bound**2 :
                q , k  = d**2//r , d/r
                S += n
                print('   r =  ',r , '     d=',d , '       q=',q , '     n=',n,'     ratio =', k ,'       r = ', get_factors(r))

    return print('\nAnswer : \t', S)

brute_force(10**6)
# brute_force(  int((10**5)**(1/2))+1 )