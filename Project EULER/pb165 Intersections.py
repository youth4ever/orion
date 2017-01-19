#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Sat, 14 Jan 2017, 23:44
#The  Euler Project  https://projecteuler.net
'''
    Intersections           -           Problem 165

A segment is uniquely defined by its two endpoints.
By considering two line segments in plane geometry there are three possibilities:
the segments have zero points, one point, or infinitely many points in common.

Moreover when two segments have exactly one point in common it might be the case
that that common point is an endpoint of either one of the segments or of both.

If a common point of two segments is not an endpoint of either of the segments it is an interior point of both segments.

!!!!!!!!!!!!!!!!!!!!   We will call a common point T of two segments L1 and L2 a true intersection point of L1 and L2
if T is the only common point of L1 and L2 and T is an interior point of both segments.             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Consider the three segments L1, L2, and L3:

L1: (27, 44) to (12, 32)
L2: (46, 53) to (17, 62)
L3: (46, 70) to (22, 40)

It can be verified that line segments L2 and L3 have a true intersection point.
We note that as the one of the end points of L3:
(22,40) lies on L1 this is not considered to be a true point of intersection.
L1 and L2 have no common point. So among the three line segments,
we find one true intersection point.

Now let us do the same for 5000 line segments.
To this end, we generate 20000 numbers using the so-called "Blum Blum Shub" pseudo-random number generator.

s0 = 290797

sn+1 = sn×sn (modulo 50515093)

tn = sn (modulo 500)

To create each line segment, we use four consecutive numbers t_n. That is, the first line segment is given by:

                    (t1, t2) to (t3, t4)

The first four numbers computed according to the above generator should be:
            27, 144, 12 and 232.
The first segment would thus be (27,144) to (12,232).

How many distinct true intersection points are found among the 5000 line segments?

'''
import time, sys


def Blum_Blum_Shub_gen():           # EFFICIENT GENERATOR
    '''     s_0 = 290797
            s_(n+1) = s_n×s_n (modulo 50515093)
            t_n = s_n (modulo 500)                  '''
    s = 290797
    while True :
        s = pow(s, 2 , 50515093 )
        t = s % 500
        yield t

B = Blum_Blum_Shub_gen()
for i in range(12):  print(i, end=' ;  ')
print(next(B), next(B), next(B), next(B) )

def two_infinite_lines_intersection( p1, p2, p3, p4) :
    ''' Given the endpoints of two lines L1(p1,p2) and L2(p3,p4)
    find the intersection point of these two lines
    Example : two_lines_intersection( [0,1], [2,3],[2,2], [-2,2])       '''
    def line(p1, p2):
        A = (p1[1] - p2[1])
        B = (p2[0] - p1[0])
        C = (p1[0]*p2[1] - p2[0]*p1[1])
        # print('A, B, C :\t',A, B,-C)
        return A, B, -C

    L1 = line(p1, p2)
    L2 = line(p3, p4)

    def intersection(L1, L2):
        D  = L1[0] * L2[1] - L1[1] * L2[0]
        Dx = L1[2] * L2[1] - L1[1] * L2[2]
        Dy = L1[0] * L2[2] - L1[2] * L2[0]
        # print('D, Dx, Dy :\t',D, Dx, Dy)
        if D != 0:
            x = Dx / D
            y = Dy / D
            return x, y
            # return round(x, 10), round(y, 10)
        else:
            return False

    R = intersection(L1, L2)
    if R:         return R
    else:        return False


class Point:
    """    Simple class for representing a point in a Cartesian coordinate system.    """
    def __init__(self, x, y):
        """        Create a new Point at x, y.        """
        self.x = x
        self.y = y
    def translate(self, dx, dy):
        """        Translate the point by dx and dy in the x and y direction.        """
        self.x += dx
        self.y += dy
    def __str__(self):
        return("Point at [%f, %f]" % (self.x, self.y))

