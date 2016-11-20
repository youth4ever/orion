print('----'*10,'ENUMERATE LIST INDEXES','----'*10)
list = ["boat", "car", "plane"]

# Call enumerate to loop over indexes and values.
for i, v in enumerate(list):
    print(i, v)

######################################

print('----'*10,' MULTIPLE LISTS ITERATIONS ','----'*10)

a = ['a1', 'a2', 'a3']
b = ['b1', 'b2']

''' will iterate 6 times, it will iterate over each b, for each a producing a slightly different outpup'''

print ("List:")
for x, y in [(x,y) for x in a for y in b]:
    print (x, y)

######################################
print('----'*10,' ZIP ','----'*10)

print ("Zip:")
for x, y in zip(a, b):
  print (x, y)

#print('------'*20)

print('----'*10,' TUPLES ','----'*10)

foo = (1,2,3)
bar = (4,5,6)

#       Multiple list running for loop many arguments:
for f, b in zip(foo, bar):
    print('f:', f,'   b: ', b)

print('------'*20)

#####################################

print('----'*10,' 3 LISTS ITERATIONS ','----'*10)

a = ['a1', 'a2', 'a3']
b = ['b1', 'b2']
c = [1, 2, 3, 4]

''' It will display the smallest list number'''

print ("List:")
for x, y, z in zip(a,b,c):
    print (x,' ',' ', y,'  ', z)


############################################
print('----'*10,' FORM a DICTIONARY FROM 2 LISTS ','----'*10)

dict = {}
letter = ['a','b','c','d','e']
number= [1, 2, 3, 4, 5, 6]

for i, j in zip(letter, number):
    dict[i] = j
#girls['Karren'] = 45
print(sorted(dict.items()))

print('------'*20)
print('---'*20,'PRIME NUMBERS GENERATOR - ELEGANT WAY, but VERY SLOW !!!','---'*20)

for n in range(2, 16):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n // x)
             break
     else:
         print(n, 'is a prime number')