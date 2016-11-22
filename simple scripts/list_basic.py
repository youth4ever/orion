import numpy as np
#           List going backwards. Reverse List
my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print('Original list :  ', my_lst)
print('\nOutput the list forwards only the ODD INDEX terms  :', my_lst[::2])        # becomes [1, 3, 5, 7, 9, 11]

print('Output the list forwards only the EVEN INDEX terms  :', my_lst[1::2])        # becomes [2, 4, 6, 8, 10, 12]

print('Output the list backwards : ', my_lst[::-1],'\n')         # becomes  [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print('Output the list backwards jumping 2 by 2, ODD Terms :  ', my_lst[10::-2])                # becomes 11 9 7 5 3 1

print('Output the list backwards jumping 2 by 2, EVEN Terms :  ', my_lst[::-2])                # becomes [12, 10, 8, 6, 4, 2]

print('Last few elements of my_lst list :',my_lst[-3:],'\n')               # Last few elements of a list [10, 11, 12]

print('Sum of the list is : ', sum(my_lst))

# Display ONLY ODD Index Terms from a list :
print(my_lst[1::2])

print('\n-------------------------------- slice ------------------------')
sl = slice(0,6, 1)
print ('Using slice we can build custom ranges :  ',my_lst[sl])


print('---------------------  PRODUCTS ---------------------')
print('\nProduct of the list is (FIRST METHOD): ', np.prod(my_lst))   # <------VERY VERY SLOW

print('\nProduct of the list is (SECOND METHOD): ')
P=1
for i in my_lst :   P *= i
print(P)

print('Product of a list using numpy :')
#from numpy import prod
print(np.prod([2,3,3,5]))                           # Product of the elements in a simple list
print(np.prod([[1.,2.],[3.,4.]]))                    # Even when the input array is two-dimensional:
print(np.prod([[1.,2.],[3.,4.]], axis=1))           # But we can also specify the axis over which to multiply:

print('\n================= LIST BASIC OPERATIONS ========================')

L=[9,6,16,0,54,11,3, 11, 0, 6, 11]
print('Return the maximum value from the list :', max(L))
print('Return the index with the maximum value from the list :', L.index(max(L)))

print('This prints a sorted list, the original remains unchanged:  ',sorted(L))
L.sort()
print('This sorts the list permanently:  ', L)
L.reverse()
print('This reverse the list permanently:  ', L)

print('List only unique elements : ', list(set(L)))

print("Join a list of numbers in a string :",  ''.join( str(i) for i in  L ) )

roman = ['MMMMDCLXXII', 'MMDCCCLXXXIII']
print("Join a list of strings :",  ''.join( roman ) , type( ''.join( roman )  ))


print('\n------------ CLONING, CLONE A LIST  ----------------------')
# Doing this way if you modify one list it will not affect the other as it will do with M=L where both will point out to the same list
M = L[:]        # However this doesn''t work for nested lists, like matrices ...etc...
print('M == L :  ',M==L,'         ;   M is L :  ', M is L)
M.insert(2,33)
print('First List : ',L,'   ;  Second List : ',M)

print('\n---------------Clone a Nested list, matrix : -----------------')
from copy import copy, deepcopy
A = [[1,2,3],[4,5,6],[7,8,9]]
B = deepcopy(A)
print(B)
# Using deepcopy() is a good solution. For a simple 2D-array case
C = [row[:] for row in A]
print(C)

# For 2D arrays it's possible use map function:
print(" For 2D arrays it's possible use map function: ")
old_array = [[2, 3], [4, 5]]
new_array = map(list, old_array)
print('old_array : ', old_array)
print('new_array : ', list(new_array))

print('\n---------- Replace an element in a simple list without affecting the indexing -----------')
my_lst.insert(my_lst.index(7),100)
del(my_lst[my_lst.index(7)])
print(my_lst)


print('\n ================== OPERATIONS WITH SUBLISTS =======================')
print('Changing a sublist will change also the list :\n')
warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]
print('brightcolors :',brightcolors)
brightcolors.append(hot)
print('brightcolors : ',brightcolors)
hot.append('pink')
print('hot : ',hot)
print('The list has been changed: ', brightcolors)
print('Concatenate lists : ', hot+warm)
print( 'Divide each element from a List  ' ,[ int(i / 2) for i in [2,4] ])      # List Comprehension to divide each element of a list



print('\n=================== JOIN,  FLATTEN A LIST =======================')
print('----------------- SINGLE FLATTEN , JOIN  ELEMENTS------------------')

list_of_lists = [[180.0, 1, 2, 3], [173.8], [164.2], [156.5,[45,12,[81,41,[2,3,8],4,11]]], [147.2], [138.2]]
single_flattened = [val for sublist in list_of_lists for val in sublist]
print(single_flattened)


print('\n----------------------- Join two lists --------------------------')
l=[101, 107]
m=[10079, 10103]
lm = l+m
print(lm)

print('\n---------------- RECURSION FLATTENING, Many levels of sublists ------------------')

def flatten(lst):
	return sum( ([x] if not isinstance(x, list) else flatten(x)
		     for x in lst), [] )

