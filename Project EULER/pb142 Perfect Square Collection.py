#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Wed, 21 Dec 2016, 00:38
#The  Euler Project  https://projecteuler.net
'''
Perfect Square Collection       -       Problem 142

Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.

'''
import time
import eulerlib, sys

print(eulerlib.primitive_triples(10))

P = eulerlib.pythagoras.triplet_gen()
for i in range(10) :

    print(next(P), end='  ')

print('\n--------------------------TESTS------------------------------')

# x + y = a       a+b = c + d ==> Find a pair of perfect squares which are equal with a different pair of perfect squares
# x − y =b
# x + z = c
# x − z = d
# y + z = e
# y − z  = f






print('\n================  My FIRST SOLUTION,  10 secs ===============\n')
t1  = time.time()


def perfect_square_collection(up_range) :
    h, cnt =0, 0

    for i in range(100, up_range) :
        for j in range(i+1 , up_range) :
            b, a = i*i , j*j
            for k in range(int(pow( (a+b),1/2)), 300,-1 ) :
                c = k*k
                d = a+b - c
                if (d**(1/2)) %1 == 0  :
                    if a !=c and a!= d and a!=b and c!=d and c > d :
                        x, y = (a+b)/2,  (a+b)/2-b
                        z = (c+d)/2 -d
                        if y > 0 and y%1 ==0  and z> 0 and z%1 ==0 and x>y>z :
                            f, g = y+z, y-z
                            if ( f**(1/2) )% 1 == 0    and ( g**(1/2) )% 1 == 0    :
                                cnt+=1
                                print('\n', str(cnt)+'.  ' ,i, j, k,d**(1/2) ,'      a, b, c, d, f, g : \t', a,b,c,d,f,g, '     ' , a+b, c+d , '   ',x, y, z )
                                return print('\n\nAnswer : \t ', int(x+y+z) , ' ;    x=' , x,' ;    y=',y , ' ;    z= ', z)

            if i*100 //up_range  > h-1 :        # Progress Bar  [######                       ]
                h += 1
                # sys.stdout.write("\r%d%%-" %h )
                sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold
                # sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(100-h) +']' )         #  Calibri, Adjust the numbers, for the font of your configuration
                # sys.stdout.flush()


# perfect_square_collection(10**3)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')




print('\n================  My SECOND SOLUTION, 5 secs  ===============\n')
t1  = time.time()



def perfect_square_collection_two(up_range) :
    h, cnt =0, 0

    for i in range(100, up_range) :
        for j in range(i+1 , up_range) :
            b, a = i*i , j*j
            x = (a+b) / 2
            if x%1 == 0 :
                y = (a+b)/2 -b
                # print( str(cnt)+'.  ' ,i, j  , '       a,b:  ', a,b,'        ' ,a+b,  '   ',x, y)
                for k in range( int(pow( (a+b),1/2)) , i , -1) :      # Can't be lower than b=i*i (lowest of the a+b sum) and bigger than sqrt(a+b)
                    c=k*k
                    d = a+b - c
                    z = (c+d)/2 -d
                    if (d**(1/2)) %1 == 0  and z> 0 : #and (a+b+c+d ) %4 == 0:
                        f, g = y+z, y- z
                        if g> 0 and ( f**(1/2) )% 1 == 0    and ( g**(1/2) )% 1 == 0    :
                            cnt+=1
                            print( str(cnt)+'.  ' ,i,j ,k, int(d**(1/2)), '       a,b,c,d,f,g:  ', a,b,c,d,f,g ,'        ' ,a+b, c+d,  '   ',x, y, z)
                            return print('\n\nAnswer : \t ', int(x+y+z) , ' ;    x=' , x,' ;    y=',y , ' ;    z= ', z)




perfect_square_collection_two(10**3)



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ===== Mon, 15 Feb 2016, 03:21, plivesey
# Some nasty Python ahead! Guessed that the solution would be somewhere within the first 1000 squares.
# Calculated the mid point between all possible pairs of squares and the distance from this mid point to either square.
#
# We know that x must be the mid point of at least two different pairs of squares, y is the mid point of at least a pair of squares
# and that the distance from y to the square is the same as that from x to its other pair of squares.
# 0.7 secs on an 8 year old Mac Pro.


num = 1000
squares = []
possible_x = {}
for i in range(0, num):
    squares.append(i**2)

