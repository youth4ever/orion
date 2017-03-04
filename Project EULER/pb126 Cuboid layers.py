#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 17 Feb 2017, 15:38
#The  Euler Project  https://projecteuler.net
'''
                        Cuboid layers     -    Problem 126

The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is 22.

- If we then add a second layer to this solid it would require 46 to cover every visible face,
- the third layer would require 78 cubes,
- and the fourth layer would require  118 cubes to cover every visible face.

- However, the first layer on a cuboid measuring 5 x 1 x 1 also requires 22 twenty-two cubes;
- similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers.
So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.

It turns out that 154 is the least value of n for which C(n) = 10.

Find the least value of n for which C(n) = 1000.

'''
import time, gmpy2
from itertools import combinations
from math import gcd
import operator, functools

# print(sympy.npartitions( 5 ))

def partition_in_three(n):     #2017-02-06 Some minor losses, but no time to fix it now
    ''':Usage:  >>> for i in P :  print( i )
    :param n: int, number
    :return: generator, tuple with partitions : (9, 1, 1), (8, 2, 1), (7, 3, 1) ....            '''
    a, b, c = n-1, 0, 1
    bc = b+c
    while a > n/3+1 :
        a-=1
        bc+=1
        for i in range( 1, bc//2+1):
            b=bc-i ; c=bc-b
            if a>=b :
                yield a, b, c
    if n%3 == 0 :
        yield n//3, n//3, n//3


def get_cuboid_layers( cuboid, k_th ) :
    a, b, c = cuboid
    L =[]
    l1 = 2*(a*b) + 2*(a*c) + 2*(b*c)
    for k in range(0, k_th+1):
        l_th = l1 + 4*(a+b+c)*k + 8* ((k-1)*k//2)
        L.append(l_th)

    return L

# must use partition of a number to find cuboid shapes --> reverse engineering, complicated # 2016-12-02 - we'll solve it later
print('\n--------------------------TESTS------------------------------')

P = partition_in_three(13)
cnt=0
for i in P :
    cnt+=1
    print( str(cnt)+'.    ',  i )

print('\n---------------------------------------------\n')

def calc_cuboid_layer( P ):
    C = list( combinations(P, 2 ))
    # F =[]
    # for i in C :
    #     F.append(gcd ( i[0], i[1] ) )
    # C2 = list( combinations(F, 2 ))
    S = 0
    for I in C :
        S+= functools.reduce( operator.mul, I )

    return 2*S

print('make_cuboid : \t ', calc_cuboid_layer(  [3, 2,1 ]) )



# @2017-02-07. I must also count the other layers.
# Doesn't suffice to count only the first layer of a partition configuration. Must go until the limit


print('\ncompute_cuboid_layers : \t', get_cuboid_layers( [1,1,1], 20 ))

print('\n================  My FIRST SOLUTION,  8 sec  ===============\n')
t1  = time.time()

def get_cuboid_layers_thousand( cuboid, k_th, up_target ) :
    a, b, c = cuboid
    L =[]
    l1 = 2*(a*b+a*c+b*c)
    l_th, k  =  l1, 0
    while l_th < up_target :
        l_th = l1 + 4*(a+b+c)*k + 8* ((k-1)*k//2)
        L.append(l_th)
        k+=1
    return L

def cuboid_layers( up_target = 2e4, C_n=10**3) :
    D = {}
    up = up_target//4
    for a in range(1, up+1):
        # print(a )
        for b in range(a, up+1):
            e = 2*(a*b)
            if e > up_target : break
            for c in range(b, up+1):
                d = 2*(a*b+a*c+b*c)
                if d > up_target : break
                cuboid = (a, b, c)
                G = get_cuboid_layers_thousand(cuboid, 70, up_target)
                # print(str(a+b+c)+'.     ', cuboid, '        ',G)
                for g in G :
                    if g not in D : D[g] =1
                    else : D[g]+=1

    bigger =  { k: v for k,v in D.items()  if v >=C_n }
    print('\n  >= ',C_n,' candidates length :', len(bigger), '\n', bigger )

    W = [ k for k,v in D.items() if v == C_n ]
    print('\n Exact  candidates :',  W[:100]  )
    if len(W) > 0 :
        return print('\n  SOLUTION : \t',   min(W)  )
    else :
        return print('We found Nothing for c_n==',C_n ,'     !!!')


cuboid_layers( up_target = 20000, C_n=10**3)                #   SOLUTION : 	 18522


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            #   Completed in : 8.315476 s

##### GENERAL IDEA #############
# Get the recurence formula for the growth of the cuboid :
# At help is the site :
# http://voxelbuilder.com/edit#C/2ecc713498db34495ee67e22ecf0f1ebf60a:A/YeYhcfhYhcfhYhffefiYhSiYfaffUhUhcje
# # UhUhcfhYfWehYhUhYfWfeYhUhYffheffYfUhYhUhYfeeeiUhUheieiUhUhcheUhUheieeUhUhceiYfffchiUhUhcjeUh
# # UhWeeUhUhcdeUhUhehhiYhSeYfaihYdfhddfYhUhYfUhYhWemUhUhcfeUhUhekedUhUhcZeUhUhcjjYhfdbhe
# # UhUhehehUhUhWecUhUhefehUhUhekefUhUhehehUhUhWeiUhUhefehUhUhefifYfWfhYheehecffeihfYhWff
# # YfajicfhXfflSiYdSefijhcYfWakYhUhUhcffUhelecUhUhcXeUhUhelecUhUhcfeUhUheienahfahfUhUheffhUheffh
# # UhcdeUhUhefefUhUhefefUhUhWeeUhUhehefUhUhehefUhUhcjeUhUhehehUhUhehehUhUhccjYhWffYfWffY
# # hWikYfWfhYhWfhYfefidcffcffclichfchffehhichfafhedhfcffahhWhdcffahfejhhchfaff


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== un, 27 Nov 2016, 21:51, Khalid, Saudi Arabia
# That was the most challenging problem so far, but I enjoyed thinking about it.
# Calculating a cube size with any number of layers is easy,
# but finding the value of n proved to be very difficult at first.
# I tried several approaches, but in the end I figured it would be below 20,000 (based on different checks),
# and gradually improved the algorithm until it managed to find the right solution in slightly over 1 second.
# Still using brute force, will be interesting to see what other approaches others have taken!

def Khalid():
    result = {}
    def calc_sizes(cubiod, max_size):
        base = 2 * (cubiod[0] * cubiod[1] + cubiod[0] * cubiod[2] + cubiod[1] * cubiod[2])
        sides = 4 * (cubiod[0] + cubiod[1] + cubiod[2])

        size = base
        if base > max_size:
            return True
        if size not in result:
            result[size] = 0
        result[size] += 1
        side_addition = 0
        counter = 0
        while True:
            size += sides + counter * 8
            if size < max_size:
                if size not in result:
                    result[size] = 0
                result[size] += 1
            else:
                break
            counter += 1
        return False
    #19710
    max_size = 20000
    club_1000 = {}
    a = 1
    while a < max_size:
        at_least_1_a = True
        b = a
        while True:
            at_least_1_b = False
            c = b
            while True:
                cubiod = (a, b, c)
                base_above_max = calc_sizes(cubiod, max_size)
                if base_above_max:
                    break
                else:
                    at_least_1_a = True
                    at_least_1_b = True
                c += 1
            if not at_least_1_b:
                break
            b += 1
        if not at_least_1_a:
            break
        a += 1

    for r in result:
        if result[r] == 1000:
            print (r, result[r])

# Khalid()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Tue, 17 Dec 2013, 16:05, superbit, Israel
# Found the formula for number of cubes in a layer after drawing a couple of layers for example,
# then I used bruteforce on the cuboid dimensions with an upper limit of 20000 for the layer value.
# Python code runs in 9 sec:


def f(L,a,b,c): return 2*(a*b+a*c+b*c)+4*L*(a+b+c)+4*L*(L-1)

def sol(n,lim):
	check = [0]*lim
	i=1
	while f(0,i,i,i)<lim:
		j=i
		while f(0,i,j,j)<lim:
			k=j
			while f(0,i,j,k)<lim:
				L=0
				while f(L,i,j,k)<lim:
					check[f(L,i,j,k)]+=1
					L+=1
				k+=1
			j+=1
		i+=1
	for i in range(lim):
		if check[i]==n: return i
	return -1


# print (sol(1000,20000))




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Fri, 3 Jan 2014, 22:56, aureleq, France
# That was a hard one..it took me a while just to understand the problem, was confused with the notion of layers.
# Anyway I started by writing a formula to compute the number of cubes knowing the cuboid size and the number of layers
# (just used pen and paper, would definitely be easier with legos...)
#
# # L: length
# # W: wide
# # H: height
# # x: nb layers
# # for x = 1: sol = 2*L*H + 2*W*H + 2*L*W
# # for x > 1: sol = 2*W*(H+2)+2*(H*(L+2*(x-1))+2*(L+2*(x-2)))+2*L*W+2*sum([2*W+2*(L+2*i) for i in range(0, x-2) ])
#
# I then simplified the formula for different values of x (from 2 to 5) and found out a recursivity formula
# between 2 consecutive layers: LayerX+1 = LayerX + 4*(H+W+L+2*x-4)
#
# The final code is a brute force and I used a parameter "limit" to limit the max number of cubes:

def prob126(c = 1000, limit = 20000):
	cub = {0:0}
	L = 1
	while True:
		if (6*L*L) > limit:
			break #stop increasing the Length
		W = L
		while True:
			if (4*L*W + 2*W*W) > limit:
				break #stop increasing the Width
			H = W
			while True:
				sol = 2*L*H + 2*W*H + 2*L*W
				if sol > limit:
					break #stop increasing Height
				x = 1
				while True:
					if x > 1:
						sol += 4*(H+W+L+2*x-4)
					if sol > limit:
						break #stop adding up layers
					if sol in cub:
						cub[sol] += 1
					else:
						cub[sol] = 1
					#print(L, W, H, x, sol)
					x += 1
				H += 1
			W += 1
		print(L)
		L += 1

	return min([ i for i in cub if cub[i] == c ])

# prob126(c = 1000, limit = 20000)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Fri, 24 Aug 2012, 10:51, gjyalpha. China
# Why 20000 works????


def cuboid_covers(l, w, h, layer):
    n = layer - 1
    #~ return (l*w + l*h + w*h) * 2 \
            #~ + n * (l + w + h) * 4 \
            #~ + 8 * ((n**3 - (n-1)**3 - 1) // 6) # hexagonalhg
    return 2*(l*w+l*h+w*h) + 4*n*(l+w+h + n-1)

res = {}
limit = 20000
l = 1
while cuboid_covers(l, l, l, 1) <= limit:
    w = l
    while cuboid_covers(l, w, w, 1) <= limit:
        h = w
        while cuboid_covers(l, w, h, 1) <= limit:
            a = 2 * (l*w+l*h+w*h)
            b = l + w + h
            n = 0
            c = a + 4 * n * (b + n - 1)
            while c <= limit:
                res[c] = res.setdefault(c, 0) + 1
                c += 8 * n + 4 * b
                n += 1
            # print(l, w, h)
            h += 1
        # print(l, w, h)
        w += 1
    # print(l, w, h)
    l += 1

group = {}
for n, count in res.items():
    group.setdefault(count, []).append(n)

# print(min(group[1000]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ===== Mon, 25 Feb 2013, 12:18, tom.wheldon, England
# I enjoy problems like this one where you need to spend more time thinking than coding.
# To get round the visualisation problem I drew the 2D slices of successive layers on squared paper.
# This actually made it obvious that there was a recurrence relation between layers and I use this in my code.
# I dealt with the issue of only generating layers that might contribute to the solution (and generating all of them)
# by looking at all cuboids with a <= b <= c, a+b+c = n for increasing values of n, with loop breaks where needed.
# I don't feel in the slightest bit guilty that I got the limit of 20,000 by trial and error -the ability to work interactively
# is usually considered a strength of scripting languages like Python.
# But if I'd only had one shot at setting a limit I'd have made a generous estimate of the number of layers
# for a given limit by looking at the loops in the program and then used the pigeon hole principle.

D = {}
limit = 20000

for n in range(3, limit//4 + 3):
    for a in range(1, n//3 +1):
        if 2*a*n -3*a*a > limit:
            break
        for b in range(a, (n-a)//2 + 1):
            c = n-(a+b)
            x = 2*b*c
            y = 2*(b+c)
            layer = x + a*y
            if layer > limit:
                break
            while layer < limit:
                if layer in D:
                    D[layer] += 1
                else:
                    D[layer] = 1
                x = x + 2*y
                y = y+4
                layer = x + a*y

for k in sorted(D):
    if D[k] == 1000:
        print(k)
        break



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ==== Fri, 3 Dec 2010, 17:34, Pygargue, France
# n = 2 * (pq + pr + qr + 2(k - 1)(p + q + r + k - 2))
# where p, q, r are side lengths and k the layer number.
#
# With this general formula, it's quite simple, the problem is to find bounds.
# The value N = 10000 was find progressing by 1000 with tries...
# Runs in a few seconds.

d = {}
N = 10000
P = (N-1)//2+1
for p in range(1, P):
    Q = min((N-p)//(p+1)+1, p+1)
    for q in range(1,Q):
        s1 = p+q
        s2= p*q
        R = min((N-s2)//s1+1, q+1)
        for r in range(1,R):
            dn = (s1+r)*2
            n = r*s1+s2
            while n <= N:
                if n in d: d[n] += 1
                else: d[n] = 1
                n += dn
                dn += 4
print(min(2*n for n in d if d[n]==1000))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

