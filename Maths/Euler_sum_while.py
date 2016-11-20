''' This script calculates the sum of the inverse squares:
1 + 1/4 + 1/9 + 1/16 + ...
the number of the terms is specified by the user
We use a while loop
'''
import math
N = int(input('How many terms do you want to SUM UP ? Enter here: \n'))

sum = 0
x = 1

while (x <= N):
    sum = sum + (1 / x**2)
    x = x + 1

print('The approximated SUM result is:   ', sum)
print('Pi^2 / 6 is                                          ', (math.pi)**2/6)