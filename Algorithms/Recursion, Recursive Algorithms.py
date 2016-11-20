# RECURSION ALGORITHMS

# TOWERS OF HANOI, Solved Recursively
print('--------------  TOWERS OF HANOI, Solved Recursively -------------------')
def printMove(fr, to):
    print('move from ' + str(fr) + ' to '+ str(to))

def Towers(n, fr, to, spare):
    if n== 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

Towers(4, 'P1', 'P2', 'P3')


# RECURSION  FUNCTION ALGORITHM MULTIPLICATION
print('\n---------------- Recursive Function Implementation of the multiplication of two numbers : ------------------')
def mult_recursive(a=3, b=9):
    if b == 1:
        return a
    else :                                                              #  The Recursive Step
        return (a + mult_recursive(a, b-1))             #

print(mult_recursive(22,89))


# RECURSION FUNCTION FACTORIAL :
print('\n---------------- Recursive Function Implementation for Factorial : ---------------')
def factorial(n=10):
    if n == 1:
        return 1
    else:
        return (n*factorial(n-1))

print(factorial(12))

# RECURSION FUNCTION for base**POWER :
print('\n----------------  RECURSION FUNCTION for base**power  :       --------------------')

def recursionPower(base=3, exp=6):
    '''
    base: int or float.    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 1 : return base
    else :
        return (base * recursionPower(base, exp-1))

print(recursionPower(3,5))

# RECURSION Function for Greatest Common Factor - CMMDC, c.m.m.d.c. - Cel Mai Mic Divizor Comun
print('\n------------   CMMDC - Cel Mai Mare Divizor Comun - The Greatest Common Divisor - GCD ------------------')
def cmmdc(a, b):
    '''    a, b: positive integers     , cmmdc, c.m.m.d.c., Cel Mai Mare Divizor Comun
        returns: a positive integer,  The Greatest Common Divisor of a & b.
    '''
    if b == 0:
       return a
    else:
       return cmmdc(b, a % b)

print(cmmdc(1445, 3005))

########################################
print('\n ------------------- Fibonacci Recursion Function, HIGHLY INEFFICIENT for Fibonacci ------------------------')

def Fib_rec(n):     # Fibonacci Recursion
    if ( n == 1 or n == 0 )  :
        return 1
    else :
        return Fib_rec(n-1) + Fib_rec(n-2)

print(Fib_rec(10))      # Already for n > 30 it takes looooong to complete

####################################################

print('\n--------------------    Recursive Solution for PASCAL TRIANGLE       ------------------------------------------')

def lattice_paths(a, b):
    if a == 0 or b == 0:
        return 1
    else:
        return lattice_paths(a, b - 1) + lattice_paths(a - 1, b)

print(lattice_paths(4,4))

print('\n--------------------    Recursive Multiple For Loop Custom Levels       ------------------------------------------')
def loop_rec(y, number):
    if (number > 1):
        loop_rec( y, number - 1 )
        for i in range(y):
            print(i, end=' ')
        print(' ;')
    else:
        for i in range(y):
            print(i, end=' ')
        print(';')
loop_rec(6,4)

print('---'*15)

def loop_rec(y, number):
    if (number > 1):
        loop_rec( y-1, number - 1 )
        for i in range(y):
            print(i, end=' ')
        print(' ;')
    else:
        for i in range(y):
            print(i, end=' ')
        print('.')
loop_rec(10,10)

print('---'*15)

def loop_rec(y, number):
    if (number > 1):
        loop_rec( y+1, number - 1 )
        for i in range(y):
            print(i, end=' ')
        print(' ;')
    else:
        for i in range(y):
            print(i, end=' ')
        print('.')
loop_rec(1,6)
print('---'*15)

def loop_rec(y, number):
    if (number >= 1):
        loop_rec( y+1, number - 1 )
        for i in range(y):
            print(i, end=' ')
        print('')
    else:
        return

loop_rec(1,5)

####################################################

print('\n--------------------------- RECURSION LOOP FOR WITH LIST ASCENDING, Descending Length ----------------------------')

fives=[5,10,15,20,25,30,35]
def rec_loop_for(i):
    if (i >= 1):
        rec_loop_for(i-1)
        for i in range(len(fives)+1-i):
            print(fives[0:i+1])
        print(';')
    else:
        return

rec_loop_for(len(fives))

print('\n--------------------------- RECURSION LOOP FOR WITH LIST DESCENDING, Descending length ----------------------------')

def rec_loop_for(i):
    if (i >= 1):
        rec_loop_for(i-1)
        for i in range(len(fives)+1-i,0,-1):
            print(fives[0:i])
        print(';')
    else:
        return

rec_loop_for(len(fives))

print('\n--------------------------- RECURSION LOOP FOR WITH LIST DESCENDING, Ascending length ----------------------------')

L=[2,3,5,7]
def rec_loop_for(i):
    if (i >= 1):
        rec_loop_for(i-1)
        for i in range(i):
            print(L[0:i+1])
        print(';')
    else:
        return

rec_loop_for(len(L))