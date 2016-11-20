#!/usr/bin/python3
# Solved by Bogdan Trif @       Completed on Wed, 2 Nov 2016, 17:53
#The  Euler Project  https://projecteuler.net
'''
                Right triangles with integer coordinates    -   Problem 91

The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.
There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive;
that is: 14 pictures with triangles
                                                                    0 ≤ x1, y1   ;  x2, y2 ≤ 2.

Given that 0 ≤ x1, y1,    x2, y2 ≤ 50, how many right triangles can be formed?
'''
import time
from math import sqrt, gcd



print('----------------- TESTS -----------------')

def check_subpoints(x , y) :        # MY OLD ATTEMPT, was wrong
    '''This function checks only the y sides doesn't account for all the possibilities. It may helpful ... '''
    points = {}
    for i in range(1, x):       # x , y ranges are ok because we check subpoints x-1, y-1. It's ok
        for j in range(1, y):
            # print(i , j)
            for a in range(j+1 ,y+1) :
                A = (i*i+j*j)
                B = i*i+(a-j)**2
                C = sqrt(A+B)
                # print(i , j , a, '     ',sqrt( (i*i+j*j) + (i*i+(a-j)**2) ) )
                if C == a :
                    # print(i , j , a,'0       ', C )
                    points[str(i)+','+str(j)+';0,'+str(a)] = (i , j)
                    points[str(j)+','+str(i)+';'+str(a)+',0'] = (j , i)
    main_points = 3*x*y
    return len(points),points              #+main_points

print(check_subpoints( 5 , 5))

print('\n--------Shift right/left functions --------------')
# Lambda Functions :
shift_right = lambda a, b :  [b, -a]        # Lambda Function to generate a vector   with 90 degrees angle to the right
print(shift_right(2,3))
shift_left = lambda a, b :  [-b, a]         # Lambda Function to generate a vector   with 90 degrees angle to the left:
print(shift_left(2,3))
# new_coord_right = lambda a, b : [a+shift_right(a , b)[0] , b+shift_right(a, b)[1] ]
# new_coord_left = lambda a, b : [a+shift_left(a,b)[0] , b+shift_left(a, b)[1] ]

# def new_coord_right(a, b , v_r):
#     v_r = lambda a, b :  [int(b/n), int(-a/n)]

# vector = lambda a, b :  [int(b/n), int(-a/n)]


def new_coord_left(a, b):
    n=gcd(a, b)
    return [a- int(b/n) , b + int(a/n) ]

# print('New Right coordinates : ',new_coord_right(2 , 2 ))
# print('New Right coordinates : ',new_coord_right(3 , 1 ))
print('New Left coordinates : ',new_coord_left(2 , 2 ))
print('New Left coordinates : ',new_coord_left(1 , 3 ))

print('---------------------')
print([i>0 for i in (3,-2)])
print('>0 Test : ',False if False in [ i>=0 for i in [3, -2]] else True)      # Tuple Test, Replace [] with () ,List Comprehension, by Bogdan Trif
print([i<=50 for i in (50, 51)])
print('<x , <y Test : ',False if False in [ i<=50 for i in [50, 51]] else True)      # Tuple Test, Replace [] with () ,List Comprehension, by Bogdan Trif

print( 'Divide each element from a List  ' ,[ int(i / 2) for i in [2,4]  ])      # List Comprehension to divide each element of a list
print(gcd(3,6))
a, b = 2 , 2
n=gcd(a, b)
v_r = [int(b/n), int(-a/n)]
print( a+ v_r[0] , b + v_r[1] )
c, d = a+ v_r[0] , b + v_r[1]
print ( c+ v_r[0] , d + v_r[1] )

print('---------------------------')
points = []



