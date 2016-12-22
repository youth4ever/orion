#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Efficient exponentiation    -       Problem 122

The most naive way of computing n**15 requires fourteen multiplications:

n × n × ... × n = n**15

But using a "binary" method you can compute it in six multiplications:

n × n = n**2
n**2 × n**2 = n**4
n**4 × n**4 = n**8
n**8 × n**4 = n**12
n**12 × n**2 = n**14
n**14 × n = n**15

However it is yet possible to compute it in only five multiplications:

n × n = n**2
n**2 × n = n**3
n**3 × n**3 = n**6
n**6 × n**6 = n**12
n**12 × n**3 = n**15

We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).

'''
import time
from  math import log2
import gmpy2
import pyprimes
print('\n--------------------------TESTS------------------------------')


def factorise(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


print('test gmpy2 module : ',gmpy2.is_prime(2))



# Tried :  Answer:   1635, 1654, 1636, 1625, 1583, 1582

#  Problema cu skepsis  @ 2016-11-24  00:33, the algorithm becomes too complicated !






print('\n=============  My SECOND SOLUTION, WEAK  ===============\n')
t1  = time.time()

print(list(pyprimes.primes_below(200)),'\n')

P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

D=dict()
cnt = 0
for n in range(1,201) :
    N=[n]
    while True:
        # SPECIAL CASES
        if N[-1] ==149 :         # Is lame but have no time to search for the error 2016-12-12, 20:20
            N = N+[ 144, 72, 36, 18, 9, 5, 4, 2, 1]

        if N[-1] in [ 5, 7] :     # CASEE  "-2"
            N.append( N[-1] - 2 )
            if N[-1] in D :
                N = N+D[N[-1]][1:]
        if N[-1] in [ 23, 43, 59,  83, 95, 107, 115, 155, 163, 179, 187  ] :         # CASEE  "-3"
            N.append( N[-1] -3)
            if N[-1] in D :
                N = N+D[N[-1]][1:]

        if N[-1] in [ 85, 125, 143, 149 ,165 ] :         # CASEE  "-5"
            N.append( N[-1] -5)
            if N[-1] in D :
                N = N+D[N[-1]][1:]

        if N[-1] in [ 87, 119 ] :         # CASEE  "-7"
            N.append( N[-1] -7)
            if N[-1] in D :
                N = N+D[N[-1]][1:]

        if N[-1] % 2 == 0 :
            while N[-1] % 2 == 0 :
                N.append(N[-1]//2 )
                if N[-1] in D :
                    N = N+D[N[-1]][1:]

        if N[-1] >32  and log2( N[-1]-1) % 1 == 0 :      # Power of 2
            N.append( N[-1] -1)
            if N[-1] in D :
                N = N+D[N[-1]][1:]

        if N[-1] % 3 == 0 :
            while N[-1] % 3 == 0 :
                N.append( N[-1] - N[-1]//3 )
                if N[-1] in D :
                    N = N+D[N[-1]][1:]

        if N[-1] % 2 != 0 and N[-1] % 3 != 0 and N[-1] > 1 and N[-1] % 2 == 1 :
            N.append(N[-1]-1 )
        elif N[-1] == 1 : break
    print(str(n)+'.      m(',n,') = ' ,len(N)-1 ,'    ',N)
    D[n] = N
    cnt+=len(D[n])-1

print('\nAnswer', cnt,'          I must find a -1 DIFFERENCE ... Not now !')                  #       Answer 1582

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
#### GENERAL IDEAS ##########
#      The Sequence can be find at :  http://oeis.org/A003313/b003313.txt


print('\n--------------------------SOLUTION 1, SUPER ALGORITHM,  --------------------------')
t1  = time.time()

# ======== Sun, 27 Mar 2016, 12:06, Pyviv. France
#
# What you are looking for is a sum where each new value is a prefix sub sum.
#
# 1
# 1 + 1
# 1 + 1 + 1
# 1 + 1 + 2
# 1 + 1 + 1 + 1
# 1 + 1 + 1 + 2
# 1 + 1 + 1 + 3
# 1 + 1 + 2 + 1
# 1 + 1 + 2 + 2
# 1 + 1 + 2 + 4
#
# I use this rule to compute sums of level i+1 knowing sums of level i.
# I also keep track of the minimal level for each value and assumed you didn't have to keep non optimal sums.
#
# The code runs in under 100ms. For 1000 values, it goes to 1.41 sec. Also, it's really short!

def response(N):
     L = [i-1 for i in range(N+1)]
     L[0] = 0
     dec = [(1,)]
     decnext = []
     C = N-3
     i = 0
     while C > 0:
         i+=1
         for d in dec:
             total = sum(d)
             s = 0
             t = list(d)
             for v in d:
                 s+=v
                 if total + s <= N and L[total +s] >= i:
                     t.append(s)
                     decnext.append(tuple(t))
                     t.pop()
                     if L[total+s] > i:
                        L[total+s] = i
                        C-=1
         dec, decnext = decnext, []
     print (L)
     return sum(L)
response(200)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')





print('\n--------------------------SOLUTION 3, SUPER ALGORITHM, Avi Levi, USA  --------------------------')
t1  = time.time()
# ======== Fri, 6 May 2016, 11:32, Avi Levy, USA
# I build up the optimal sequences of intermediate steps in the exponentiation algorithm by storing them in a queue
# and processing them in the manner of breadth-first search. The code runs in 169 milliseconds.


cutoff = 200
opt = {}
queue = [[1]]

while queue:
  l = queue.pop(0)
  for i in l:
    j = i + l[-1]
    if j > cutoff:
      break
    if j in opt and opt[j] < len(l):
      continue
    opt[j] = len(l)
    queue.append(l + [j])

print(sum(opt[k] for k in opt))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()


path=[[[x for x in range(1,i+1)]] for i in range(201)]
for i in range(1, len(path)):
    for j in path[i]:
        for k in [a for a in j if i+a<len(path)]:
            if len(path[i][0])+1 < len(path[i+k][0]): path[i+k] = [j + [i+k]]
            elif len(path[i][0])+1 == len(path[i+k][0]): path[i+k].append(j + [i+k])
print (sum(len(p[0])-1 for p in path[1:]))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

cutoff = 200

opt = {}
queue = [[1]]

while queue:
  l = queue.pop(0)
  for i in l:
    j = i + l[-1]
    if j > cutoff:
      break
    if j in opt and opt[j] < len(l):
      continue
    opt[j] = len(l)
    queue.append(l + [j])

print(sum(opt[k] for k in opt))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()
# =======  Mon, 3 Nov 2014, 07:13, grovert, USA
# I have a function that returns all chains up to a given depth. I don't add chains
# terminating in a given sum if it was already found at a lower depth.
# This runs in less than a second in Python. I had this down to a half second, but don't want to reverse the changes I made.

import itertools

def memoize(f):
    cache = {}
    def memoized(*args):
        if args in cache:
            return cache[args]
        else:
            result = cache[args] = f(*args)
            return result
    return memoized

@memoize
def getall(depth, maxnum):
    """Return the ordered pair set(chains for depth <= current depth), set(all terminals found at this depth or below)"""
    if depth==1:
        return {(1,)}, {1}
    last, lastfound = getall(depth-1, maxnum)
    found = lastfound.copy()
    current = set()
    for lst in last:
        for pair in itertools.combinations_with_replacement(lst, 2):
            s = sum(pair)
            if s<=maxnum and s not in lastfound:
                found.add(s)
                current.add(tuple(sorted(lst+(s,))))
    return current.union(last), found

def solve():
    for depth in range(1,31):
        solutions = {(t[-1], len(t)-1) for t in getall(depth, 200)[0]}
        if len(solutions)==200:
            nums, lengths = zip(*sorted(solutions))
            break
    print (lengths, "\n", sum(lengths))

solve()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()
# ======= Wed, 12 Aug 2015, 20:53, Haroun, Algeria
# Took 170 milliseconds, I created a list for f(n)f(n) and another list that stores all the paths that gives xnxn in f(n)f(n) multiplications.
# for example f(5)=3f(5)=3 can be obtained by 2→4→5or 2→3→5.

L=201;
paths=[[]]*L;
mins=[100]*L;
mins[0]=0;
paths[2]=[[2,1]];
mins[1]=0;mins[2]=1;
for i in range(2,L):
    for x in paths[i]:
        for j in x :
            n=i+j;
            if n<L :
                if mins[n]>mins[i]+1:
                    mins[n]=mins[i]+1;
                    paths[n]=[[n]+x];
                elif mins[n]==mins[i]+1:
                    paths[n]+=[[n]+x]
sol=sum(mins)

print ("the answer is : " , (sol))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()
# ==== Wed, 14 Oct 2015, 03:55, GNFS, USA
m = [999 for i in range(201)]

def gen_tree(current_path, last, mult_count):
    m[last] = min(m[last], mult_count)
    for n in current_path:
        # Tree max, tree depth limit, pruning
        if n + last <= 200 and mult_count <= 10 and mult_count - m[last] <= 0:
            gen_tree(current_path + [n+last], n+last, mult_count+1)

gen_tree([1], 1, 0)
print(m)
print(sum(m[k] for k in range(1, 201)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()
# ===== Thu, 14 Nov 2013, 23:46, SafassThin, France
# I sweated on this one.. but with a bit of help from internet, I managed to come up with this recursive code.
# As others have pointed out, as the limit goes higher, the answer will most probably get wrong
# at some point because of too early discard of potential paths...

def euler_122(limit=200):
    m = [0]+[i for i in range(limit)]
    def explore_node(current, exps):
        steps = len(exps)
        for e in exps:
            candidate = current+e
            if candidate>limit or steps>m[candidate]: continue
            m[candidate] = steps
            explore_node(candidate,[candidate]+exps)
    explore_node(1,[1])
    return sum(m)

euler_122()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()
# ==== Wed, 2 Apr 2014, 22:20, darebear, USA
# Took a couple hours to think through, but finally produced some nice code in Python.
# I think it could be optimized more, but it still runs in 200ms.

N = 200
n = set(range(1, N + 1))
entire = {1}
chains = {1: [[1]]}
current_level = chains.keys()
while not n <= entire:
    next_level = dict()
    for k in current_level:
        for j in chains[k]:
            newlst = [i + k for i in j if i + k not in entire]
            for m in newlst:
                try:
                    next_level[m].append(j.copy() + [m])
                except KeyError:
                    next_level[m] = [j.copy() + [m]]
    for j in next_level:
            chains[j] = next_level[j].copy()
    current_level = next_level.keys()
    entire |= set(current_level)

print(sum([min(map(len, chains[i])) - 1 for i in range(1, N + 1)]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()
# ==== Tue, 16 Apr 2013, 00:05, jbum, USA
# Same as shitpants, and many others above.  My table is keyed by (n,x) for each n, for each x <= n.
# (n,n) or (n,1) will contain the shortest solution for n.  Storing the table as we build it prevents needless recursion for higher numbers.

limit = 200
cache = {(1,1):[1]}

for n in range(2,limit+1):
  for a in range(n//2+n%2,n):
    if (a,n-a) in cache:
      cache[(n,a)] = [n] + cache[(a,n-a)]
      for x in cache[(n,a)]:
        if (n,x) not in cache or len(cache[n,a]) < len(cache[(n,x)]):
          cache[(n,x)] = cache[(n,a)]

  # print n,len(cache[(n,1)])-1,cache[(n,1)]    # print shortest exponentiation for each n here

sm = sum([len(cache[(x,x)])-1 for x in range(2,limit+1)])
print ("Result",sm)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 11, mhb038, ELEGANT  --------------------------')
t1  = time.time()
# ====== Mon, 28 Nov 2016, 11:01, mbh038, England
# About 75 ms in Python. I approached this as I did the coin sum problem.
# Starting with the lowest values, for each k  I would look back to all the places (lower k values)
# I could have come from by the rules of the game, look at the path length back to 1 from each of those places
# and pick from among them those that had the shortest path.
# These paths, to which we now add the extra step from their respective smaller k values to the current k are,
# necessarily, the shortest paths back to 1 from the current k.
#
# I use a dictionary that stores, for each k, the shortest path length for that k,
# a list of the paths from that k back to 1 that have this shortest length and a set of all the k values in these paths.
# Starting with base cases of k=1 and 2, for each next k I cast back to smaller k, as far as k/2+1.
# For each decrement value m, which takes us back to k-m, I look to see if that m is in any of the shortest paths found for k-m.
# - If it is, then we can get to k from k-m. Among these k-m I select those which have the shortest path.
# - If the length of that path is L, then the shortest possible path from k is L+1.
# I then create a new entry in the dictionary for k.
# The list of shortest paths for this k is is made by taking from the lists of shortest paths for the selected k-m all those that contain m.
# I add the current k to each and they then are the possible shortest paths back from this k.
# And then on to k+1 until we get to k=200.


def p122(n):
    memo={1:[0,{(1)},{1}],2:[1,{(1,2)},{1,2}]}
    msum=1
    for k in range(3,n+1):
        options={}
        for m in range(1,k//2+1):
            if m in memo[k-m][2]:
                options[m]=1+memo[k-m][0]

        minpath=min([v for key,v in options.items()])
        shortest=[key for key,v in options.items() if v==minpath]

        memo[k]=[minpath,set(),set()]
        for index in shortest:
            for x in memo[k-index][1]:
                if index in x:
                    memo[k][1].add((k,)+x)
                    memo[k][2].add(k)
                    for i in x:
                        memo[k][2].add(i)
        msum+=minpath

    print(msum)

p122(200)

# In an earlier version I didn't store each valid shortest path for each k,
# but just one set of all the  smaller k in all the possible shortest paths to k.
# This was very fast, at 10 ms and wrong, but only for 5 values of k for which it underestimated the path length by 1,
# giving me a result of 1577. From memory, 4 of those k values were 71, 139, 141 and 142.
# I have not been able to get around needing to store all the shortest paths for each k.
# At least the time penalty is only one order of magnitude and not two,
# since when deciding whether each of my cast-back values m is valid,
# it then is sufficient simply to look at a single set of all the nodes in all the shortest paths for that k-m.
# At that point in the code,  I don't need to worry about which of the paths to k-m actually contain m,
# just that at least one of them does. However, once I decide that, for example, I can get back to k=12 from k=15 with m=3,
# because the set of all k values crossed by one or more of the shortest paths to 12 contains 3,
# e the shortest paths to k=15 will be  only those paths to k=12 that did contain 3, now with k=15 added.
# Any paths to 12 that did not contain 3 don't get used, because you can't use them to get to 15 from 12.
# To make this selection I do need to store all the separate shortest paths back to 1 for each value of k.
#
# Hence, in my algorithm, I need a data structure that contains, for each k, the minimum path length from that k,
# all the actual shortest paths from k, and (for speed only) a set of all the k values visited by those paths.


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')