def onSegment(p, q, r ):
    ''' Given three colinear points p, q, r, the function checks if
         point q lies on line segment 'pr'   '''
    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
        q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)) :
       return True

    return False

def orientation(p, q ,r) :
    ''':Description:   To find orientation of ordered triplet (p, q, r).
                The function returns following values :
            :0: --> p, q and r are colinear
            :1: --> Clockwise
            :2: --> Counterclockwise
    --> See http://www.geeksforgeeks.org/orientation-3-ordered-points/   for details of below formula.  '''
    val  = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if (val == 0):  return 0   # colinear
    if (val > 0): return 1     # clock or counterclock wise
    if (val < 0): return 2

def doIntersect(p1, q1, p2, q2) :
    ''' The main function that returns true if line segment 'p1q1' and 'p2q2' intersect.
    '''
#  Find the four orientations needed for general and  special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

#  General case:
    if (o1 != o2 and o3 != o4) : return True

#  Special Cases :
#        p1, q1 and p2 are colinear and p2 lies on segment p1q1
    if (o1 == 0 and onSegment(p1, p2, q1)) : return True

#       p1, q1 and p2 are colinear and q2 lies on segment p1q1
    if (o2 == 0 and onSegment(p1, q2, q1)) : return True

#       p2, q2 and p1 are colinear and p1 lies on segment p2q2
    if (o3 == 0 and onSegment(p2, p1, q2)) : return True

#      p2, q2 and q1 are colinear and q1 lies on segment p2q2
    if (o4 == 0 and onSegment(p2, q1, q2)) : return True

    return False           # Doesn't fall in any of the above cases


def endpoint_on_line( p1, q1, p3, q3 ) :
    '''Works only if there is an intersection   '''
    # if doIntersect(p1, q1, p3, q3) :
    # Conditions when the slope is infinite :
    if (p1.x - q1.x ) ==0 :
        if (p1.x == p3.x or p1.x == q3.x):
            return True
        m1 = 1e30
    else : m1 = (p1.y - q1.y ) / (p1.x - q1.x )

    if (p3.x - q3.x ) ==0 :
        if (p3.x == p1.x or p3.x == q1.x):
            return True
        m3 = 1e30
    else : m3 = (p3.y - q3.y ) / (p3.x - q3.x )

    y = lambda x0, y0, m, x :  y0 + m*( x - x0 )
    # Test from 1-st line to the endpoints of 2-nd line
    if y(p1.x, p1.y, m1, p3.x ) == p3.y : return True
    if y(p1.x, p1.y, m1, q3.x ) == q3.y : return True
    # Test from 2-nd line to the endpoints of 1-st line
    if y(p3.x, p3.y, m3, p1.x ) == p1.y : return True
    if y(p3.x, p3.y, m3, q1.x ) == q1.y : return True

    # print( m1, m3, p3.x , '    ', y(p1.x, p1.y, m1, p3.x ), p3)
    # print( y(p1.x, p1.y, m1, p3.x ) == p3.y, p3.x  )
    return False

print('\n--------------------------TESTS------------------------------')


################
t1  = time.time()


p1 , q1 = Point (12, 32) , Point( 27, 44)
p2 , q2 = Point(46, 53) , Point(17, 62)
p3,  q3 =  Point(22, 40) ,  Point(46, 70)
p4,  q4 =  Point(2, 2) ,  Point(10, 10)
p5,  q5 =  Point(5, 5) ,  Point(15, 15)
p6,  q6 =  Point(3, 1) ,  Point(9, 8)

# print( two_lines_intersection( 27, 44, 12, 32) )
print( ' L1 & L2 two_lines_intersection test : ', doIntersect( p1, q1, p2, q2)   )
print( ' L2 & L3 two_lines_intersection test : ', doIntersect( p2, q2, p3, q3)   )
print( ' L1 & L3 two_lines_intersection test : ', doIntersect( p1, q1, p3, q3) )
print( ' L2 & L3 two_lines_intersection test : ', doIntersect( p4, q4, p5, q5)  )
print( ' L2 & L3 two_lines_intersection test : ', doIntersect( p4, q4, p6, q6) ,'\n\n'    )



