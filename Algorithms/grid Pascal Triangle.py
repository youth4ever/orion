
grid = []
n = 5
for i in range(n+1):
    grid.append([1] * (n+1))

for i in range(n):
    for j in range(n):
        print(grid)
        grid[i+1][j+1] = grid[i][j+1] + grid[i+1][j]

print(str(grid[n][n]))

print('\n--------------')
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
        print(grid)
    print(grid[size][size])

main()

print('\n-------------------- OnE MATRIX ROW - PASCAL TRIANGLE----------------------')

total = 5
combinations = [1] + [0]*total
monies = [1]*total

for x in monies:
	for i in range(x,total+1):
		combinations[i] += combinations[i-x]

print (combinations[total])
