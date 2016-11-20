# This finds the square root by using the BISECTION Method.
# Bisection method take a guess to be the midpoint between low and high compares this new number 'ans
# with the x^2-'ans' and repeats the process until is < epsilon, which is the desired precision
# As you increase the precision, the number of guesses (steps) needed by the algorithm increases

from math import  sqrt
from decimal import *
getcontext().prec =102

root_2 = Decimal(2).sqrt()
print(root_2)

x = Decimal(2.0)
epsilon = Decimal(1e-100)
print(epsilon)
numGuesses= 0
low = Decimal(1.0)
high = Decimal(2.0)
ans = high #(high + low)/2.0
print(high, low, (high+low)/2)

while abs(ans**2 - x) >= epsilon:
    print('low= '+ str(low) + ';    high = '+ str(high) + ' ;    ans= ' + str(ans))
    numGuesses+= 1
    if ans**2 < x :
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('numGuesses= ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x) ,'by ' ,ans-root_2 )
print(root_2)