print('Endpoint_on_line( p1, q1, p3, q3 ) Test: \t  ',  endpoint_on_line( p1, q1, p1, q1 ))
print('Endpoint_on_line( p1, q1, p3, q3 ) Test: \t  ',  endpoint_on_line( p4, q4, p5, q5 ))
print('Endpoint_on_line( p1, q1, p3, q3 ) Test: \t  ',  endpoint_on_line( p4, q4, p6, q6 ))

print( '\n onSegment Check  if are colinear : p, q, r : \t' , onSegment ( p1 , q1 ,p2 ) , p1, q1, p2 )      # False POSITIVE !!!!! Function NOT OK !!!
print( 'onSegment Check  if are colinear : p, q, r : \t' , onSegment ( p1 , q1 , q2 ) )
print( 'onSegment Check  if are colinear : p, q, r : \t' , onSegment ( p1 , q1 , q3 ) , p1 , q1 , q3 )
print( 'onSegment Check  if are colinear : p, q, r : \t' , onSegment ( p1 , q1 , p3 ) )
print( 'onSegment Check  if are colinear : p, q, r : \t' , onSegment ( p2 , q2 , p3 ) )
print( 'onSegment Check  if are colinear : p, q, r : \t' , onSegment ( p2 , q2 , p3 ) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------TESTS------------------------------')

t1  = time.time()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def first_solution(up_limit ) :
    POINTS = set()
    SEGM = []
    G = Blum_Blum_Shub_gen()

    for i in range(up_limit//4) :
        x1, y1, x2, y2 = next(G), next(G), next(G), next(G)
        p1, p2 = (x1, y1), (x2, y2)
        SEGM.append([ p1, p2 ])
        # SEGM.append( ( x1, y1, x2, y2 ) )
    print(len(SEGM) ,SEGM[:10])

    counter, itr, h = 0, 0, 1
    for x in range(len(SEGM)+1):
        for y in range(x+1, len(SEGM)):
            itr+=1
            p1 , q1 = Point (SEGM[x][0][0], SEGM[x][0][1]  ) , Point (SEGM[x][1][0], SEGM[x][1][1] )
            p2 , q2 = Point (SEGM[y][0][0], SEGM[y][0][1]  ) , Point (SEGM[y][1][0], SEGM[y][1][1] )
            # p2 , q2 = Point(46, 53) , Point(17, 62)
            if doIntersect( p1, q1, p2, q2 ) == True :
                if endpoint_on_line( p1, q1, p2, q2 ) == False :
                    counter += 1
                    r1 , s1 = SEGM[x][0] , SEGM[x][1]
                    r2 , s2 = SEGM[y][0] , SEGM[y][1]
                    P = two_infinite_lines_intersection( r1, s1, r2, s2  )
                    POINTS.add(P)
                    # print(str(counter)+".  ",SEGM[x],SEGM[y] , r1, s1, r2, s2, P )

            if itr*100 // 12497500  > h-1 :        # Progress Bar #
                h += 1
                sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold
                # sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(100-h) +']' )         #  Calibri, Adjust the numbers, for the font of your configuration
                # sys.stdout.flush()

    print('\nThe total number of INTERSECTIONS is : \t ', counter)
    return print('\nANSWER : DISTINCT  INTERSECTIONS  : \t ', len(POINTS))        # ANSWER : The DISTINCT  INTERSECTIONS is : 	  2868868

    ##  TOTAL ( Reapeating)  number of INTERSECTIONS is : 	  2868997
    # The DISTINCT  INTERSECTIONS is : 	  2868868       round 10 and without rounding

first_solution(up_limit = 20000)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')                # Completed in : 243.9 s


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, NOT WORKING  --------------------------')
t1  = time.time()

# ==== Sat, 7 Jan 2017, 22:28, gjanee, USA
# Python, about 30 seconds.

# Brute force with one optimization: we sort the segments in order of
# X coordinate, which allows us to stop testing for intersections
# earlier.  Had the problem size been larger, a sweep line algorithm
# such as Bentley-Ottmann would have been necessary.
#
# A C++ version of this program finished in a few seconds, but getting
# this Python version to finish in under a minute was a challenge.
# Two further optimizations were required: first, considerable time
# was saved by inserting structured (but simple) integers into the set
# of intersection points instead of tuples.  Second, we eschewed
# Python's built-in fractions module.
#
# Our line segment intersection test is based on the following
# analysis.  Consider line segments defined by vector endpoints p and
# p+r, and q and q+s.  We seek scalar t and u such that
# p + tr = q + us.  Furthermore, for the intersection to be a true
# intersection point, it must be that 0 < t,u < 1.  Use X to denote
# the cross product.  If rXs = 0, the line segments are parallel
# (collinear or not) and thus there can be no true intersection point,
# so we consider only the case rXs != 0.  Cross both sides with s so
# that (noting that sXs = 0), pXs + t*(rXs) = qXs, or
# t = (q-p)Xs / rXs.  Similarly, u = (p-q)Xr / sXr, but since
# rXs = -sXr, we can write u = (q-p)Xr / rXs.

def not_ok_solution():
    M = 1000000000 # upper bound on fraction components

    def gcd (a, b):
      while b != 0:
        a, b = b, a%b
      return a

    segments = []
    s = 290797
    for i in range(5000):
      s = (s*s)%50515093
      t1 = s%500
      s = (s*s)%50515093
      t2 = s%500
      s = (s*s)%50515093
      t3 = s%500
      s = (s*s)%50515093
      t4 = s%500
      if t1 <= t3:
        segments.append((t1, t2, t3, t4))
      else:
        segments.append((t3, t4, t1, t2))

    segments.sort(key=lambda s: s[0])

    def intersects (a, b):
      # Determines if two line segments intersect, but only in the limited
      # sense of this problem.  The collinear case is not handled, for
      # example, because it is not needed.  Returns the intersection point
      # as a pair (x, y), each of which is a fraction represented as a
      # pair (numerator, denominator), or None.
      rxs = (a[2]-a[0])*(b[3]-b[1]) - (a[3]-a[1])*(b[2]-b[0])
      t = (b[0]-a[0])*(b[3]-b[1]) - (b[1]-a[1])*(b[2]-b[0])
      u = (b[0]-a[0])*(a[3]-a[1]) - (b[1]-a[1])*(a[2]-a[0])
      if (rxs > 0 and 0 < t and t < rxs and 0 < u and u < rxs) or\
        (rxs < 0 and rxs < t and t < 0 and rxs < u and u < 0):
        n = a[0]*rxs + t*(a[2]-a[0])
        cd = gcd(n, rxs)
        x = (n/cd, rxs/cd)
        assert x[0] < M and x[1] < M
        n = a[1]*rxs + t*(a[3]-a[1])
        cd = gcd(n, rxs)
        y = (n/cd, rxs/cd)
        assert y[0] < M and y[1] < M
        return (x, y)
      else:
        return None

    intersections = set()

    for i in range(len(segments)):
      for j in range(i+1, len(segments)):
        if segments[j][0] > segments[i][2]: break
        I = intersects(segments[i], segments[j])
        if I:
          # To save time, convert the intersection point to a single,
          # unique integer.
          intersections.add(((I[0][0]*M+I[0][1])*M+I[1][0])*M+I[1][1])

    return print (len(intersections))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 2, VERY SIMPLE ,1 min --------------------------')
t1  = time.time()

# ==== Tue, 14 May 2013, 16:40, tom.wheldon, England
# Straightforward unoptimised implementation of a standard algorithm - runs in 36 seconds in Python.
# I eliminated duplicates by throwing intersection points into a set (wasteful - I know).
# Equality testing on floating point numbers is always a bit problematic - quite a few people seem to have run into problems.
# Using 15 digit precision floats I rounded to 10 places after the decimal point.
# The integer part takes a maximum of three digits and I allowed two digits for rounding errors.
# I then checked to see if the answer changed if the floats were rounded to 8 places or 12 places - it didn't,
# which gives confidence in the result (though not as much as checking the answer).

def solution1():
    N = 5000

    def intersect(i,j):
        x1,y1,x2,y2 = segs[i]
        x3,y3,x4,y4 = segs[j]
        d = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
        if d == 0:
            return 0
        ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3))/d
        ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3))/d
        if 0 < ua < 1 and 0 < ub < 1:
            return (round(x1 + ua*(x2-x1),10), round(y1 + ua*(y2-y1),10))
        else:
            return 0

    segs = []
    n = 290797
    for i in range(N):
        c = []
        for j in range(4):
            n = n*n % 50515093
            c.append(n%500)
        segs.append(c)

    points = set()
    for i in range(N-1):
        for j in range(i+1,N):
            p = intersect(i,j)
            if p:
                points.add(p)

    return print(len(points))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 3,  2 min --------------------------')
