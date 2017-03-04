#!/usr/bin/python                   o(^_^)o
# Solved by Bogdan Trif @   Completed on Thu, 16 Feb 2017, 20:51
#The  Euler Project  https://projecteuler.net
'''
                                Concave triangle        -       Problem 587

A square is drawn around a circle as shown in the diagram below on the left.
We shall call the blue shaded region the L-section.
A line is drawn from the bottom left of the square to the top right as shown in the diagram on the right.
We shall call the orange shaded region a concave triangle.

p587_concave_triangle_1.png
It should be clear that the concave triangle occupies exactly half of the L-section.

Two circles are placed next to each other horizontally, a rectangle is drawn around both circles,
and a line is drawn from the bottom left to the top right as shown in the diagram below.

p587_concave_triangle_2.png
This time the concave triangle occupies approximately 36.46% of the L-section.

If n circles are placed next to each other horizontally, a rectangle is drawn around the n circles,
and a line is drawn from the bottom left to the top right, then it can be shown that the least value of n
for which the concave triangle occupies less than 10% of the L-section is n = 15.

What is the least value of n for which the concave triangle occupies less than 0.1% of the L-section?

'''
import time, math
import scipy, sympy
from scipy.integrate import dblquad

x, y, z = sympy.symbols("x y z")

circle = (x- (1/2))**2 + (y-(1/2))**2 - (1/4)

print('\n-----Second example, more detailed : -------\n')
# The main equation, we substitute y=f(x) = x/2 into it, ##### actually we do x=2*y
w1 = circle.subs( y, x/1 )
print('The SUBSTITUTED expression : \t' , w1 )

#Expand, Put in standard form
w2 = sympy.expand (w1)
print('The EXPANDED expression : \t' ,  w2 )
# Lambdify, which means that we create a function from the previous expression
J =  sympy.lambdify(x, w2)
print('We simply test the function with some values : \t',J(0), J(1), J(1/2))
# we find the roots of the quadratic equation :

print('Solving quadratic, finding its roots : \t', sympy.solve( w2, x ) )
min_root = min ( sympy.solve( w2, x ) )
print('The smallest root is : \t', min_root)



######### Bounded region by y = x, circle : (x-1/2)**2+(y-1/2)**2 = 1/4, x=0


area2 = dblquad(lambda x,y : 1, 0, 0.146446609406726, lambda x: x, lambda x: (1/2)-(x-x*x)**(1/2))
print('\n',area2,'\n', area2[0])



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

x, y, z = sympy.symbols("x y z")
def find_x_up_bound( n) :
    circle = (x- (1/2))**2 + (y-(1/2))**2 - (1/4)
    w1 = circle.subs( y, x/n )
    #Expand, Put in standard form
    w2 = sympy.expand (w1)
    print('The EXPANDED expression : \t' ,  w2 )
    # we find the roots of the quadratic equation :
    print('Solving quadratic, finding its roots : \t', sympy.solve( w2, x ) )
    min_root = min ( sympy.solve( w2, x ) )
    print('The smallest root is : \t', min_root)
    return min_root

print('\nfind_x_up_bound : \t' ,find_x_up_bound(10) )

n=10
x_up = find_x_up_bound(n)

def compute_area( x_up, n ) :
    area = scipy.integrate.dblquad( lambda x,y : 1, 0, x_up, lambda x: x/n , lambda x: (1/2)-(x-x*x)**(1/2) )
    # print('\n',area,'\n', area[0])
    return area[0]