flattened =  flatten(list_of_lists)
print(flattened)

print('\n---------------- ITERATIVE FLATTENING, Many levels of sublists ------------------')
def flat(lst):
    '''Function flat is iterative and flattens the list in-place.
     It follows the Python idiom of returning None when acting in-place:'''
    i=0
    while i<len(lst):
        while True:
            try:
                lst[i:i+1] = lst[i]
            except (TypeError, IndexError):
                break
        i += 1
fl = flat(list_of_lists)
print(fl)

print('\n---------------- GENERATIVE FLATTENING, Many levels of sublists ------------------')

def flatten(lst):
    ''' This method shows a solution using Python generators.
     flatten is a generator that yields the non-list values of its input in order.
     In this case, the generator is converted back to a list before printing.'''
    for x in lst:
        if isinstance(x, list):
            for x in flatten(x):
                yield x
        else:
            yield x

flt = flatten(list_of_lists)
print(flt)

print('\n-------------------------MUTATION & ITERATION ------------------------')
# AVOID MUTATIING A LIST  as you are iterating over it   !!!!!!!!!!!!!
L1 = [1, 2, 3, 4];  L2 = [1, 2, 5, 6] ; print('The original lists are : ', L1,'  ; ',L2)
def remove_dups(L1, L2):
    ''' Removes duplicates from L1, does nothing on L2 '''
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
remove_dups(L1, L2)
print('The lists with duplicates from L1 removed are : ', L1,'  ; ',L2)

print('\n------------------------- REMOVE AN ITEM ------------------------')
lll=['foo', 'bar', 'baz', 'bar', 'bar']
print(lll)
print('REMOVE method removes a string and an int :  ',lll.remove('bar'))
print(lll)
print('POP method removes only an integer by its index  :  ',my_lst.pop(4))

print('\n ------------------------ REMOVE MANY ITEMS with CONDITION, first CLONE The LIST -------------')
berbec = [1,3,4,56,2,1,42,5,1,54,2,1,5,1,3,1,6,54,1,43,1,1,4,1]
jaguar = berbec[:]
print(jaguar)
for i in range(len(berbec)) :
    if berbec[i] == 1 :
        jaguar.remove(berbec[i])
print(jaguar)

print('\n ------------------------ REMOVE/ DELETE MANY ITEMS at ONCE  -------------')
A = [3,5,4,7,9,8,1,2,10]
print('Original List : ', A)
rem = [3,4,5]
print('Items to remove/ delete at once: ', rem)
new_A = [i for i in A if i not in rem]
print('The new_A list after we deleted the elements from rem list: ', new_A)


print('\n ----------------------- Get the INDEX in a nested list : ------------------------')
my_array=[['1', '2', '3', '7'], ['0', '1', '6', '9'], ['0', '1', '3', '9'], ['1', '2', '5', '8'], ['0', '1', '5', '8']]
mtx = [[1,    2,    3,    4],\
           [5,    6,    7,    8],\
           [9,   10,   11,  12],\
          [13,  14,   15,  16]]
print(my_array[2].index('3'), type(my_array[0]))            # Prints 2    <class 'list'>
print(mtx[2-2].index(3), type(mtx[0][3]))                          # Prints   2 <class 'int'>

print('\n=====================    COUNT ELEMENTS     ==========================')
print(' -------------How to count the occurrences of a list item in Python ---------------------')
print(' -------------- Count the numbers of elements in a list ----------------------------')
# Function which counts the number of occurrences of elements in a list
test_list = [2, 2, 13, 5 , 2, 2, 3, 3, 7, 13, 5, 7, 19]
def occurDict(items):
    '''  Function which counts the number of occurrences of elements in a list'''
    d = {}
    for i in items:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    return d

duplicates = {}
for i in test_list:
    if i in duplicates:
        duplicates[i] += 1
    else:
        duplicates[i] = 1
print(duplicates)

print('\n 2nd method to count the numbers of elements in a list ')
test_2=[2, 2, 8, 2, 5, 5, 6, 5, 6, 5, 6, 7, 2, 5, 5, 5, 6, 8]
for i in set(test_2):
    print(i, test_2.count(i), end='; ')

print('Count a single element at a time :  ',[1, 2, 3, 4, 1, 4, 1].count(1))


from collections import Counter
lst = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print(Counter(lst))


print ('Count only the elements which occur two or more times ' ,[item for item, count in Counter(test_2).items() if count > 1] )
print ('Count only the elements which occur two  times ' ,[item for item, count in Counter(test_2).items() if count == 2] )


print ('\nUsing LIST COMPREHENSION count all elements : ',[[x, lst.count(x)] for x in set(lst)] )

print('\n Another way to get the number of occurrences of each item, is/in a DICTIONARY :  ',dict((i, lst.count(i)) for i in lst))


lst = [True, False, False, True, True, True, True, True, True]
def duplicates(lst, item):
    ''':Description:    index-of-duplicates-items-in-a-python-list
    :param lst: list
    :param item: argument : boolean: True , False, integer, anything
    :return:  A list containing the index of the element which is duplicate
    '''
    return [i for i, x in enumerate(lst) if x == item]

print(duplicates(lst, False) )

