# Newton - Raphson
#   This gives us another way of generating guesses, which we can check; very efficient
# Is far more precise than the BISECTION Search and uses by far less steps

epsilon = 0.01
y= 24.0
guess = y/2.0
numGuesses= 0

while abs(guess*guess -y) >= epsilon:
    numGuesses+= 1
    guess = guess -(((guess**2) -y)/(2*guess))
    print('numGuesses= ' +str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))


