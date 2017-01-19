import operator

# Make an iterator that returns accumulated sums, or accumulated results of other binary functions
# (specified via the optional func argument). If func is supplied, it should be a function of two arguments.
# Elements of the input iterable may be any type that can be accepted as arguments to func.
# (For example, with the default operation of addition, elements may be any addable type including Decimal or Fraction.)
# If the input iterable is empty, the output iterable will also be empty.
#
# Roughly equivalent to:

def accumulate(iterable, func=operator.add):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total

# There are a number of uses for the func argument. It can be set to min() for a running minimum,
# max() for a running maximum, or operator.mul() for a running product.
# Amortization tables can be built by accumulating interest and applying payments.
# First-order recurrence relations can be modeled by supplying the initial value in the iterable
# and using only the accumulated total in func argument:

data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
# running product
print(list(accumulate(data, operator.mul)) )        # running product

# running maximum
print(list(accumulate(data, max)))                      # running maximum

# Amortize a 5% loan of 1000 with 4 annual payments of 90
cashflows = [1000, -90, -90, -90, -90]
print('Amortize a 5% loan of 1000 with 4 annual payments of 90 : ',list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)) )

print('\n--------------------- cycle -------------------')
# itertools.cycle(iterable)
# Make an iterator returning elements from the iterable and saving a copy of each.
# When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely. Roughly equivalent to:

def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

print('cycle works well with zip and next \n')
key='ABCD'
C = cycle(key)
print('Cycling the key : ' , C.__next__() , C.__next__(),  C.__next__() , C.__next__() )
for i in range(14) : print( next(C)  , end='  ' )

print('\n------------------- Dynamically creating nested for loop? ------------------')

import itertools
counts = [1, 2, 3]
ranges = [range(x) for x in counts]
for i in itertools.product(*ranges):
    print( i , end='  ')


print('\n\n---------- Combinations between Elements of Unknown Number of  Nested Lists -------------------')
# Nested Lists, Iterating over an unknown number of nested loops in python
from itertools import product
lists = [     ['THE', 'A'],     ['ELEPHANT', 'APPLE', 'CAR'],     ['WALKED', 'DROVE', 'SAT'] ]
for items in product(*lists):
    print (items)


print('\n#########   MORE ADVANCED METHODS TO GENERATE PYTHAGOREAN TRIPLETS    #################\n')
import itertools
# Method I - With Only One variable :

print(list((a,b,c) for a,b,c in itertools.product(range(1, 100), repeat=3) if a<=b<=c and a**2 + b**2 == c**2))

# Method II - With Only One variable :

print(list(x for x in itertools.product(range(1, 100), repeat=3) if x[0]<=x[1] <=x[2] and x[0]**2 + x[1]**2 == x[2]**2))


print('\n------------------ RECURSIVE GENERATOR ------------------')

# RECURSIVE GENERATOR

def orduples(size, start, stop, step=1):
    if size == 0:
        yield ()
    elif size == 1:
        for x in range(start, stop, step):
            yield (x,)
    else:
        for u in orduples(size - 1, start, stop, step):
            for x in range(u[-1], stop, step):
                yield u + (x,)
if __name__ == "__main__":
    print(list(orduples(3, 0, 5)))

print('--------------------- UNIQUE COMBINATIONS -------------------')
from itertools import combinations

for combination in combinations(range(1,6), 3):
    print (combination, end='  ')

print('\n----------------- Unique Custom List Non-reapeating Combinations')
for combination in combinations([2, 3, 5, 7, 11, 13], 3):
    print (combination, end='  ')


print('\n-------------- Cartesian products (itertools.product) -------------------')
for p in itertools.product([1, 2, 3], [4, 5]): print(p, end= ' ;  ')
print()
for p in itertools.product([0, 1], repeat=4):
    print ( ''.join(str(x) for x in p), end=' ;  ' )


print('\n --------------- Chaining iterables (itertools.chain) ------------------')

a = [1, 2, 3, 4]
for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a, 3)):
    print (p, end=' ;   ')
print()
for subset in itertools.chain.from_iterable(itertools.combinations(a, n) for n in range(len(a) + 1)) :
    print (subset, end=' ;  ')


print('\n --------------- Grouping adjacent list items using islice   ------------------')

# Using slices
from itertools import islice
group_adjacent = lambda a, k: zip(*(islice(a, i, None, k) for i in range(k)))
print( list(group_adjacent(a, 3)) )
print( list(group_adjacent(a, 2)) )
print( list(group_adjacent(a, 1)) )

print('\n --------------- Sliding windows (n-grams) using zip and iterators   ------------------')

from itertools import islice
def n_grams(a, n):
    z = (islice(a, i, None) for i in range(n))
    return zip(*z)

a = [1, 2, 3, 4, 5, 6]
print(list (n_grams(a, 2)) )
print(list (n_grams(a, 3)) )
print(list (n_grams(a, 4)) )

print('\n------ Combinations and combinations with replacement (itertools.combinations and itertools.combinations_with_replacement) ---')

for c in itertools.combinations([1, 2, 3, 4, 5], 3):
    print (''.join(str(x) for x in c), end=' ;  ' )
print()
for c in itertools.combinations_with_replacement([1, 2, 3], 2):
    print (''.join(str(x) for x in c), end=' ;  ')


print('\n------ Permutations (itertools.permutations) ---')
for p in itertools.permutations([1, 2, 3, 4]):
    print ( ''.join(str(x) for x in p) , end=' ;  ')


print('\n----------- Finding consecutive numbers in a list -----------------')

import itertools
from operator import itemgetter
# Find runs of consecutive numbers using groupby.  The key to the solution
# is differencing with a range so that consecutive numbers all appear in
# same group.
L = [ 1,  4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
for k, g in itertools.groupby( enumerate(L), lambda x: x[1]-x[0] ) :
    print (list(map(itemgetter(1), g)))