#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 3 Nov 2016, 17:17
#The  Euler Project  https://projecteuler.net
'''
Almost equilateral triangles        -       Problem 94
It is easily proved that no equilateral triangle exists with integral length sides and integral area.
However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths
and area and whose perimeters do not exceed one billion (1,000,000,000).
'''
import time
from decimal import *
getcontext().prec = 50
from itertools import count


def heron_area1(a):
    s= (3*a+1)/2
    return Decimal(s*(s-a)*(s-a)*(s-a-1)).sqrt()

def heron_area2(a):
    s= (3*a-1)/2
    return Decimal(s*(s-a)*(s-a)*(s-a+1)).sqrt()

def triang_area1(a):
    h = Decimal(a*a - ((a+1)/2)**2).sqrt()
    return (a+1)*h/2

def triang_area2(a):
    h = Decimal(a*a - ((a-1)/2)**2).sqrt()
    return (a-1)*h/2

print('--------------TESTS -------------------')
# print(almost_equil_triang_area1(5) , almost_equil_triang_area1(5) % 1 == 0 )
# print(almost_equil_triang_area2(5) , almost_equil_triang_area2(5) % 1 == 0 )
print(Decimal(2).sqrt())

print(heron_area1(1577987) , heron_area1(1577987) % 1 == 0 )
print(triang_area1(1577987) , triang_area1(1577987) % 1 == 0 )
print(heron_area2(1600445) , heron_area2(1600445) % 1 == 0 )
print(triang_area2(1600445) , triang_area2(1600445) % 1 == 0 )


print('\n-------------------  MY SOLUTION ----------------------')
# Using http://www.had2know.com/academics/nearly-equilateral-heronian-triangles.html
t1  = time.time()
V=[]        # Case 1 , n,n, n+1
W=[]         # Case 2 , n,n+1, n+1
iter=0
S = 0
for i in range(3 , 10**9//3+1, 2):
    iter+=1
    if triang_area1(i) % 1 == 0 :
        V.append(i)
        S += 3*i+1
        print( i, i , i+1 , '  p=' ,3*i+1 , '  ',triang_area1(i), '  <- case 1  ')
    if triang_area2(i) % 1 == 0 :
        W.append(i-1)
        S += 3*i-1
        print( i-1, i, i , '  p=' , 3*i-1,'   ' ,triang_area2(i), '  <- case 2  ')
    # if iter % 2.5e7 == 0 : print(iter)
    if len(V) == 3 and len(W) == 3 : break

# print('\nV:',V)
# print('W : ',W,'\n')

for i in count():
    v = 15*V[-1]- 15*V[-2] + V[-3]
    w = 15*W[-1]- 15*W[-2] + W[-3]
    if v < 1e9/3 :
        V.append( v )
    if w < 1e9/3 :
        W.append( w )
    else : break


print('\n',V,'\nPerimeters :     ', [3*i+1 for i in V])
print(W,'\nPerimeters :     ', [3*i+2 for i in W])

print()
print('PERIMETERS SUM: ',sum([3*i+1 for i in V] + [3*i+2 for i in W]))    # Answer : 518408346


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')      # Completed in : 81.0046 ms


# THIS GENERATES the almost equilateral triangles for the Isoscel case case a=b+1=c+1 IS OK !E.g, a=5,b=6,c=6
# Now I need to make one for the Isoscel Case a=b-1=c-1, E.g : a= 16, b=17, c=17
# from math import gcd
# S=0
# for u in range(10**5,10**6):
#     for v in range(int(u*0.49), int(u)):
#         a = 2*(u*u - v*v)
#         b, c = u*u + v*v , u*u + v*v
#         if gcd(u,v) ==1 and a == b+1 :
#             print(u,v,'  ',a,b,c, '    Perimeter : ',a+b+c)
#             S+=a+b+c
#             break
# print('\n',S)


#
# 5.   p= 16    12   <- case 1
# 17.   p= 50     120   <- case 2
# 65.   p= 196    1848   <- case 1
# 241.   p= 722     25080   <- case 2
# 901.   p= 2704    351780   <- case 1
# 3361.   p= 10082     4890480   <- case 2
# 12545.   p= 37636    68149872   <- case 1
# 46817.   p= 140450     949077360   <- case 2
# 174725.   p= 524176    13219419708   <- case 1
# 652081.   p= 1956242     184120982760   <- case 2
# 2433601.   p= 7300804    2564481115560   <- case 1
# 9082321.   p= 27246962     35718589344360   <- case 2
# 33895685.   p= 101687056    497495864091732   <- case 1


# Answer: Not ok All Perimeters Sum : 138907096


print('\n============  OTHER SOLUTIONS FROM EULER FORUM =============')
print('\n----------------SOLUTION 1 ,-------------------------')
t1  = time.time()

# ben1996123, Mathematica, England

# I just solved Pell's equation. The area of a triangle with side lengths a, a, a+1 is :
#
# 1/4 (a+1) sqrt((a-1)(3a+1))
#
# so (a-1)(3a+1) = x^2 has to be a perfect square. Substituting x -> 2x and a -> (2a-2)/3 gives the equation a^2 - 3x^2 = 1,
# which we can solve and get the solutions.
# Same method for a triangle with side lengths a, a, a-1.
# Then we just need to check which ones have 1/4 (a+1) x as an integer (they all do), and sum 3a+1 or 3a-1.



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

print('\n----------------SOLUTION 2 , VERY NICE SOLUTION-------------------------')
t1  = time.time()

# All solutions of the form s, s, s+1 can be derived from solving
# the Pell's Equation for d = 3
def pell_solutions (d, init_x, init_y, max_perimeter):
    perim_sum = 0
    x0, y0 = init_x, init_y
    s = x0 ** 2 + y0 ** 2
    perim = s + s + (s + 1)
    xn, yn = x0, y0

    while perim < max_perimeter:
        perim_sum += perim
        x_next = x0 * xn + d * y0 * yn
        y_next = y0 * xn + x0 * yn
        s = x_next ** 2 + y_next ** 2
        perim = 3 * s + 1
        xn, yn = x_next, y_next

    return perim_sum

# The triangles of form s, s, s-1 can be generated by finding the
# squares x ** 2 such that (x ** 2 + 8) / 3 is also square
# This follows from conditions of generating Pythagorean triples
def greater_side_solutions (max_perimeter):
    perim_sum = 0
    square_range = [x * x for x in range(1, int((2 * max_perimeter)**0.5)+1)]
    oth_range = map (lambda x: (x + 8)/3, square_range)
    test_set = set(square_range).intersection(set(oth_range))
    test_list = list(test_set)
    test_list.remove(4) # this will appear in the set
                        # but it corresponds to triangle w sides 1,1,2
    return sum(map(lambda x: (3 * x - 8)/2, test_list))

def main():
    d = 3
    init_x, init_y = 2, 1
    max_perimeter = 10 ** 9
    perim_sum = pell_solutions (d, init_x, init_y, max_perimeter)
    perim_sum += greater_side_solutions (max_perimeter)
    print (perim_sum)
main()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

# print('\n----------------SOLUTION 3 ,-------------------------')
# t1  = time.time()
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')
#
# print('\n----------------SOLUTION 4 ,-------------------------')
# t1  = time.time()
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')
#
# print('\n----------------SOLUTION 5 ,-------------------------')
# t1  = time.time()
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

