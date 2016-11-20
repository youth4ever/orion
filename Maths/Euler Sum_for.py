import math

N=int(input("Number of terms you want to sum up : \n"))
sum = 0

for x in range(1, N+1, 1):
    sum = sum + 1/x**2

print("The result is : ", sum, "\n")
print("The EXACT result is : ", math.pi**2/6)

