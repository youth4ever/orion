#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Coded triangle numbers      -       Problem 42
The n-th term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
nearly two-thousand common English words, how many are triangle words?
'''
f = open(r'pb022_names.txt', 'r')
line= f.readline()
#print(line)
names = [i.strip('"') for i in line.split(',')]
# print(names)
names = sorted(names)
print(len(names) , names)
#for i in names: print(i, end=' ')

alphabet={'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13,\
          'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26, }
#for i, j in alphabet.items(): print(i, end = ' ' )

a, b  = alphabet.keys(), alphabet.values() ; print(a, b)


dd = dict(enumerate(string.ascii_uppercase, start=1))       # Construct the dictionary of letters
# print(dict(enumerate(string.ascii_uppercase, start=1)))
D = dict(zip(dd.values(),dd.keys()))                    # Invert the dictionary
print(D)

# I only copied the content of pb022