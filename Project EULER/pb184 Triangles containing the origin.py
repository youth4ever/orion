#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                Triangles containing the origin         -       Problem 184

Consider the set Ir of points (x, y) with integer co-ordinates in the interior of the circle with radius r,
centered at the origin, i.e. x**2 + y**2 < r**2 .

For a radius of 2, I2 contains the nine points (0,0), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1) and (1,-1).
There are eight triangles having all three vertices in I2 which contain the origin in the interior.
Two of them are shown below, the others are obtained from these by rotation .

For a radius of 3, there are 360 triangles containing the origin in the interior and having all vertices in I3
and for I5 the number is 10600 .

How many triangles are there containing the origin in the interior and having all three vertices in I105 ?


'''
import time, zzz


# How many point inside I105 ?
def Quad_I_points(lim) :
    cnt, P  = 0, []
    for x in range(0, lim ):
        for y in range(0, lim ):
            r = (x**2+y**2)**(1/2)
            if r > lim : break
            else :
                cnt+=1
                print(str(cnt)+'.         x=', x,'     y=' ,y , '    radius = ', r,   )
                P.append((x,y))
    P.pop(0)
    print('\n',P)
    return P

def cartesian_to_barycentric(x1, y1, x2, y2, x3, y3):
    """Convert cartesian coordinates to barycentric coordinates and return all > 0.
    Reference: https://en.wikipedia.org/wiki/Barycentric_coordinate_system_(mathematics)
    """
    try :
        alpha = (((y2 - y3) * (0 - x3) + (x3 - x2) * (0 - y3)) /   ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)))
    except :
        alpha = 10**15
        ZeroDivisionError
    try :
        beta = (((y3 - y1) * (0 - x3) + (x1 - x3) * (0 - y3)) /   ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)))
    except :
        beta = 10**15
        ZeroDivisionError

    gamma = 1 - alpha - beta

    return alpha > 0 and beta > 0 and gamma > 0

def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * (-y2*x3 + y1*(-x2+x3) + x1*(y2-y3)+ x2*y3))

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

LIM = 3

Q_1 = Quad_I_points(LIM)
print('\nQuad_1 : \t',Q_1[:50] )
Q_2 = [ (-i[0], i[1] ) for i in Q_1 if i[0] != 0  ]
print('Quad_2 : \t',Q_2[:50] )
Q_3 = [ (-i[0], -i[1] ) for i in Q_1 if i[0] != 0   ]
print('Quad_3 : \t',Q_3[:50]  )
Q_4 = [ ( i[0], -i[1] ) for i in Q_1 if ( i[0] != 0  and  i[1] !=0 ) ]
print('Quad_4 : \t',Q_4[:50] )

print('\n--------------------------')

#CASE 1 - 2 points in Quad 1, 1 point in Quad 2 :
D = {}
count = 0
for i in range(len(Q_1)) :
    for j in range(i+1, len(Q_1)) :
        for k in range(len(Q_3)) :
            # print( Q_1[i] , Q_1[j] , Q_3[k] )
            # ( ax, ay), (bx, by), (cx, cy ) =  Q_1[i] , Q_1[j] , Q_3[k]
            # print( ( ax, ay), (bx, by), (cx, cy ) )
            # p = ax*by - ay*bx > 0       # Computing individual Triangles
            # q = bx*cy - by*cx > 0
            # r = cx*ay - cy*ax > 0
            # print(p, q, r)
            # count += p == q == r        # Here he uses the property that the partial areas must be either Positive or Negative

            (x1, y1), (x2, y2), (x3, y3) = Q_1[i] , Q_1[j] , Q_3[k]       # BARYCENTRIC COORDINATES
            if cartesian_to_barycentric(x1, y1, x2, y2, x3, y3):
                A = tuple(sorted(( (x1, y1), (x2, y2), (x3, y3) )))
                a1, a2, a3, a4, a5, a6 = A[0][0], A[0][1], A[1][0], A[1][1], A[2][0], A[2][1]
                Area = triangle_area( x1, y1, x2, y2, x3, y3 )
                X = (a1, a2, a3, a4, a5, a6)
                if Area == 7 :
                    print('case 1 : ' , (x1, y1), (x2, y2), (x3, y3) ,'    ' ,  Area ,  )
                if X not in D : D[X] = 1
                else : D[X]+=1

                count += 1

                # LST.append( )
    for l in range(len(Q_2)) :
        for m in range(len(Q_3)) :
            (x1, y1), (x2, y2), (x3, y3) = Q_1[i] , Q_2[l] , Q_3[m]
            if cartesian_to_barycentric(x1, y1, x2, y2, x3, y3):
                A = tuple(sorted(( (x1, y1), (x2, y2), (x3, y3) )))
                a1, a2, a3, a4, a5, a6 = A[0][0], A[0][1], A[1][0], A[1][1], A[2][0], A[2][1]
                Area = triangle_area( x1, y1, x2, y2, x3, y3 )
                X = (a1, a2, a3, a4, a5, a6)
                if Area == 7 :
                    print('case 2 : ' , (x1, y1), (x2, y2), (x3, y3) ,'    ' ,  Area   )
                if X not in D : D[X] = 1
                else : D[X]+=1
                count += 1

# @2017-03-10, 18: 00 - I left here that I must analyze why for I3 I obtain 108 results instead of 90
        # for n in range(len(Q_4)) :
        #     (x1, y1), (x2, y2), (x3, y3) = Q_1[i] , Q_2[l] , Q_4[n]
        #     if cartesian_to_barycentric(x1, y1, x2, y2, x3, y3):
        #         print('case 3 : ' ,(x1, y1), (x2, y2), (x3, y3) )
        #         count += 1


print('\nAnswer :\t', count)


print([v for k,v in  D.items() ])








t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

