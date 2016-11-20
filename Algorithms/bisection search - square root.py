# This finds the square root by using the BISECTION Method.
# Bisection method take a guess to be the midpoint between low and high compares this new number 'ans
# with the x^2-'ans' and repeats the process until is < epsilon, which is the desired precision
# As you increase the precision, the number of guesses (steps) needed by the algorithm increases
from math import sqrt
x= 2
epsilon = 1e-12
numGuesses= 0
low = 1.0
high = x
ans= high #(high + low)/2.0

while abs(ans**2-x) >= epsilon:
    print('low= '+ str(low) + ';    high = '+ str(high) + ' ;    ans= ' + str(ans))
    numGuesses+= 1
    if ans**2< x:
        low = ans
    else:
        high = ans
    ans= (high + low)/2.0
print('numGuesses= ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x) ,'by ' , ans-sqrt(2))
