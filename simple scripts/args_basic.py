#!/usr/bin/python

import sys

print('Number of arguments:', len(sys.argv), 'arguments.\n')
print('Argument List:', str(sys.argv), '\n')
print('The list of arguments is:\n')
'''
print('Argument No 0   is:', str(sys.argv[0]))
print('Argument No 1   is:', str(sys.argv[1]))
print('Argument No 2   is:', str(sys.argv[2]))
print('Argument No 3   is:', str(sys.argv[3]))
print('Argument No 4   is:', str(sys.argv[4]))
'''

a = 0
for i in sys.argv[0:]:	
		print('Argument No', a, 'is:', i)
		a = a + 1
		
