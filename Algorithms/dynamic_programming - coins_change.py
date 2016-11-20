'''
http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
If the amount does not match we have several options. What we want is the minimum of a penny plus
the number of coins needed to make change for the original amount minus a penny,
or a nickel plus the number of coins needed to make change for the original amount minus five cents,
or a dime plus the number of coins needed to make change for the original amount minus ten cents, and so on.
So the number of coins needed to make change for the original amount can be computed according to the following:

numCoins = min  [1+numCoins(originalamount−1)
1+numCoins(originalamount−5)
1+numCoins(originalamount−10)
1+numCoins(originalamount−25)]
'''

'''

def recMC(coinValueList,change):       # Innefficient Algorithm
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

print(recMC([1,5,10,25],63))
'''

'''
The trouble with the above algorithm in Listing 7 is that it is extremely inefficient.
In fact, it takes 67,716,925 recursive calls to find the optimal solution to the 4 coins, 63 cents problem!
To understand the fatal flaw in our approach look at Figure 5, which illustrates a small fraction of the 377 function calls
needed to find the optimal set of coins to make change for 26 cents.
'''

# The key to cutting down on the amount of work we do is to remember some of the past results
# so we can avoid recomputing results we already know. A simple solution is to store the results for the minimum
# number of coins in a table when we find them. Then before we compute a new minimum,
# we first check the table to see if a result is already known. If there is already a result in the table,
# we use the value from the table rather than recomputing. ActiveCode 1 shows a modified algorithm to incorporate our table lookup scheme.

def recDC(coinValueList,change,knownResults):
   # Recursively Counting Coins with Table Lookup (lst_change2)
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

print(recDC([1,5,10,25],63,[0]*64))

print('\n-----------------DYNAMIC PROGRAMMING--------------------')

def coinsum(value):

    coins = [1,2,5,10,20,50,100,200]

    ways = [0] * (value+1)
    ways[0] = 1

    while coins[-1] > value:
        del(coins[-1])
    print(coins)
    for i in range(len(coins)):
        for j in range (coins[i],value + 1):
            print('i, j ',i,j, '  ; coin:',coins[i], '  ;  nr. of ways:',ways[j - coins[i]])
            ways[j] += ways[j - coins[i]]
            print(ways)
        print('--------')

    print (ways[-1])

coinsum(10)