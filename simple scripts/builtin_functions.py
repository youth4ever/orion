
print('\n------------------- enumerate --------------------------')
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))

print(list(enumerate(seasons, start=1)))


print('\n-----------------Binary, Decimal, Octodecimal,  Hexadecimal  Conversions ----------------')
print('Decimal to Binary : ',bin(14))
print('Binary to Decimal : ',int('10111', 2))

print('Decimal to Binary : ',bin(1411))
print('Binary to Decimal : ',int('10110111', 2))
print('------------------------')
print('Hexadecimal to Decimal : ',int('ffaa', 16))
print('Octodecimal to Decimal : ',int('7676', 8))

print('Decimal to Hexadecimal  : ', hex(65365) )
print('Decimal to Octodecimal  : ', oct(65) )

print('\n-----------------------   ord & chr    ---------------------')
print('ord(a) and chr(57) return (respectively) the integer representing the given char and the char represented by the given integer.')
print('Test ord  :   ', ord('a'))
print('Test chr  :   ', chr(97))

print('\n--------------------    zip    -------------------------')
print('zip(a, b) returns an iterator that aggregates elements from each of the two iterables. '
      'It stops on the shortest input sequence ')
a = [0,1,2,3,4,5,6]
b = ['a' , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j' 'k', 'l','m']
z = zip(a,b)
for i in range(6):  print(next(z), end='  ')

print('\n\n--------------------       cycle & next    -------------------------')
from itertools import cycle
print("cycle(key) returns an iterator that produces an infinite concatenation of key's content ")
print('G.__next__() or next(G) where G is a generator gives next item in the sequence ')
print('cycle works well with zip and next \n')
key='abcd'
C = cycle(key)
print('Cycling the key : ' , C.__next__() , C.__next__(),  C.__next__() , C.__next__() )
for i in range(14) : print( next(C)  , end='  ' )

print('\n--------------------       map    -------------------------')
# The advantage of the lambda operator can be seen when it is used in combination with the map() function.
# map() is a function with two arguments:       r = map(func, seq)
# The first argument func is the name of a function and the second a sequence (e.g. a list) seq. map() applies
# the function func to all the elements of the sequence seq. It returns a new list with the elements changed by func

print('Here we make o conversion between Celsius and Fahrenheit using lambda and map: ' )
Celsius = [39.2, 36.5, 37.3, 37.8]
print(Celsius)
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print( list(Fahrenheit) ,'\n')

#   Example 2 :
# map() can be applied to more than one list. The lists have to have the same length. map() will apply its lambda
#         function to the elements of the argument lists, i.e. it first applies to the elements with the 0th index,
# then to the elements with the 1st index until the n-th index is reached:
print(' ---  map can be applied to more than one list : ----')
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print('Using two lists with map: ', list( map(lambda x,y : x+y, a , b) ))
print('Using three lists with map: ', list(map(lambda x,y,z : x+y+z, a, b ,c)))
print('Using three lists with map: ', list(map(lambda x,y,z : x+y-z, a, b , c) ))


print("\n --------------------------- FILTERING, filter function --------------------------")
# The function filter(function, list) offers an elegant way to filter out all the elements of a list,
# for which the function function returns True.
# The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True or False.
# This function will be applied to every element of the list l.
# Only if f returns True will the element of the list be included in the result list.

fib = [0,1,1,2,3,5,8,13,21,34,55]
even = filter(lambda x: x % 2, fib)
print ('Here we filter the even numbers of the Fibonacci sequence, we display only odd :  ', list(even))

odd = filter(lambda x: x % 2 == 0, fib)
print ('Here we filter the odd numbers of the Fibonacci sequence, we display only even :  ',list(odd))

print('\n -------------------------------  Reducing a list, with reduce -----------------')
# The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.
#
# If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
# = At first the first two elements of seq will be applied to func, i.e. func(s1,s2)
#     The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
# = In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
#     The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
# = Continue like this until just one element is left and return this element as the result of reduce()
# We illustrate this process in the following example:
from functools import reduce
a = reduce(lambda x,y: x+y, [47,11,42,13])
print('Calculates the sum of the list :   ', a )
f = lambda a,b: a if (a > b) else b
print('Determining the maximum of a list of numerical values by using reduce:   ', reduce(f, [47,11,42,102,13]))
s = reduce(lambda x, y : x+y, range(1,101))
print('Calculating the sum of the numbers from 1 to 100:   ', s)
factorial = reduce(lambda x,y : x*y, range(1,6))
print('Calculating the factorial of 5 :   ', factorial)