print('\ncompute_area : \t' ,compute_area(x_up, n) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n============= My FIRST SOLUTION, 10 sec  ===============\n')
t1  = time.time()

def solution_pb_587(n=2220) :
    L_section = (1-math.pi/4 )/4
    print('L_section area : \t', L_section)

    while True :
        x_up = find_x_up_bound(n)
        area = compute_area(x_up, n)
        print()
        print(str(n)+'.         x_up =', x_up,'      area=', area, '      %=', 100-area*100/L_section  )
        if 100-area*100/L_section < 0.1 :

            return print('\nAnswer : \t', n)

        n+=1


# solution_pb_587()                   #   Answer : 	 2240

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  18 ms  --------------------------')
t1  = time.time()

# ===== Sat, 11 Feb 2017, 05:40, WalkerTesla, USA
# I used the Quadratic Formula to find the lower intersection of the line with the leftmost circle.
#
# From here, I defined three areas, includeTriangle, which is the triangle connecting the origin
# to the lower tangency point of the leftmost circle to the intersection above,
# excludeTriangle which is the triangle connecting the center of the leftmost circle to the intersection above
# to the lower tangency point of the leftmost circle, and sector, which is the sector of the leftmost circle
# which corresponds to the arc from the above intersection to the lower tangency point of the leftmost circle.
#
# Then the area of concave triangle is just includeTriangle - sector + excludeTriangle.
#
# This Python script runs this:

import math
lsection = 1-math.pi/4

def findIntersection(n):
    a = (n*n+1)/(n*n)
    b = -2-2/n
    c = 1
    x = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    y = x/n
    return [x,y]

def subtractSector(a):
    x = a[0]
    y = a[1]
    thirdSide = math.sqrt((1-x)*(1-x) + y*y)
    angle = 2*math.asin(thirdSide/2)
    sector = angle/2
    return sector

def areaTriangle(a, b, c):
    sum1 = 0
    sum2 = 0
    sum1 += a[0]*b[1]
    sum1+= b[0]*c[1]
    sum1+=c[0]*a[1]
    sum2+= b[0]*a[1]
    sum2+= c[0]*b[1]
    sum2+=a[0]*c[1]
    return abs(sum1-sum2)/2

def fractionLSection(n):
    coordinates = findIntersection(n)
    sector = subtractSector(coordinates)
    includeTriangle = coordinates[1]/2.0
    excludeTriangle = (1.0-coordinates[0])/2.0
    area = includeTriangle - sector + excludeTriangle
    return area/lsection

counter = 2.0
value = 1.0
while(value>0.001):
    value = fractionLSection(counter)
    counter+=1.0

print (counter-1)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ======Tue, 7 Feb 2017, 01:02, Cal22, England
#
# Some points:
#
# I let the bottom left corner be the point (0,0), and let the circles have radius 1.
# The line and circle therefore intersect where (x−1)**2+(x**2/n**2−1)**22=1,
# which can be expanded and solved using the quadratic formula.
#
# In calculating ∫{X, 1} 1−√dx∫X11−1−(x−1)2dx I used the substitution x−1=sin(u)x−1=sin(u) which yields
# ∫0arcsin(X−1)cos(u)−cos2(u)du=[sin(u)−u2−sin(2u)4]
# 0arcsin(X−1)=1−X+arcsin(X−1)2+sin(2arcsin(X−1))4∫arcsin(X−1)0cos(u)−cos2(u)du=[sin(u)−u2−sin(2u)
# 4]arcsin(X−1)0=1−X+arcsin(X−1)2+sin(2arcsin(X−1))4 (where X is the x value of the point of intersection).


import math
import numpy

#in all functions, the n parameter refers to the number of circles present

def get_intersection(n): #returns the first point of intersection between the line y=x/n and the circle (x-1)^2+(y-1)^2=1
    a = 1 + (1 / (n ** 2))
    b = -2 - (2 / n)
    c = 1

    x = min(numpy.roots([a, b, c]))
    y = x / n

    return {"x": x, "y": y}

def get_concave_triangle_area(n):
    intersection = get_intersection(n)

    return (intersection["x"] * intersection["y"] / 2)\
        + 1\
        - intersection["x"]\
        + (math.sin(2 * math.asin(intersection["x"] - 1)) / 4)\
        + (math.asin(intersection["x"] - 1) / 2)

def get_l_section_proportion(n):
    return get_concave_triangle_area(n) / (1 - (math.pi / 4))

n = 1
while True:
    proportion = get_l_section_proportion(n)
    print("n={} gives a proportion of {}".format(n, proportion))

    if proportion < 0.001:
        break

    n += 1



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, 2 ms  --------------------------')
t1  = time.time()


# ====Mon, 6 Feb 2017, 06:21, wakkadojo, USA
# I've been out of the saddle for quite some time. Nice for euler to give a freebie for people like me that need to ease back in.
#
# I centered my circle at (1, 1)
# Step 0: Area of the "ell" is 1−π/4
#
# Step 1: is to calculate intercept of a line with the circle.
# The intercept is x_m=(1+m−2m−√)/(1+m2)xm=(1+m−2m)/(1+m2) where mm is the slope (i.e. 1/n1/n).
#
# Step 2: analytical calc of the area. Break the section into a curve + a triangle, and the area becomes
# mx2m2−12[(1−xm)1−(1−xm)2)−−−−−−−−−−−−√+sin−1(1−xm)]
# mxm22−12[(1−xm)1−(1−xm)2)+sin−1⁡(1−xm)]
#
# Step 3: Determine range to search. Just double upper bound until area fraction is below the target
# Step 4: Binary search
# 2240
# real	0m0.464s
# user	0m0.407s
# sys	0m0.047s


import numpy as np

def ell_area():
    return 1 - np.pi / 4

def find_intercept(m):
    return (1 + m - np.sqrt(2*m)) / (1 + m**2)

def find_area(m):
    x0 = find_intercept(m)
    triangle_area = m * x0**2 / 2
    curve_area = (1 - x0) - 0.5*(\
        (1 - x0) * np.sqrt(1 - (1 - x0)**2) +\
        np.arcsin(1 - x0)\
    )
    return triangle_area + curve_area

def cast_wide(tgt_frac, n):
    m = 1 / n
    area_frac = find_area(m) / ell_area()
    if area_frac < tgt_frac:
        return n
    else:
        return cast_wide(tgt_frac, 2 * n)

def binary_contract(tgt_frac, low, high):
    if low == high - 1:
        return high
    else:
        mid = (low + high) // 2
        m_mid = 1 / mid
        frac_mid = find_area(m_mid) / ell_area()
        if frac_mid > tgt_frac:
            return binary_contract(tgt_frac, mid, high)
        else:
            return binary_contract(tgt_frac, low, mid)


tgt_frac = 0.001
high_bound = cast_wide(tgt_frac, 1)
print(binary_contract(tgt_frac, 1, high_bound))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, 3.5 secs  --------------------------')
t1  = time.time()

# ===Sun, 5 Feb 2017, 21:50, rathmann, USA
# My method is similar to many so far.
#
# I used Sympy to solve the quadratic and evaluate the integral.  Since I
# have not seen a Sympy solution yet, here it is.  The code is not
# particularly short, but (I think) quite straightforward:
# One additional note, especially for those with an aversion to
# trigonometric integrals: For xx near 0, the circular arc can be
# approximated quite well by a parabola:
#
# 1−1−x2−−−−−√=x22+O(x4)
# 1−1−x2=x22+O(x4)
#
# (Think Taylor series or osculating circles in reverse.)  Substituting
# x22x22 makes for a nice easy integral, which evaluates to
#
# −(k−2–√k3−−√−1)36(k2+1)3
# −(k−2k3−1)36(k2+1)3
#
#
# (For k the number of circles in the original problem.)
# This avoids any arcsins, and is very close to the exact expression in the vicinity of 2240.


from sympy import symbols, sqrt, solve, Eq, simplify, Integral, N,  pi

x,y, k = symbols('x, y, k')

# Coordinate system: (0,0) is center of circle.  Circle has radius 1,
# and corner of rectangle is (-1, -1).
e1 = Eq(x**2+y**2,1)   # Equation of circle
e2 = Eq(k*(y+1), x+1)  # line from (-1, -1) with slope 1/k

sols = solve([e1,e2], (y,x), dict=True)

# There are two solutions; I looked and picked the one in the desired
# quadrant.
x_k = sols[0][x]
y_k = sols[0][y]

# Divide the concave triangle into a (real) triangle on the left, and
# a portion under the circle on the right.

Area_t = simplify((x_k+1)*(y_k+1)/2) # Triangle on left
Area_i = Integral(1-sqrt(1-x**2), (x, x_k, 0))  # portion under circle

def area_proportion(n_circles):
    """Compute the gives a concave triangle to L-section ratio."""
    return N(
        (Area_t.subs(k,n_circles) + Area_i.subs(k,n_circles).doit()) /
        ((4-pi)/4))

for n_circles in [1, 2, 2239, 2240]:
    print (n_circles, "gives a concave triangle to L-section ratio of",     area_proportion(n_circles))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  VERY SIMPLE --------------------------')
t1  = time.time()

# ==== Wed, 25 Jan 2017, 00:27, Knut.Angstrom, Sweden

"""
Line: y=x/n
Circle x**2 + y**2 = 1
Cutting in A(x,y)
"""
from math import *
def p(n):
    n2=n**2
    x=(n2+n-sqrt(2*n**3))/(n2+1)
    y=x/n
    t=(1-x)/2        # Triangle (1,0),(x,y),(1,1) sin(angle)=1-x
    s=asin(1-x)/2    # Sector   (1,0),(x,y),(1,1)
    conc=y/2-(s-t)   # Triangle (1,0),(x,y),(0,0) - difference
    L=1-pi/4
    return conc/L
for n in range(1,10000):
    if p(n)<0.001:
        print(n)
        break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ===== Wed, 25 Jan 2017, 13:00, sO3SrLCr4Rqb00Zr..., Japan
# This one was too easy for a problem in the 500s.
# Even if numerical integration were somehow disallowed (due to a much smaller cutoff),
# it still would have been far too easy for a problem in the 500s.
# Basic numerical integration. No optimization of integration. No optimization such as binary search. Nothing.
# Problem read, programmed, and executed all under 3 minutes.


import numpy as np
import itertools

num_pts = 100


def conc_tri_area(n):
    x = np.linspace(0, 1, num_pts)

    # Take bottom left corner as origin
    m = 1/n
    b = 0
    y_lin = m*x+b

    # Use r=1, so (x-1)^2+(y-1)^2=1^2
    r = 1
    y_cir = -(r**2 - (x-1)**2)**0.5 + 1

    y = np.minimum(y_lin, y_cir)
    return np.sum(y)  # Fastest easiest way to program integration--only used as a ratio so ignore any constants.


def main():
    area_1 = conc_tri_area(1)
    area_L = 2*area_1  # This method may be better than a more exact solution as the rounding issues will work the same way as later when used in a ratio.
    cutoff = 0.001
    for n in itertools.count(1):
        area_n = conc_tri_area(n)
        area_ratio = area_n / area_L
        cutoff_pass = area_ratio <= cutoff

        if cutoff_pass:
            print(n, area_ratio, cutoff_pass)
            break


if __name__ == "__main__":
    main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# ==== Thu, 26 Jan 2017, 19:36, Guy, England

from math import pi,sin,asin,atan

x=1
n=0
while x>0.001:
    n+=1
    phi=0.25*pi-atan(1/n)
    beta=0.25*pi-asin(pow(2,0.5)*sin(phi))+phi
    x=(4*sin(beta/2)*sin(beta/2)-2*beta+2*sin(beta))/(4-pi)
print('The least number of circles is {}.'.format(n))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# ==== Sun, 29 Jan 2017, 19:37, mbh038, England
# Praise be! An 'easy one' that I can do! A welcome relief after other problems to which
# I have given up to three weeks of effort, some of that, up to now, fruitless. I love this site. Keep it up!
#
# About 0.2 ms in Python. Like many others I avoid integration and split the concave triangle into two parts to the left
# or right of the lower intersection of the left-most circle with the diagonal line.
# Assuming circles of unit radius, the coordinates x0,y0 of the intersection are found in terms of n, as:
# x0=nn+1−2n−−√n2+1
# x0=nn+1−2nn2+1
#
# y0=x0n
# y0=x0n
#
# The  area of the 'orange' triangle to the left of this intersection is x0y0/2,
# and the area of the concave triangle to its right is given by :
# AC=(1−x0)y02−θ−sinθ2
# AC=(1−x0)y02−θ−sin⁡θ2
#
# Thus the total 'orange' area is
# AC=y0(n)−θ+sinθ2
# AC=y0(n)−θ+sin⁡θ2
#
# where
# θ=arctan1−x01−y0
# θ=arctan⁡1−x01−y0
#
# The blue area LL is
# AL=1−π4
# AL=1−π4
#
# Using binary search, I find the smallest nn such that AC/AL<0.001 in about a dozen iterations.

import time
import math
import numpy as np

def p587(target):
    t=time.clock()
    nmin=1
    nmax=5000
    n=(nmax+nmin)//2
    r=ratio(n)
    lastn=nmax
    while abs(lastn-n)>1:
        lastn=n
        if r>target:
            nmin=n
        else:
            nmax=n
        n=(nmax+nmin)//2
        r=ratio(n)
        print(nmin,nmax,r)
    i = 0
    while ratio(n+i)>target:
        i+=1
    print((n+i-1,ratio(n+i-1)),(n+i,ratio(n+i)))
    print(time.clock()-t)

def ratio(n):
    """analytically find orange area/blue area"""
    x0,y0=xcross(n),ycross(n)
    theta=math.atan((1-x0)/(1-y0))
    AC=(y0-theta+math.sin(theta))/2
    AL=1-np.pi/4
    return AC/AL

def xcross(n):
    """returns lowest x value where diagonal line and leftmost circle cross"""
    return n*((n+1)-(2*n)**0.5)/(n**2+1)

def ycross(n):
    """returns lowest y value where diagonal line and leftmost circle cross"""
    return xcross(n)/n

p587(0.001)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 9,   --------------------------')
t1  = time.time()

# ==== Mon, 23 Jan 2017, 09:56, KORENA, USA
#
# My math skills aren't nearly what they should be so I went about this the old fashioned Trig route!
#
# 1. Calculate the intersection of the 1 / n line and the circle using the equation (x - 1)^2 + (mx - 1)^2 = 1 where "m" is 1 / n. Call that (x, y)
#
# 2. Find the angle between the points (1, 0), (1, 1), and (x, y). Call that A
# 3. Find the area of the "pizza slice" which is Pi * A / 360. Call that P
# 4. Find the area of the triangle (1, 0), (1, 1), and (x, y). Subtract that from P to get C
# 5. Find the area of the triangle (0, 0), (x, y), and (1, 0) and then subtract C from it to get F.
# 6. Take the ratio of F over (4 - Pi) / 4 (the area of L)!
#
# Runs in a few milliseconds.

import math

def length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2

def areaWithinAngle(a):
    return math.pi * a / 360

def areaOfTriangle(x1, y1, x2, y2, x3, y3):
    return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x3 * y2 - x2 * y1) * .5