for x in range(1, num):
    for y in range(x + 1, num):
        diff = (squares[y] - squares[x])
        if diff % 2 == 0:
            diff /= 2
            mid = squares[x] + diff
            if mid in possible_x:
                possible_x[mid].append(diff)
            else:
                possible_x[mid] = [diff]

for x in sorted(possible_x):
    if len(possible_x[x]) > 1:
        for y in possible_x[x]:
            if y in possible_x:
                possible_z = possible_x[y]
                for z in possible_z:
                    if z in possible_x[x]:
                        print (x, y, z, x + y + z)
                        break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ===== Fri, 28 Aug 2015, 02:00, DrLock, England
# x+y=a**2, x−y=b**2, x+z=c**2, x−z=d**2, y+z=e**2, y−z=f**2,
#
# We get: a**2=c**2+f**2,  a**2=d**2+e**2,  c**2=b**2+e**2
#
# Algorithm:
#  - Generate all Pythagorean triples (α**2+β**2=γ**2) up to 'limit'
#  - Find three triples α_1**2+β_1**2=γ_1**2,  α_2**2+β_2**2=γ_2**2, α_3**2+β_2**2 = β_3**2, such that:
#     * γ_1=γ_2
#     * β_2>α_1,α_2,β_1
#     * γ_3=β_2
#     * β_3=α_1 or β_3=β_1
#  - If no such triples exist, increase 'limit' and start again.
#
# For generating the triples, I used the algorithm described here: Tree of primitive Pythagorean triples.
# Really efficient (just remember to generate non-primitives triples as well for this problem).
#
# Here is my python code, ~2ms. Default limit is 1000 (which appear to be sufficient), but works as well if limit is lower
# (I tried with 10 and 100, without any meaningful change in running time).
#
# To gain efficiency, I store triples in a dictionary, where keys are γγ and values are {(β,α)|α2+β2=γ2,β>α}{(β,α)|α2+β2=γ2,β>α}
# and I keep track of γγ such that their corresponding value has a cardinality bigger than 1 (list 'candidates').
# The priority queue 'tree_queue' contains a list of triples that awaits to be treated (i.e. store non-primitive triples based on them,
# and generate their children --- again, see Tree of primitive Pythagorean triples).
#
# One might try to speed the process even more by generating Pythagorean triples in order,
# thus carrying out solution testing earlier and avoiding to generate unnecessary triples.
# However, I am not sure we would gain much, because this implies to keep a priority queue of both primitive
# AND non primitive triples (whereas here, the queue contains only primitive triples, and is consequently much smaller).



from heapq import heappush, heappop, heappushpop

