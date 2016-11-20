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

print('--------------------- cycle -------------------')
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