######################################
print('\n-------------------    Finding the index of an item given a list containing it in Python  -----------------------')
# It always finds the index of the first element in the list, so if there are many the next ones will not be listed:
print(["foo", "bar", "baz", "bar"].index("bar"))
print(test_list.index(13),end=' ')

#       Using Enumerate :
print('\nUsing Enumarate : ')
xs = ['foo', 'bar', 'baz', 'bar','Dan', 'bar']
for i, j in enumerate(xs):
    if j == 'bar': print (i, end= ' ' )
# This can be more useful than index if there are duplicates in the list, because index() only returns the first occurrence,
# while enumerate returns all occurrences.    As a list comprehension:
f = [i for i, j in enumerate(['foo', 'bar', 'baz', 'bar', 'bar']) if j == 'bar']
print('\n',f)

print('-------'*20)

# Boolean, Get information about the existence of an element in a list:
print('\nBOOLEAN, Get information about the existence of an element in a list:')
print(15 in test_2)
print(7 in test_2)

print('\n------------------------MIN, Max of TWO LISTS :------------------------------')
pth1=[131, 201, 96, 342, 746, 422, 111, 956, 331]
pth2=[131, 201, 96, 342, 746, 422, 121, 37, 331]

for x, y in zip(pth1, pth2[::-1]):
    print(min(x, y),end='  ')

print('\n\n------------------------ INTERSECTION, Common elements of TWO Sublists :------------------------------')
# Method 1
A=[1,3,5,'a','c',7]
B=[1,2,3,'c','b','a',6]
print('Method 1 : ',A,B ,  '\n' ,set(A).intersection(B))

# Method 2
b1 = [1,2,3,4,5,9,11,15]
b2 = [4,5,6,7,8]
b3 = [val for val in b1 if val in b2]
print('Method 2 : ',b1,b2,'\n',b3)

# Method 3
def intersect(a, b):
    '''  Returns the intersection of two lists. Only the common elements will be displayed.  '''
    return list(set(a) & set(b))
print ('Method 3 : \n',intersect(b1, b2))


print('\n---------------- SUBSet of another List -------------------------')
def isSubset(L1, L2):
    '''  Returns True if the first list is a subset of the second list, otherwise returns False'''
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
L1 = [1,2,3]
L2 = [1,2,3,4]
print(isSubset(L2, L1))

print('\n--------------------Generate all the Subsets of a List, RECURSION ---------------------')
def genSubsets(L):
    ''' Generates all the possible Subsets of a List. Has O(c^n) complexity (Exponential) '''
    res = []
    if len(L) == 0:
        return[[]] #list of empty list
    smaller = genSubsets(L[:-1])# all subsets without last element
    extra = L[-1:]# create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra) # for all smaller solutions, add one with last element
    return  smaller+new# combine those with last element and those without

print(genSubsets(L2))

print('\n------------------ Instances of a list ------------------------')
L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
print(isinstance(2,list))                   # Returns False, because  2 is NOT a list, is an integer
print(isinstance([5],list))                 # Returns True, because [5] is a list  with a single element
print(isinstance([5,6,2,5,9],list))     # Returns True, because [5,6,2,5,9] is a list
print(any(isinstance([5,6,2,5,9],list)) for i in L)     # generator object
print(any(isinstance(i , list)) for i in L)     # This expression is a type boolean to check if a sublist is a part of a list

########################################
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    if any(isinstance(i, list) for i in L) == True:
        for A in range(len(L)):
            L[A].reverse()
        L.reverse()
        return L
L = [[2, -1, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 101, 10, 1, 1, 5, 4, 3]]
print(deep_reverse(L),'\n')

print('---------------------- Checks if a sublist is part of a composed list of lists -------------------------------- ')
if any(isinstance(i, list) for i in L) == True:     # isinstance(i,list) checks if i is a type list from a larger composed list of lists L
        for j in range(len(L)): print(L[j])             # prints the sublists of L


print('\n================== SEARCH in MATRICES, LIST of Lists ==================')
print('\n-------------- Search for an element in a list of list if the position in the sublist is known------------------')
my_list = [['a','b'], ['a','c'], ['b','d']]
search = 'c'
print(any('c' == x[1] for x in my_list))
print('d' in (x[1] for x in my_list))

print('\n--------------- Get the index of a searched element from a matrix ------------')
mymatrix=[[1,2,19],[4,19,6],[7,8,9]]
val = 9
print([(index, row.index(val)) for index, row in enumerate(mymatrix) if val in row])

print('\n--------------- Returns TRUE if an element is in a matrix, Else return FALSE ------------')
print( [val in row for row in mymatrix])
print( True  if  True in [ val in row for row in mymatrix ]  else False)    # Nice List Comprehension Construction, by Bogdan Trif, 2016-11-01

print('\n------------------Swapping, interchanging, moving elements in a list -----------------')
# keywords :    swap, move, change, interchange, shift elements in a list
enigma=[3, 1, 9, 6, 8, 0]
print(enigma)
print('Suppose you want to swap elements between them, here we swap 1 with 8 :')
enigma[1], enigma[4] = enigma[4], enigma[1]
print(enigma)