t1  = time.time()

# ====== at, 30 Aug 2014, 19:59, manoloku, Argentina
#
# The idea is to find 0<l<1 and 0<m<1 such that:
# a+l(b-a)=c+m(d-c).
# This is a system of 2 equations (one for component x and one for component y),
# I solved with determinants, so I can say if the lines are parallel or not easily.
# I did it with only integers, storing the intersections (in the form numerator and denominator) in a set.

def solution3():
    def det(m11,m12,m21,m22):
      return m11*m22-m21*m12

    def mcd(a,b):
      while b:
        a, b = b, a%b
      return a

    s=290797
    t=[]
    for i in range(0,20000):
      s=(s*s)%50515093
      t.append(s%500)

    segmentos=5000
    intersecciones=set()
    for i in range(0,(segmentos*4)-4+1,4):
      a=(t[i],t[i+1])
      b=(t[i+2],t[i+3])
      for j in range(i+4,(segmentos*4)-4+1,4):
        c=(t[j],t[j+1])
        d=(t[j+2],t[j+3])

        dtot=det(b[0]-a[0],c[0]-d[0],b[1]-a[1],c[1]-d[1])
        if  dtot==0: continue #Descarto segmentos paralelos

        detl=det(c[0]-a[0],c[0]-d[0],c[1]-a[1],c[1]-d[1])
        detm=det(b[0]-a[0],c[0]-a[0],b[1]-a[1],c[1]-a[1])


        #Descarto si detl o detm tienen distinto signo que dtot
        if dtot<0:
          if detl>0: continue
          if detm>0: continue
        if dtot>0:
          if detl<0: continue
          if detm<0: continue
        #Descarto si la interseccion se da al principio o final del segmento
        if detl==0 or detm==0: continue
        if detl==dtot or detm==dtot: continue

        #Descarto si l>1 o m>1
        if abs(detl)>abs(dtot): continue
        if abs(detm)>abs(dtot): continue

        intxN=a[0]*dtot+(b[0]-a[0])*detl
        intyN=a[1]*dtot+(b[1]-a[1])*detl
        mcdx=mcd(intxN,dtot)
        mcdy=mcd(intyN,dtot)
        intersecciones.add((intxN//mcdx,dtot//mcdx,intyN//mcdy,dtot//mcdy))

    return print(len(intersecciones))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 4,  VERY SLOW --------------------------')
t1  = time.time()

# ==== Fri, 24 May 2013, 14:53, bobrovsky.serj, Russia
# Using python Fractions is a bit slow (compared with float), handmade lib would be bulky, so…160 sec.

from fractions import Fraction

def euler165():
    l, s = [], 290797
    for i in range(5000):
        ll = []
        for j in range(4):
            s = s * s % 50515093
            ll.append(s % 500)
        ax, ay, bx, by = ll
        l.append((ax, ay, bx, by, bx - ax, by - ay))

    points = set()
    for i in range(1, len(l)):
        ax, ay, bx, by, ABX, ABY = l[i]
        for j in range(i):
            cx, cy, dx, dy, CBX, CBY = l[j]
            den = ABX * CBY - CBX * ABY
            if den != 0:
                u, v = (cx - ax) * CBY - (cy - ay) * CBX, (cx - ax) * ABY - (cy - ay) * ABX
                if den < 0:
                    u, v, den = -u, -v, -den
                if 0 < u < den and 0 < v < den:
                    points.add((Fraction(ax * den + ABX * u, den), \
                                Fraction(ay * den + ABY * u, den)))

    return len(points)

# print(euler165())

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 5,  2 min --------------------------')
t1  = time.time()

# ==== Sat, 19 Mar 2011, 19:22, Bo, USA
#
# With more than 5,000 segments a sweep algorithm would have been necessary.
# Without that, it was pretty straightforward application of parameterizing the two segments,
# solving for their intersection point, and making sure that point was contained on both segments.

def BO() :
    from gmpy2 import mpq
    from itertools import combinations

    # Blum Blum Shub random number generator
    def bbs_prng(s=290797, m_s=50515093, m_t=500):
      while 1:
        s = (s * s) % m_s
        yield s % m_t

    N_segments = 5000
    A_segments = []
    # Generate the starting and ending points of the segments
    rng = bbs_prng()
    for i in range(N_segments):
      points = next(rng), next(rng), next(rng), next(rng)
      A_segments.append(points)

    answer = set()
    # Consider all distinct pairs of segments
    for seg_1, seg_2 in combinations(A_segments, 2):
      # Get the endpoints of a pair of segments
      a_x, a_y, b_x, b_y = seg_1
      c_x, c_y, d_x, d_y = seg_2
      # Compute each of their slopes
      m_1 = "undefined" if (b_x == a_x) else mpq(b_y - a_y, b_x - a_x)
      m_2 = "undefined" if (d_x == c_x) else mpq(d_y - c_y, d_x - c_x)
      # In Euclidean geometry, two lines with the same slope can never intersect
      if m_1 == m_2:
        continue
      # Parameterize the line segments as follows. The s (or t) parameter goes
      # from 0 to 1, with 0 being the starting point of the segment and 1 being
      # the ending point.
      # L_1(s) = (1 - s) * a + s * b
      # L_2(t) = (1 - t) * c + t * d
      # Solve L_1(s) = L_2(t). Since there are x and y components of both, this is
      # a linear system that can be solved for s and t.
      s_n = (a_x - c_x) * d_y + (c_y - a_y) * d_x - a_x * c_y + a_y * c_x
      s_d = (a_x - b_x) * d_y + (b_y - a_y) * d_x + (b_x - a_x) * c_y + (a_y - b_y) * c_x
      s = mpq(s_n, s_d)
      # If the intersection is beyond line segment 1, don't count it.
      if not (0 < s < 1):
        continue
      t_n = -a_x * (c_y - b_y) - b_x * (a_y - c_y) - (b_y - a_y) * c_x
      t_d = a_x * (d_y - c_y) + b_x * (c_y - d_y) + (b_y - a_y) * d_x + (a_y - b_y) * c_x
      t = mpq(t_n, t_d)
      # If the intersection is beyond line segment 2, don't count it.
      if not (0 < t < 1):
        continue
      x = a_x + s * (b_x - a_x)
      y = a_y + s * (b_y - a_y)
      answer.add((x, y))

    return len(answer)

BO()

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