print('\n-------------  THE MAIN TEST :):):)------------------')
x , y = 50 , 50
for a in range(1 ,x+1) :
    for b in range(1 ,y+1) :
        n = gcd(a,b)
        v_r = [int(b/n), int(-a/n)]
        v_l = [int(-b/n), int(a/n)]
        c_d = [a+ v_r[0] , b + v_r[1]]
        e_f = [a+ v_l[0] , b + v_l[1]]

        up_c_d = False if False in [ i<=x for i in c_d] else True
        down_c_d = False if False in [ i>=0 for i in c_d ] else True
        up_e_f = False if False in [ i<=x for i in e_f] else True
        down_e_f = False if False in [ i>=0 for i in e_f ] else True

        if down_c_d == True and up_c_d == True :
            points.append( ([a,b],c_d ))
            print([a, b] , ' ;   vector:', v_r ,' ;    new_coord :'  ,c_d, '  ' , down_c_d, up_c_d ,'    <<---c, d-----')

        while down_c_d == True and up_c_d == True :
            #print(c_d)
            c_d = [c_d[0]+v_r[0] ,c_d[1]+v_r[1] ]
            #print(c_d)
            up_c_d = False if False in [ i<=x for i in c_d] else True
            down_c_d = False if False in [ i>=0 for i in c_d ] else True
            if down_c_d == True and up_c_d == True :
                print([a, b] , ' ;   vector:',v_r ,' ;    new_coord :'  ,c_d, '  ' , down_c_d, up_e_f , '    -- WHILE c,d--')
                points.append( ([a,b],c_d ))

        if down_e_f == True and up_e_f == True :
            points.append( ([a,b],e_f ))
            print([a, b] , ' ;   vector:', v_l ,' ;    new_coord :'  ,e_f, '  ' , down_e_f, up_e_f, '    <<----e, f------')

        while down_e_f == True and up_e_f == True :
            # print(e_f)
            e_f = [e_f[0]+v_l[0] ,e_f[1]+v_l[1] ]
            # print(e_f)
            up_e_f = False if False in [ i<=x for i in e_f] else True
            down_e_f = False if False in [ i>=0 for i in e_f ] else True
            if down_e_f == True and up_e_f == True :
                print([a, b] , ' ;   vector:',v_l ,' ;    new_coord :'  ,e_f, '  ' , down_e_f, up_e_f , '    -- WHILE  e,f--')
                points.append( ([a,b],e_f ))

print('\nPoints : ', len(points) , points)

# print( (25,25) in points.values())
# print([k for k, v in points.items() if v ==(21,21)])       # NICE List comprehension to get the keys for a specific value in a Dictionary



print('\n---------------------------- MY FIRST SOLUTION   -----------------------------\n')
t1  = time.time()

def right_triangles_integer_coord(x):           # Looks ugly because of the explanations
    points = []
    for a in range(1 ,x+1) :
        for b in range(1 ,x+1) :
            n = gcd(a,b)                        #  The scale vector factor, Example : to gcd(3,3)=3 will result in a vector scaled by 3 =>v_r=[1,-1], v_l=[-1,1]
            v_r = [int(b/n), int(-a/n)]     # This is the vector that shifts to right and finds the new coordinates scaled by gcd
            v_l = [int(-b/n), int(a/n)]     # This is the vector that shifts to left and finds the new coordinates scaled down by gcd
            c_d = [a+ v_r[0] , b + v_r[1]]  # new point to the right c_d = (c,d) resulted from applying right vector, and thus having a triangle [(0,0),(a,b),(c,d) ]
            e_f = [a+ v_l[0] , b + v_l[1]]      # new point to the left  e_f = (e,f) resulted from applying left vector, and thus having a triangle [(0,0),(a,b),(e,f)

            up_c_d = False if False in [ i<=x for i in c_d] else True       # up range to the right Check
            down_c_d = False if False in [ i>=0 for i in c_d ] else True    # down range to the right Check
            up_e_f = False if False in [ i<=x for i in e_f] else True           # up range to the left Check
            down_e_f = False if False in [ i>=0 for i in e_f ] else True        # up range to the left Check ; We need all these conditions because we have
    # RIGHT CASE          #  because we have two cases: vectors to the right & to the left
            if down_c_d == True and up_c_d == True :                # CASE RIGHT VECTOR
                points.append( ([a,b],c_d ))                        # If the [c,d] points are in the square we count them
                # print([a, b] , ' ;   vector:', v_r ,' ;    new_coord :'  ,c_d, '  ' , down_c_d, up_c_d ,'    <<---c, d-----')

            while down_c_d == True and up_c_d == True :         # After computing the first triangle we check for next others using the v_r vector
                c_d = [c_d[0]+v_r[0] ,c_d[1]+v_r[1] ]                       # change the coordinate by the shifting vector to the right v_r
                up_c_d = False if False in [ i<=x for i in c_d] else True       # we update the check with the new coordinates conditions
                down_c_d = False if False in [ i>=0 for i in c_d ] else True    # update with new coordinates, without those => infinite loop
                if down_c_d == True and up_c_d == True :            # check again if the new point coordinates are in the square :
                    # print([a, b] , ' ;   vector:',v_r ,' ;    new_coord :'  ,c_d, '  ' , down_c_d, up_e_f , '    -- WHILE c,d--')
                    points.append( ([a,b],c_d ))                            # count if it obeys the criteria
    # LEFT CASE
            if down_e_f == True and up_e_f == True :            # CASE LEFT VECTOR,  the same as the other case but using the v_l shifting vector
                points.append( ([a,b],e_f ))
                # print([a, b] , ' ;   vector:', v_l ,' ;    new_coord :'  ,e_f, '  ' , down_e_f, up_e_f, '    <<----e, f------')

            while down_e_f == True and up_e_f == True :
                e_f = [e_f[0]+v_l[0] ,e_f[1]+v_l[1] ]
                up_e_f = False if False in [ i<=x for i in e_f] else True
                down_e_f = False if False in [ i>=0 for i in e_f ] else True
                if down_e_f == True and up_e_f == True :
                    # print([a, b] , ' ;   vector:',v_l ,' ;    new_coord :'  ,e_f, '  ' , down_e_f, up_e_f , '    -- WHILE  e,f--')
                    points.append( ([a,b],e_f ))
    main_points = 3*x*x
    return len(points) + main_points

