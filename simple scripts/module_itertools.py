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


print('\n---------------------- Equivalent of the Arbitrary Sized FOR NESTED LOOPS  ------------------')
for a, b, c, d in itertools.product(range(1, 4+1), repeat=4):
    print(a, b,c, d, end='   ')


print('\n\n ============== INTRO TO ITERTOOLS ===============')
# Python provides a great module for creating your own iterators.
# The module I am referring to is **itertools**.
# The tools provided by itertools are fast and memory efficient.
# You will be able to take these building blocks to create your own specialized iterators that can be used for efficient looping.
# In this chapter, we will be looking at examples of each building block so that by the end you will understand
# how to use them for your own code bases.
#
# Let’s get started by looking at some infinite iterators!

print('\n============== The infinite iterators ===============')

# The itertools package comes with three iterators that can iterate infinitely.
# What this means is that when you use them, you need to understand that you will need to break out
# of these iterators eventually or you’ll have an infinite loop.
#
# These can be useful for generating numbers or cycling over iterables of unknown length,
# for example. Let’s get started learning about these interesting iterables!
#
# count(start=0, step=1)
#
# The count iterator will return evenly spaced values starting with the number you pass in as its start parameter.
# Count also accept a step parameter. Let’s take a look at a simple example:

from itertools import count
for i in count(10):
    if i > 20:  break
    else:   print(i, end = '   ')

# Here we import count from itertools and we create a for loop.
# We add a conditional check that will break out of the loop should the iterator exceed 20,
# otherwise it prints out where we are in the iterator. Y
# ou will note that the output starts at 10 as that was what we passed to count as our start value.

print('\n\n---------------------- islice Method -----------------------------')

# Another way to limit the output of this infinite iterator is to use another sub-module
# from itertools, namely islice. Here’s how:

# Here we import islice and we loop over count starting at 10 and ending after 5 items.
# As you may have guessed, the second argument to islice is when to stop iterating.
# But it doesn’t mean “stop when I reach the number 5”.
# Instead, it means “stop when we’ve reached five iterations”.

from itertools import islice, count
for i in islice(count(10), 5):
    print(i, end = '   ')

print('\n-------------------cycle (iterable) Method ----------------- ')
# The cycle iterator from itertools allows you to create an iterator that will cycle through a series of values infinitely.
# Let’s pass it a 3 letter string and see what happens:
from itertools import cycle
count = 0
for item in cycle('XYZ'):
    if count > 7:   break
    print(item, end = ' ,  ')
    count += 1

# Here we create a for loop to loop over the infinite cycle of the three letter: XYZ.
# Of course, we don’t want to actually cycle forever, so we add a simple counter to break out of the loop with.

# You can also use Python’s next built-in to iterate over the iterators you create with itertools:
print()
polys = ['triangle', 'square', 'pentagon', 'rectangle']
iterator = cycle(polys)
for i in range(10):
    print(next(iterator), end=' ,  ')

# In the code above, we create a simple list of polygons and pass them to cycle.
# We save our new iterator to a variable and then we pass that variable to the next function.
# Every time we call next, it returns the next value in the iterator.
# Since this iterator is infinite, we can call next all day long and never run out of items.


print('\n\n-------------------repeat(object[, times]) Method ----------------- ')

# The repeat iterators will return an object an object over and over again forever
# unless you set its times argument. It is quite similar to cycle except
# that it doesn’t cycle over a set of values repeatedly. Let’s take a look at a simple example
from itertools import repeat
repeat(5, 5)
iterator = repeat(5, 5)
for i in range(5):     # if we put 6 instead, it will break
    print(next(iterator), end=' ,  ')

# Here we import repeat and tell it to repeat the number 5 five times.
# Then we call next on our new iterator six times to see if it works correctly.
# When you run this code, you will see that StopIteration gets raised because we have run out of values in our iterator.

print('\n==============   Iterators that terminate  =================\n')
# Most of the iterators that you create with itertools are not infinite.
# In this sections, we will be studying the finite iterators of itertools.
# To get output that is readable, we will be using Python’s built-in list type.
# If you do not use list, then you will only get an itertools object printed out.

print('\n-------------------accumulate(iterable[, func]) Method ----------------- ')
# The accumulate iterator will return accumulated sums or the accumulated results
# of a two argument function that you can pass to accumulate.
# The default of accumulate is addition, so let’s give that a quick try:

from itertools import accumulate
print( list(accumulate(range(10))) )

# Here we import accumulate and pass it a range of 10 numbers, 0-9.
# It adds each of them in turn, so the first is 0, the second is 0+1, the 3rd is 1+2, etc.
# Now let’s import the operator module and add it into the mix:

import operator
print( list(accumulate(range(1, 10), operator.mul)) )

# Here we pass the number 1-4 to our accumulate iterator. We also pass it a function: operator.mul.
# This functions accepts to arguments to be multiplied.
# So for each iteration, it multiplies instead of adds (1×1=1, 1×2=2, 2×3=6, etc).
#
# The documentation for accumulate shows some other interesting examples
# such as the amortization of a loan or the chaotic recurrence relation.
# You should definitely give those examples a look as they are will worth your time.

print('\n------------------- chain(*iterables) Method ----------------- ')

# The chain iterator will take a series of iterables and basically flatten them down into one long iterable.
# I actually recently needed its assistance in a project I was helping with.
# Basically we had a list with some items already in it and two other lists that we wanted
# to add to the original list, but we only wanted to add the items in each list.
# Originally I tried something like this:

my_list = ['foo', 'bar']
numbers = list(range(5))
cmd = ['ls', '/some/dir']
my_list.extend(cmd)
my_list.extend(numbers)
print( my_list )

# Well that didn’t work quite the way I wanted it to. The itertools module provides a much more elegant way
# of flattening these lists into one using chain:
from itertools import chain
my_list = list(chain(['foo', 'bar'], cmd, numbers))
print(my_list)






