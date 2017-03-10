#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 23 Feb 2017, 22:41
#The  Euler Project  https://projecteuler.net
'''
   Counting the number of "hollow" square laminae that can form one, two, three, ... distinct arrangements      -       Problem 174

We shall define a square lamina to be a square outline with a square "hole"
so that the shape possesses vertical and horizontal symmetry.

Given eight tiles it is possible to form a lamina in only one way: 3x3 square with a 1x1 hole in the middle.
However, using thirty-two tiles it is possible to form two distinct laminae.

If t represents the number of tiles used, we shall say that t = 8 is type L(1) and t = 32 is type L(2).

Let N(n) be the number of t ≤ 1000000 such that t is type L(n); for example, N(15) = 832.

What is ∑ N(n) for 1 ≤ n ≤ 10?

'''
# The problem states that you can use any number of tiles t &le; 1,000,000.
# Depending on the number of tiles used, you can form only a certain number of distinct laminae.
# There are 832 different number of tiles up to the stated limit which can form exactly 15 distinct laminae,
#  i.e. N(15)=832.



import time

print('--------------------------TESTS------------------------------')


print('\n==============  My FIRST SOLUTION,  4 sec  ===============\n')
t1  = time.time()

# @ 2017-02-23, 22:48
# Note: I used exactly the same code as for the pb 173.
# Pb173 was too detailed than needed but it seems that is better sometimes to be more detailed!

from math import sqrt
def gen_square_hole(i, n):
    ''':Description:
    :param:
        :n:     -       side of the square         2i+1     <   n <   infinity
        :i:     -       thickness of the sides,     1 <  i <= n/2-1    '''
    if n%2 ==0:
        if  i <= (n/2)-1 :
            return 4*i*(n-i)
        else : return 0
    if n%2 == 1:
        if  i < n/2 :
            return 4*i*(n-i)
        else : return 0

def pb174(lim = 1e2):
    D = {}
    counter=0
    for i in range(1, int(sqrt(lim)),1 ):
        for n in range(3,   int((lim+4*i*i)/(4*i))+1  ):
            tiles = gen_square_hole(i, n)
            if tiles != 0 :
                if tiles not in D : D[tiles]=1
                elif tiles in D : D[tiles]+=1
                counter+=1
#                 print(str(counter)+'.  Thickness: ',i, ' ; Side : ',n , ' ;  Tiles: ' ,tiles)
#     print(D)

    print(sum( [ 1 for v in D.values() if v==15]))
    print(sum([ 1 for v in D.values() if 1<=v<=2]))
    S = sum([ 1 for v in D.values() if 1<=v<=10])
    return print('\nAnswer :\t', S ,'       ' , counter)

pb174(1e6)              #   Answer :	 209566

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')               #   Completed in : 4.880279 s


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  2 sec  --------------------------')
t1  = time.time()

# === Fri, 30 Dec 2016, 09:34, mbh038, England
# About 750 ms in Python.
# I start with a 1x1 hole. With this hole I add layers 1 tile thick until I have reached the limit,
# note each time how many tiles there are altogether and increase the tally for that number by one.
# Then I move to a 2x2 hole, and so on.



def p174(n):
    tallies=[0]*(n+1)
    for i in range(8,n,4):
        j=0
        total=0
        while 1:
            total+=i+j*8
            if total>n:
                break
            tallies[total]+=1
            j+=1
    nsum=0
    for i in range(1, 11):
        nsum+=len([x for x in tallies if x==i])
    print (nsum)

p174(10**6)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Thu, 8 Oct 2015, 20:55, anumoshsad, Bangladesh

def pe174():

	c = [0]*1000001
	for i in range(1,500001):
		j=i+1
		while True:
			x=j*j-i*i
			if x>1000000:break
			if (j-i)%2==0:c[x]+=1
			j+=1
	print(sum([1 for i in c if i>0 and i<11]))

pe174()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Fri, 31 Oct 2014, 23:22, Nicolas Patrois, France


def Nicolas_Patrois():
    compte=0
    maxi=10**6

    t=[0]*(maxi+1)

    for a in range(1,maxi//2+1,):
      for b in range(a-2,0,-2):
        tt=(a-b)*(a+b)
        if tt<=maxi:
          t[(a-b)*(a+b)]+=1
        else:
          break

    return print(sum([t.count(i) for i in range(1,11)]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# === Fri, 15 Jun 2012, 14:04, Kutta, Hungary
# Reused code from 173 (1 sec):

limit = 1000000
c = [0]*(limit+1)
for h in range(1, limit//4):
    for n in range(h+2, int((limit+h*h)**0.5)+1, 2):
        c[(n+h)*(n-h)] += 1

print( sum(1 <= x <= 10 for x in c))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# === Mon, 16 Jul 2012, 13:09, ephemeral, USA
# 173 with a cache. Runs in ~1.5 seconds in Python.

def euler_174():
    limit, count = 10**6, 0;
    max_width, cache = int(limit / 4), [0] * (limit + 1)

    for i in range(1, max_width):
        for j in range(i + 2, max_width, 2):
            d = j * j - i * i
            if d > limit: break
            cache[d] += 1

    for i in range(0, limit + 1, 2):
        if cache[i] > 0 and cache[i] < 11: count += 1

    return print(count)

euler_174()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ==== Wed, 3 Feb 2010, 07:08, jhogan, USA
# This one was not hard after solving 173.  Modified the 173 code to store values in an array then count the results.


limit=1000000
record=[0]*(limit+1)

for high in range(1,limit//3):
    for low in range(high-1,0,-1):
        if low!=0 and high%2!=low%2:
            continue
        v=high*high-low*low
        if v>limit:
            break
        if v<=limit:
            record[v]+=1

print("Solution=",sum([record.count(n) for n in range(1,11)]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# ==== Thu, 6 Nov 2008, 21:00, KING-OLE, Denmark
# A minor twist from 173, but more or less the same. Runs in 1-2 secs.

a = [0]*1000001

for x in range (8,1000001,4):
  z=x
  a[z]+=1
  y=x+8
  z+=y
  while z <= 1000000:
    a[z]+=1
    y+=8
    z+=y

z = 0
for x in range(1,11):
  z+=a.count(x)

print (z)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')





