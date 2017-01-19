#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Investigating multiple reflections of a laser beam      -       Problem 144
In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam.
The beam enters the cell, bounces around on the mirrors, and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation 4* x**2 + y**2 = 100

The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing the light to enter and exit through the hole.

The light beam in this problem starts at the point (0.0,10.1)
just outside the white cell, and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse,
it follows the usual law of reflection "angle of incidence equals angle of reflection."
That is, both the incident and reflected beams make the same angle with the normal line at the point of incidence.

In the figure on the left, the red line shows the first two points of contact between the laser beam and the wall of the white cell;
the blue line shows the line tangent to the ellipse at the point of incidence of the first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is: m = −4x/y

The normal line is perpendicular to this tangent line at the point of incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before exiting?
'''
import time
import numpy as np


def get_quadratic_roots(a, b, c ) :
    return np.roots([ a ,b , c])

def in_ellipse(x, y):
    if  100 - (4* x**2 + y**2) >= 0 :
        return True
    else : return False

def line_equation_two_points ( p1, p2) :
    ''':Description: function which returns the coefficients m & y_0 of a line equation
    :param p1: tuple with two arguments x1, y1
    :param p2: tuple with two arguments x2, y2
    :return: tuple : with three coefficients, x_0, y_0, m - the slope : y = y_0+m( x-x0 )
    :Example: line_equation_two_points( (2,0), (1,-1)  )
    '''
    m =  ( p2[1] - p1[1] ) / ( p2[0] - p1[0] )
    return ( p1[0], p1[1], m  )


# print('Function in_ellipse Testing :', in_ellipse(2, 2 ))
# print('Function in_ellipse Testing :', in_ellipse( 4 , 9 ))
# print('Function in_ellipse Testing :', in_ellipse(0.1, 9.95 ))
# print('Function in_ellipse Testing :', in_ellipse(0, 10 ))


print('\nFunction get_quadratic_roots Testing :', get_quadratic_roots(201.96,-284.214, 2.01 ) )

print('\nFunction line_equation_two_points Testing :', line_equation_two_points( (0.0, 10.1), (1.4, -9.6) )  )

ellipse_coeffs = [4, 1, -100]
line_coeffs = line_equation_two_points( (0.0, 10.1), (1.4, -9.6) )
line_coeffs = (0, 10.1, -14.07142857)

def line_ellipse_next_intersection( line_coeffs , ellipse_coeffs ):
    '''     Ellipse in standard form : a*x**2 + b*y**2 - c =0  --> (p, q, o).
    This is just a simple standard Ellipse straight and centered at (0,0).
        Line in standard form : y = y_0 + m* (x - x_0)       (  x_0, y_0, m )   --> ( a, b ,c )
    point1 - tuple with two arguments, the starting (initial) point of the line (x0, y0)

    :return: tuple with two arguments: the second point of intersection with the ellipse
    '''
    x0, y0 , m  = line_coeffs[0], line_coeffs[1], line_coeffs[2]
    a, b, c = ellipse_coeffs[0], ellipse_coeffs[1], ellipse_coeffs[2]

    quadratic =  get_quadratic_roots( a+b*m**2 ,  2*b*m*(y0-m*x0) , b*(y0**2 - 2*m*x0*y0 + (m*x0)**2 )+c )
    x1, x2 = quadratic[0], quadratic[1]

    if abs( x1-line_coeffs[0] ) < 1e-5 :     x = x2           # Here we need to calculate the y only
    else : x = x1                                                         # for the 2-nd point

    y = lambda x :  y0 + m*( x - x0 )

    return x, y(x)

print('\nFunction line_ellipse_next_intersection Testing :', line_ellipse_next_intersection( line_coeffs , ellipse_coeffs ) )

def ellipse_tangent_slope( x , y ) :
    '''     :Returns: the derivative (slope m) of an ellipse at a given point (x,y)
    :param x: int, x-coord of the hitting point
    :param y: int, y-coord of the hitting point
    :return: slope m of that point of the ellipse, the derivative of an ellipse at a point
    '''
    ellipse_coeffs = [4, 1, -100]       # Characteristics of the ellipse, x-coeff, y-coeff and admin coeff
    a, b, c = ellipse_coeffs[0], ellipse_coeffs[1], ellipse_coeffs[2]
    m = (- a* x )/ ( b* y )
    return m

print('\nFunction ellipse_tangent_slope Testing :', ellipse_tangent_slope(1.4 , -9.6 ) )

def get_quadrant( x, y ) :
    if x > 0 and y > 0 : return 1
    if x < 0 and y > 0 : return 2
    if x < 0 and y < 0 : return 3
    if x > 0 and y < 0 : return 4

print('\nArctangent Testing :\t',   np.arctan( 1 )* 180/ np.pi )
print('Arctangent Testing :\t',  np.arctan(0.5833)* 180/ np.pi )
print('Arctangent Testing :\t',   np.arctan( -14.07 )* 180/ np.pi )

print('\nFunction get_quadrant Testing :', get_quadrant(1.4 , -9.6 ),'\n' )

def get_exit_line_slope( tan_slope, m_in, quadrant ) :
    t_a = np.arctan(tan_slope) * 180/ np.pi
    if quadrant == 1  :
        if m_in > 0 :
            a_in = ( np.arctan(m_in)* 180/ np.pi )- 180
            da = abs(a_in) - abs(t_a)
            a_out = t_a + 180 + da
        if m_in < 0 :
            a_in = ( np.arctan(m_in)* 180/ np.pi )
            da = abs(t_a) - abs(a_in)
            a_out = t_a - da

    if quadrant == 2  :
        if m_in > 0 :
            a_in = ( np.arctan(m_in)* 180/ np.pi )
            da =  abs(t_a) - abs(a_in)
            a_out = t_a - 180 + da

        if m_in < 0 :
            t_a = t_a-180
            a_in = ( np.arctan(m_in)* 180/ np.pi )
            da = abs(t_a) - abs(a_in)
            a_out = t_a +180 - da

    if quadrant == 3  :
        if m_in > 0 :
            t_a = t_a + 180
            a_in = ( np.arctan(m_in)* 180/ np.pi )
            da =  abs(t_a) - abs(a_in)
            a_out = t_a - 180 + da

        if m_in < 0 :
            a_in = ( np.arctan(m_in)* 180/ np.pi )
            da = abs(t_a) - abs(a_in)
            a_out = t_a +180 - da

    if quadrant == 4  :
        if m_in > 0 :
            t_a = t_a - 180
            a_in = ( np.arctan(m_in)* 180/ np.pi ) -180
            da =   abs(a_in) - abs(t_a)
            a_out = t_a + 180 + da

        if m_in < 0 :
            a_in = ( np.arctan(m_in)* 180/ np.pi ) +180
            da = abs(a_in) - abs(t_a)
            a_out = t_a - 180 - da

    m_out = np.tan( a_out * np.pi / 180 )
    # print( '\nIN :  ', tan_slope, m_in, quadrant ,'Tan angle: ', t_a,' ,  In angle :  ' ,a_in ,' , Diff :  ' , da ,' OUT angle:  ',a_out,' ,  Out slope:  ' ,m_out, '   quadr:  ' ,quadrant )

    return m_out


###         QUADRANT  I    ####
# print('Function get_exit_line_slope Testing :', get_exit_line_slope(-2, 3,  1 ) )
# print('Function get_exit_line_slope Testing :', get_exit_line_slope(-2, -0.333333333333,  1 ) )
###         QUADRANT  II    ####
# print('Function get_exit_line_slope Testing :', get_exit_line_slope(2, 1/2, 2 ) )
# print('Function get_exit_line_slope Testing :', get_exit_line_slope(2, -5.5, 2 ) )
###         QUADRANT  III    ####
# print('Function get_exit_line_slope Testing :', get_exit_line_slope(-2, 3, 3 ) )
# print('Function get_exit_line_slope Testing :', get_exit_line_slope(-2, -0.333333333333, 3 ) )

###         QUADRANT  IV    ####
print('Function get_exit_line_slope Testing :', get_exit_line_slope(2, 1/2, 4 ) )
print('Function get_exit_line_slope Testing :', get_exit_line_slope(2, -5.5, 4 ) )
#### SUPER, is working  @ 2017-01-16, 22:09



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def multiple_reflections() :
    ellipse_coeffs = [4, 1, -100]
    line_coeffs = line_equation_two_points( (0.0, 10.1), (1.4, -9.6) )
    # line_coeffs = (0, 10.1, -14.07142857)
    m_in = -14.07142857
    counter = 0
    # for i in range(12) :
    while True :
        X = line_ellipse_next_intersection( line_coeffs , ellipse_coeffs )
        quadrant = get_quadrant( X[0], X[1] )
        tangent = ellipse_tangent_slope( X[0], X[1])
        ray_in_slope = line_coeffs[2]
        m_out = get_exit_line_slope (tangent , ray_in_slope, quadrant)
        counter += 1
        # print('\n'+str(counter) +'.   Hit point :   ',X ,' ,   Tangent slope: ' ,tangent, ' , Ray In Slope:  ',m_in , ' , Ray Out Slope:  ', m_out, '\n Line coefficients : \t', line_coeffs)
        m_in = m_out
        line_coeffs = ( X[0] , X[1] , m_in )

        if -0.01 < X[0] < 0.01 and X[1] > 9 :
            return print('\n\n Let there be light !  : \t\t : ', counter-1)

multiple_reflections()          # Answer : 354


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          #   Completed in : 72.00408 ms

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()




# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

##############  GENERAL IDEAS   ##########

# =====Fri, 23 Oct 2015, 00:06, demongolem, USA
# Solved purely by excel.  In fact, I think it is actually a far bit easier in excel than say Java which I conventioned to.
# The off by one error is the least of one's worries.  If one comes that far, they have it.
#
# So the mathematical insights I used were as follows:
#
# Always have 3 slopes at each iteration: incidence, tangent and reflection.
# We get the initial incidence slope by giving us the two initial points.
# The normal is always the same and it acts as a line to simplify things.
# In fact, we really should not have been given that, that was a little bit too baby.
# It's like, oh let's not expose these poor saps to the slightest bit of calculus, it will blow their minds!.
# Then the key to problem is figuring out the slope for the reflection line.  This is:
#
# m_r = (2 * m_t - m_i * (1 - m_t^2)) / (1 - m_t^2 + 2 * m_t * m_i)
#
# Using that and the original ellipse equation, we are able to solve a quadratic equation for x
# and then substitute for y to get the next reflection point and we start the cycle anew
# to find the next slope of reflection line.  Of course, with quadratic equations,
# there are always 2 solutions and it turns out one of them is the point we are currently at,
# so we are able to very simply choose the other (x,y) as the correct one to go to.


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# Uncomment all lines below to produce an interactive plot

# import numpy as np
# import matplotlib.pyplot as plt

import math

u,v = 0, 10.1
x,y = 1.4, -9.6

hits = 0

# plt.ion()
# t = np.arange(0.0, 6.28, 0.05)
# plt.plot(5 * np.cos(t), 10 * np.sin(t), 'k')
# plt.axes().set_aspect('equal', 'datalim')

def next(one, two):
  u, v = one
  x, y = two

  # plt.plot((x,u), (y,v), 'r')
  # print(hits, end=" ")
  # input()

  b1, b2 = (u-x, v-y)
  mb = math.sqrt(b1**2 + b2**2)

  c1, c2 = (y*mb/(4*x*b2 - y * b1), -4*x*mb/(4*x*b2 - y * b1))

  r = -c1 * c2 - math.sqrt(c1**2 + c2**2 - 1)
  r /= (c1**2 - 1)

  a2 = -(8*r*x+2*y)/(4*r**2 + 1)
  a1 = r*a2

  return (a1 + x, a2 + y)

while True:
  temp = next((u,v),(x,y))
  u,v = x,y
  x,y = temp

  hits += 1
  if -.01 <= x and x <= .01 and y > 0:
    print(hits)
    break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  VERY SIMPLE --------------------------')
t1  = time.time()

# ===== Sun, 13 Dec 2015, 21:05, dw98, USA
# I, too, used vectors and was worried about error propagation but found that I did not have to worry about it.

count = 0
x0, y0 = 0.0, 10.1
x1, y1 = 1.4, -9.6
while y1 < 9.9 or abs(x1) > 0.01:
    vix, viy = x1 - x0, y1 - y0  #These are the components of the incident light ray as a vector with x0, y0 as the origin
    lx, ly = 4. * x1, y1 # The components of the normal line to the surface (Reflected across)
    lDotl, viDotl = lx**2 + ly**2, vix*lx + viy*ly    #Dot products
    vrx, vry = 2. * viDotl/lDotl * lx - vix, 2. * viDotl/lDotl * ly - viy   #Vector for the reflection
    mr = vry / vrx
    b = y1 - mr * x1    #equation for the reflection line
    x2 = (-2 * mr * b + ((2 * mr * b)**2 - 4*(mr**2 + 4)*(b**2 - 100))**.5) / (2*(mr**2 + 4))     #Simultaneous solution by substitution of the the two equations -- line of reflection and the ellipse
    if abs(x2 - x1) < 0.00001:  #if the first solution to the quadratic is identical to the point of reflection, choose the other solution:
        x2 = (-2 * mr * b - ((2*mr*b)**2 - 4*(mr**2+4)* (b**2-100))**.5) / 2 / (mr**2 + 4)

    x0, y0, x1, y1 = x1, y1, x2, mr * x2 + b    #Forward the variables for the next iteration.
    count += 1
print(count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Sun, 1 Feb 2015, 03:40, DanGoldbach, England
# Pure geometry, no linear algebra. Pretty horrific. If it didn't work on my first try, I don't think I could debug this.


""" ewww """
from math import tan, atan, degrees, sqrt

def get_p3a(a, b, m, c):
    x = ((-a*a*c*m)/(b*b+a*a*m*m) +
         a * sqrt((b*b-c*c)/(b*b+a*a*m*m) +
                  ((a*a*c*c*m*m)/(b*b+a*a*m*m)**2)))
    y = m*x + c
    return x,y

def get_p3b(a, b, m, c):
    x = ((-a*a*c*m)/(b*b+a*a*m*m) -
         a * sqrt((b*b-c*c)/(b*b+a*a*m*m) +
                  ((a*a*c*c*m*m)/(b*b+a*a*m*m)**2)))
    y = m*x + c
    return x,y

def find_g(p1, p2, m):
    phi = atan((p2[1]-p1[1]) / (p2[0]-p1[0]))
    alpha = atan(m)
    theta = phi - alpha
    return tan(phi - 2*theta)

def next_m(p2x, p2y):
    return -4*p2x/p2y

def same_point(p1, p2):
    return (abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) < 1e-8)

def next_point(p1, p2):
    m = next_m(p2[0], p2[1])
    g = find_g(p1, p2, m)
    p3a = get_p3a(5, 10, g, -g*p2[0]+p2[1])
    p3b = get_p3b(5, 10, g, -g*p2[0]+p2[1])
    return p3a if not same_point(p3a, p2) else p3b

count = 0
p1, p2 = (0.0, 10.1), (1.4, -9.6)
while not (-0.01 <= p2[0] <= 0.01 and -9.99 <= p2[1] <= 10.01):
    p1, p2 = p2, next_point(p1, p2)
    count += 1
print(count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   ELEGANT--------------------------')
t1  = time.time()

# ==== Fri, 14 Oct 2016, 13:59, drymonade, Russia

def calc(x1, y1, x2, y2):
    k1 = (y2 - y1) / (x2 - x1)
    k2 = y2 / (4*x2)
    k3 = (2*k2 - k1 + k1*k2*k2) / (2*k1*k2 - k2*k2 + 1)
    b3 = y2 - k3*x2
    d = 400 + 100*k3*k3 - 4*b3*b3
    x11 = (-k3*b3 + d**0.5) / (4 + k3*k3)
    x22 = (-k3*b3 - d**0.5) / (4 + k3*k3)
    x3 = 0
    y3 = 0

    if abs(x11 - x2) < abs(x22 - x2):
        x3 = x22
    else:
        x3 = x11

    y3 = k3*x3 + b3

    return x3, y3

x1 = 0.0
y1 = 10.1
x2 = 1.4
y2 = -9.6
x3 = 1
y3 = 0
counter = 0

while(abs(x3) >= 0.01 or y3 < 0):
    counter += 1
    x3, y3 = calc(x1, y1, x2, y2)
    # print(x3, y3)
    x1, y1 = x2, y2
    x2, y2 = x3, y3

print(counter)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ==== Mon, 6 Apr 2015, 08:02, stysis, Australia
# I enjoyed that one! The solution came quite quickly once I worked out how to do the geometry.
#
# Like rjsam on 25 Feb 2015, I also graphed the path of the laser - but I was very impressed
# with the GIF frank44 posted on 4 Sep 2014. Kudos to you!
#
# Here's my Python code of under 20 lines which runs in 0.03 seconds on my i3 at 3.10 GHz.
# It took me a moment to realise why my first output of 355 was wrong -
# of course the the last laser path doesn't hit the mirror. Doh!

import time, math

start = time.time()
o,d = [0,10.1],[1.4,-9.6] # Origin and first destination
hits = 1
while not all((-0.01 < d[0] < 0.01, d[1] > 0)):
    # Calculate the gradient of input laser
    m1 = (o[1]-d[1])/(o[0]-d[0])
    # Calculate the gradient of the tangent at the point of contact
    tangentm = -4*d[0]/d[1]
    # calculate the gradient of the reflected laser
    m2 = -math.tan(math.atan(m1) - 2*math.atan(tangentm))
    # calculate the y intercept for the reflected laser
    c = d[1] - m2*d[0]
    # Make the old destination be the new origin
    o[0],o[1] = d[0],d[1]
    # calculate the 2 x-intercepts between the new laser path and the ellipse
    x1 = (-2*m2*c + ((2*m2*c)**2 - 4*(4+m2**2)*(c**2-100))**0.5)/(8+2*m2**2)
    x2 = (-2*m2*c - ((2*m2*c)**2 - 4*(4+m2**2)*(c**2-100))**0.5)/(8+2*m2**2)
    # Find which of the x-intercepts is the new destination
    if int(d[0]*100) == int(x1*100): d[0] = x2
    else: d[0] = x1
    #Calculate the new y-intercept
    d[1] = m2*d[0] + c
    hits += 1
print(hits-1,d)
print("This took %0.3f seconds." % (time.time()-start))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ===== Sat, 27 Jun 2015, 16:27, SickMath, Mexico

import math

Sx, Sy = 0.0, 10.1
Ex, Ey = 1.4, -9.6

for bounce in range(1000) :

    if -0.01 <= Ex <= 0.01 and Ey > 0 : break

    mR = (Ey - Sy) / (Ex - Sx)
    mT = - 4 * Ex / Ey
    mN = - 1 / mT

    newTg = math.atan(mR) + 2 * (math.atan(mN) - math.atan(mR))
    newM = math.tan(newTg)
    newQ = Ey - newM * Ex

    newX = sorted([(- newM*newQ + math.sqrt(400 + 100*newM**2 - 4*newQ**2)) / (newM**2 + 4),
            (- newM*newQ - math.sqrt(400 + 100*newM**2 - 4*newQ**2)) / (newM**2 + 4)],
                  key = lambda x : abs(Ex - x))[1]

    newY = newM * newX + newQ

    Sx, Sy = Ex, Ey
    Ex, Ey = newX, newY

print (bounce)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

from math import sqrt;

x0,y0=0,10.1;
x1,y1=1.4,-9.6;k=0;
while abs(x1)>0.01 or y1<0:
	k+=1;
	beam_slope=(y1-y0)/(x1-x0);
	tan_slope=-4*x1/y1;
	q=(beam_slope-tan_slope)/(1+tan_slope*beam_slope);
	newslope=(tan_slope-q)/(1+q*tan_slope);
	#the new line is y=newslope*(x-x1)+y1=a x +b;
	a,b=newslope,y1-newslope*x1;
	sol1,sol2=(-a*b+2*sqrt(100+25*a**2-b**2))/(4+a**2),(-a*b-2*sqrt(100+25*a**2-b**2))/(4+a**2);
	x0,y0=x1,y1
	if abs(sol1-x1)>abs(sol2-x1):
		x1=sol1;
	else :
		x1=sol2;
	y1=a*x1+b;

print ("the answer is :" ,k )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# === Tue, 2 Dec 2014, 22:22, raulbc777, Paraguay
# The slope of the tangent of a ellipse is:
#
# dy/dx=d(sqrt(100−4x2))/dx
#
# dy/dx=4.2.x2sqrt(100−4x2)dy
# So, dy/dx=4xy

import math
from math import sqrt
from decimal import *
getcontext().prec = 20

def findNextPoint(m, xP, yP, count = 0):
    #print m, xP, yP
    n = Decimal(yP) - Decimal(m*xP)
    xN = Decimal(-xP) - Decimal(2*m*n)/Decimal(m**2 + 4)
    yN = Decimal(m*(xN - xP)) + Decimal(yP)
    return (xN, yN)


def findNextSlope(m, x, y):
    mT = Decimal(-4* x)/Decimal(y)
    mP = Decimal(-1)/Decimal(mT)
    tgw = Decimal(m - mP)/Decimal(1 + m*mP)
    mR = Decimal(mP - tgw)/Decimal(mP*tgw + 1)
    return mR


x0 = Decimal('0')
y0 = Decimal('10.1')
xInit = Decimal('1.4')
yInit = Decimal('-9.6')
mInit = Decimal(yInit - y0)/Decimal(xInit - x0)
mP = mInit
xP = xInit
yP = yInit
count = 0
while True:
    mN = findNextSlope(mP, xP, yP)
    (xN, yN) = findNextPoint(mN, xP, yP)
    count += 1
    if -0.01 <= xN <= 0.01:
        yA = math.sqrt(100 - 4*0.01**2)
        if yN >= yA:
            break
    xP = xN
    yP = yN
    mP = mN

print ("Number of reflections of laser beam: ",count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 9,   --------------------------')
t1  = time.time()

# === Thu, 18 Dec 2014, 06:58, lahvak, USA
# Spent couple days trying to derive a reasonable equation for a function ft1(t)
# that would receive as input a parameter value corresponding to a point P0
# and return a value of a parameter corresponding to the point P2 obtained by aiming a beam from P0
# to a point P1 corresponding to the parameter t1 and finding where the reflected beam hits the ellipse.
# I tried several different parametrizations of the ellipse, but could not find anything simple enough to be useful.
# I then gave up and solved it the simple way (pylab is used just for plotting):

# import pylab as pl                # Uncomment to also draw figures

def ipoint(x0,y0,v1,v2):
    a = 4*v1**2 + v2**2
    b = 8*x0*v1 + 2*y0*v2
    s = -b/a
    return (x0 + s*v1,y0 + s*v2)

def dot(v1,v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def nextdir(x0,y0,x1,y1):
    v1 = (x0-x1,y0-y1)
    v2 = (4*x1,y1)
    coef = dot(v1,v2)/dot(v2,v2)
    return (2*coef*v2[0] - v1[0],2*coef*v2[1] - v1[1])

def is_done(x,y):
    return y>0 and -.01 <= x <= .01

p1 = (0.0,10.1)
p2 = (1.4,-9.6)
n = 0

lx = [p1[0]]
ly = [p1[1]]

while not is_done(*p2):
    newdir = nextdir(*p1+p2)
    p1 = p2
    lx += [p1[0]]
    ly += [p1[1]]
    p2 = ipoint(*p1+newdir)
    n += 1

print(n)

# t = pl.linspace(0,2*pl.pi,500)
# x = 5*pl.cos(t)
# y = 10*pl.sin(t)
#
# pl.plot(lx,ly,x,y,'r')
# pl.axes().set_aspect('equal')
# pl.show()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