def innerAngleFromPoint(x, y):
    n = (2 - length(x, y, 1, 0) ** 2) / 2
    return math.degrees(math.acos(n))

def lowerLArea(x, y):
    roundArea = areaWithinAngle(innerAngleFromPoint(x, y))
    cutArea = roundArea - areaOfTriangle(1, 1, x, y, 1, 0)
    return areaOfTriangle(0, 0, x, y, 1, 0) - cutArea

def ratio(x, y):
    l = lowerLArea(x, y)
    return l / lowerLArea(0, 1)

def pointForCircles(n):
    m = 1.0 / n
    x1, x2 = quadratic(1 + m * m, -2 - 2 * m, 1)
    y1 = m * x1
    y2 = m * x2
    return x2, y2

r = .5
n = 1
while r > .001:
    n += 1
    x, y = pointForCircles(n)
    r = ratio(x, y)

print (n)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 10,   --------------------------')
t1  = time.time()

# ==== Sun, 22 Jan 2017, 05:12, ving, USA
# In the pretty picture above, D = (D+C+A) - (B+C+A) + B.  All three of these areas can be easily calculated:

from math import sqrt, pi, asin

L = 1 - pi/4

def f(k):
    # Returns the fraction concave / L for k = 1/n
    x = (1 + k - sqrt(2*k)) / (1 + k*k) # The intersection of (x - 1)^2 + (y - 1)^2 = 1
                                        # and y = kx
    # theta is the angle between the radii to (x, y) and (1, 0)
    sin_theta = 1 - x
    theta = asin(sin_theta)
    s = (k + (1 - k) * sin_theta - theta) / 2
    return s / L

n = 1
while f(1/n) > 0.001:
    n += 1
print(n)  # Answer: 2240

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 10, SUPER TARE SOLUTIA  --------------------------')
t1  = time.time()

# ==== Sat, 18 Feb 2017, 12:32, eidanch, Israel

from math import sqrt, asin, pi

def intersection(n):
    return (n**2 + n - sqrt(2)*n*sqrt(n))/(n**2 + 1)

def S(n):
    p = intersection(n)
    return p**2/(2*n) + (1 - p) - 0.5*(sqrt(1-(p-1)**2)*(1-p) + asin(1-p))

def ratio(n):
    return S(n)/(1 - pi/4)

def e587(r):
    n = 1
    while ratio(n) >= r:
        n *= 2
    n /= 2
    while ratio(n) >= r:
        n += 1
    return n

if __name__ == '__main__':
    print(e587(0.001))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

