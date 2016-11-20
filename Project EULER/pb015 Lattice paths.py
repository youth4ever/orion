#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Wed, 28 Sep 2016, 10:37
#The  Euler Project  https://projecteuler.net

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
    00, 10, 11, 20, 21, 22
How many such routes are there through a 20×20 grid?
'''
#       The idea is to replace the grid with a matrix
#       2nd idea is to build a counter with the largest digit to be: 19
from math import factorial
digits = [0, 1, 2, 3]

collection=[]
s=[0, 0, 0]

for i in range(3):
    while s[i] < 1:
        s[i] += 1
        print(s)
print('-----------')
s=[2,0,0]
print(s)
for j in range(1,3):
    while s[j] < 2:
        for k in range(1,3):
            s[k]+=1
            print(s)

print('\n-------------------- MY SOLUTION, Only used the Mathematical Combination Formula --------------------------')

def combinations(n , k):
    result = factorial(n)//(factorial(k)*factorial(n-k))
    return result


print('\nOn a 20 x 20 GRID there are ',combinations(40, 20),'  lattice paths !!')           # 137846528820

print('\n=====================   OTHER SOLUTIONS FROM THE EULER FORUM ======================')
print('\n-------------------- SOLUTION 1 , SORT OF PASCAL  TRIANGLE ---------------------------')

grid=[]
n = 3           # n x n   Grid dimension
for i in range(n+1):
       grid.append([])
       for j in range(n+1):
              grid[i].append(0)

for i in range(n+1):
       grid[n][i]=1
       grid[i][n]=1

for i in range(n-1,-1,-1):
       for j in range(n-1,-1,-1):
              grid[i][j] = grid[i+1][j] + grid[i][j+1]

print (grid[0][0])


print('\n-------------------- SOLUTION 2 , Dynamic programming --------------- ---------------------------')

#After much thinking I came up with this shitty (though fast: 0.0023 seconds) recursive implementation:

k = 3
N = k + 1

def solution():
    d = {(N, N): 1}
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            if (i,j) in d:
                continue
            if i == N:
                d[(i,j)] = d[(N, j+1)]
                continue
            if j == N:
                d[(i,j)] = d[(i+1, N)]
                continue
            d[(i,j)] = d[(i+1, j)] + d[(i, j+1)]

    print (d[(1,1)])

solution()

print('\n-------------------- SOLUTION 3 , PASCAL TRIANGLE --------------- ---------------------------')
# http://stackoverflow.com/questions/15580291/how-to-efficiently-calculate-a-row-in-pascals-triangle

def pascal(n):
    row = [1]
    for x in range(n):
        row = [l + r for l, r in zip(row + [0], [0] + row)]
    # print row
    return row

print(pascal(2*3)[3])

print('\n-------------------- SOLUTION 4 ,     STRANGE SOLUTION          --------------- ---------------------------')

n=3         # The  n x n dimension of the grid
def main():
    x = 1
    greatest = 0
    for k in range(1,2*n+1):
        x = x*(((2*n+1)-k)/k)
        if(x > greatest):
            greatest=x
    print(greatest)
main()

print('\n-------------------- SOLUTION 5 ,     VERY ELEGANT , GRID NICE & FAVORITE  SOLUTION      ------------------------------------------')

# This problem was surprisingly easy. All I just did was just look at the number of possible ways to one part of a grid,
# then I applied it so that I pretended this was a 21 * 21 grid!

grid = []
n = 3
for i in range(n+1):
    grid.append([1] * (n+1))

for i in range(n):
    for j in range(n):
        grid[i+1][j+1] = grid[i][j+1] + grid[i+1][j]

print(str(grid[n][n]))

print('\n-------------------- SOLUTION 6 ,     VERY ELEGANT , RECURSIVE  SOLUTION       ------------------------------------------')

print('I still dont undesrstand it yet !')

def lattice_paths(a, b):
    if a == 0 or b == 0:
        return 1
    else:
        return lattice_paths(a, b - 1) + lattice_paths(a - 1, b)

print(lattice_paths(4,4))

print('\n-------------------- SOLUTION 7 ,     INTERESTING  SOLUTION       ------------------------------------------')
# from math import factorial            # already imported

grid = [4, 4]  # size of grid
down = grid[0]  # number of available downward moves
right = grid[1]  # number of available right moves
total_moves = right + down
ans = factorial(total_moves) / (factorial(down) * factorial(right))
print (ans)


print('\n-------------------- SOLUTION 8 ,     OTHER GRID, MATRIX  SOLUTION       ------------------------------------------')
'''
Initially went the recursion route and found out it was indeed too slow in this computation with recurring calculations.
With observing the pattern of grid's structure I found it worthwhile to use matrices.
Here is my solution using Python's NumPy (matrix), implementing an iterative memorization method.
'''
def main():
    size = 3
    grid_points_count = size + 1
    grid = []
    for x in range(grid_points_count):
        cur_row = []
        for y in range(grid_points_count):
            if x > 0 and y > 0:
                cur_row.append(cur_row[y - 1] + grid[x - 1][y])
            else:
                cur_row.append(1)
        grid.append(cur_row)
    print(grid[size][size])

main()