print(right_triangles_integer_coord(50))            # Answer : 14234

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')          #Completed in : 51.003 ms



print('\n============  OTHER SOLUTIONS FROM EULER FORUM =============')
print('\n----------------SOLUTION 1 , THE FASTEST & ELEGANT SnakeCake, England-------------------------')
t1  = time.time()
# Fast code - 6ms for solution, or under 2 seconds for 500 by 500 grid (where the improvement over brute force really shows).
# Imported primes method just generates primes up to and including the parameter
gridsize = 50
prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

def remove_common_factors(x,y):
    for p in prime:
        while x % p == 0 and y % p == 0:
            x //= p
            y //= p
        if p > x or p > y:
            break
    return x,y

def main(lim):
    total = 0
    for px in range(1, lim + 1):
        for py in range(1, lim + 1):
            dx, dy = remove_common_factors(py, px)
            total += min((lim - px) // dx, py // dy)
    ## Double for right angle at Q and add lim^2 for right angles at origin and P or Q on axis
    return (total * 2) + (lim**2 * 3)

print(main(gridsize))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')          # Completed in : 11.0006 ms




print('\n----------------SOLUTION 2 , REALLY FAST & VERY ELEGANT , Hvalfisk, Denmark-------------------------')
t1  = time.time()
# I pick a point (x,y), and for every multiple of this point (n*x, n*y),
# I calculate how many times (x, y), rotated either clockwise (y, -x) or counter-clockwise (-y, x),
# can be added to the (n*x, n*y) before going out of bounds.

from itertools import product
points = product(range(1,50), repeat=2)
angles = set()
result = 3*50**2
for x, y in points:
    if not y/x in angles and x+y <= 50:
        angles.add(y/x)
        for n in range(1,50//max(x,y)+1):
            result += min((50-n*x)//y, n*y//x)
            result += min((50-n*y)//x, n*x//y)
print(result)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')          # Completed in : 10.0007 ms


print('\n----------------SOLUTION 4 , nimon, England-------------------------')
t1  = time.time()
# This problem is my proudest achievement on this website! Very enjoyable. I am clearly more a mathematician than a programmer :/

def vectoradd(p,q):
    return (p[0]+q[0], p[1]+q[1])

def scale(p,k):
    return (k*p[0],k*p[1])

def solve(n):
    total = n**2

    mesh = []

    for p1 in range(n+1):
        for p2 in range(n+1):
            mesh += [(p1,p2)]

    P = mesh
    P.remove((0,0))

    for p in P:
        g = gcd(p[0],p[1])
        orth = (-(p[1]/g),p[0]/g)
        k = 1
        while vectoradd(p,scale(orth,k)) in mesh:
            total += 2
            k += 1

    print (total)

solve(50)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')      # Completed in : 2151.1228 ms



print('\n----------------SOLUTION 5 , BRUTE FORCE , List Comprehension, Talby, Germany  -------------------------')
t1  = time.time()
# The brute force solution as python one-liner:

from itertools import *
print(sum((a[0]+a[1]==a[2] for a in (sorted((p[0]**2+p[1]**2, q[0]**2+q[1]**2, (p[0]-q[0])**2+(p[1]-q[1])**2)) for (p,q) in combinations(product(range(51),range(51)),2)) if a[0]>0)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')          # Completed in : 26524.5171 ms

print('\n----------------SOLUTION 5 , elvischen   -------------------------')
t1  = time.time()
# The brute force solution as python one-liner:

L = 50
sum_t = L*L*3
for x1 in range(0,L+1):
    for y1 in range(0,x1+1):
        for x2 in range(1,L+1):
            for y2 in range(1,L+1):
                if x1**2+y1**2 == x2**2+y2**2+(x1-x2)**2+(y2-y1)**2:
                    if x1 != x2 and y1!= y2:
                        if x1==y1:
                            sum_t += 1
                        else:
                            sum_t += 2
print (sum_t)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