def DrLock():
    limit = 1000
    tree_queue = []
    tc, tb, ta = 5, 4, 3 # initial triple
    all_triples = {}
    primitive_triples = {}
    candidates = set()
    solutions = []
    while True:
        candidates.clear()

        # Update tables (add multiples of old primitive pythagroean triples)
        for keyc in primitive_triples:
            index = 0
            while index<len(primitive_triples[keyc]):
                keym, keyb, keya = primitive_triples[keyc][index]
                mta, mtb, mtc = keym*keya, keym*keyb, keym*keyc
                while mtc <= limit:
                    if mtc in all_triples:
                        candidates.add(mtc)
                        all_triples[mtc].append((mtb, mta))
                    else:
                        all_triples[mtc] = [(mtb, mta)]
                    mta += keya
                    mtb += keyb
                    mtc += keyc
                primitive_triples[keyc][index] = (mtc//keyc, keyb, keya)
                index += 1

        # Generate new pythagorean triples
        while tc <= limit:
            # Add non-primitive triples of nta, ntb, ntc
            mta, mtb, mtc = ta, tb, tc
            while mtc <= limit:
                if mtc in all_triples:
                    candidates.add(mtc)
                    all_triples[mtc].append((mtb, mta))
                else:
                    all_triples[mtc] = [(mtb, mta)]
                mta += ta
                mtb += tb
                mtc += tc
            # Save the current triple in primitive table
            if tc in primitive_triples:
                primitive_triples[tc].append((mtc//tc, tb, ta))
            else:
                primitive_triples[tc] = [(mtc//tc, tb, ta)]
            # Add the children of the current triple in the queue and take the next triple
            heappush(tree_queue, (2*ta-2*tb+3*tc, 2*ta-tb+2*tc, ta-2*tb+2*tc))
            heappush(tree_queue, (-2*ta+2*tb+3*tc, -ta+2*tb+2*tc, -2*ta+tb+2*tc))
            tc, tb, ta = heappushpop(tree_queue, (2*ta+2*tb+3*tc, ta+2*tb+2*tc, 2*ta+tb+2*tc))

        # Check whether there are solutions
        for a in candidates:
            # Run through every pair in all_triples[a]
            for i in range(len(all_triples[a])-1):
                for j in range(i+1, len(all_triples[a])):
                    c,f = all_triples[a][j]
                    e,d = all_triples[a][i]
                    if c<e: # swap triples
                        c,e = e,c
                        f,d = d,f
                    # Find triple (b,e,c)
                    if c in all_triples:
                        for g,b in all_triples[c]:
                            # Swap e,d and/or g,b if necessary
                            if g == d:
                                d,e = e,d
                            elif b == e:
                                g,b = b,g
                            elif b == d:
                                d,e = e,d
                                g,b = b,g
                            # Is (f,c,a), (e;d,a), (b;e,c) a solution?
                            if g == e:
                                if (a*a+b*b)%2 == 0 and (e*e+f*f)%2 == 0 and (c*c-d*d)%2 == 0:
                                    solutions.append((a*a+b*b, e*e+f*f, c*c-d*d))
        if solutions != []:
            break

        # Increase limit
        limit *= 10

    # Find smallest solution
    x,y,z = solutions.pop()
    best = x+y+z
    while solutions != []:
        x,y,z = solutions.pop()
        if x+y+z < best:
            best = x+y+z

    return print(best//2)

DrLock()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ===== Mon, 18 Aug 2014, 07:56, nanogyth, USA
# 1. Find triplets a,b,c
# m>n, m+n odd, coprime, (mm-nn,2mn,mm+nn)*k
# 2. Factor bb to find g; bb = i(2g+i)
# 3. Check (g+a)(g-a) is square



MAX_C = 533 # 30ms
#MAX_C = int((2*1006193)**.5)+1 #200ms
#MAX_C = int((2*10**8)**.5)+1 #22s

def check_triple(_a,_b,_c):
    for k in range(1,MAX_C//_c+1):
        a,b,c = _a*k,_b*k,_c*k
        d = b*b
        for i in range(1,b):
            if d%i == 0 and (d//i - i)%2 == 0:
                g = (d//i - i)//2
                if g > c and ((g*g-a*a)**.5).is_integer():
                    x2 = g*g + c*c
                    if x2%2 == 0:
                        x = x2//2
                        y = x - a*a
                        z = x - c*c
                        return x+y+z,x,y,z,a,b,c,g,k
    return None

for m in range(2,int(MAX_C**.5)+1):
    for n in range(m-1,0,-2):
        out = check_triple(m*m-n*n, 2*m*n, m*m+n*n)
        if out is not None:
            print(out,m,n)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ===== Tue, 14 Oct 2014, 22:57, HuggyHermit, Scotland
# Not perhaps as elegant as using Pythagorean quadruples (wish I'd thought of that!) but not bad, I think:
# a guaranteed correct answer in less than 0.2s in Python.
# Essentially, I set a2 = x + y, b2 = x+z and c2 = x-z and loop over a,b,c (a > b > c) rather than x,y,z.
# One other optimisation was noting that x-y in this scheme is b2+c2-a2, which has to be greater than zero,
# further restricting the values b and c can take. Also, b and c have to have the same parity otherwise the solution
# won't correspond to integer values for x,y,z.
#
# Finally, x+y+z = a2 + (b2-c2)/2. Since b2 > c2, this means x+y+z > a2. Thus, once we have *an* answer,
# we know we can stop searching once we hit an a such that a2 > answer found, as all subsequent answers will have to be bigger.


from math import sqrt

def isSquare(x):
    return int(sqrt(x))**2 == x

a, root2, bestsum = 1, sqrt(2), None
while True:
    a2 = a*a
    if bestsum and a2 > bestsum:
        break
    for b in range(int(a/root2)+1, a):
        b2 = b*b
        if not isSquare(a2 - b2):
            continue
        cstart = int(sqrt(a2 - b2)) + 1
        if (b+cstart)%2 != 0:
            cstart += 1
        for c in range(cstart, b, 2):
            c2 = c*c
            if not isSquare(b2 + c2 - a2) or not isSquare(a2 - c2):
                continue
            xyzsum = a2 + (b2 - c2)/2
            if not bestsum or xyzsum < bestsum:
                bestsum = xyzsum
    a += 1

print (bestsum)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
