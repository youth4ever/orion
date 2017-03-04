print('\n------ # Function to find the minimum sum - RECURSIVE SOLUTION -----------')

# Function to find the minimum sum - RECURSIVE SOLUTION
def findMinRec(arr, i, sumCalculated, sumTotal):

    # If we have a reached last element.  Sum of one
    # subset is sumCalculated, sum of other subset is
    # sumTotal-sumCalculated.  Return absolute difference
    # of two sums.
    if i==0 :
        return abs((sumTotal-sumCalculated) - sumCalculated)

    # For every item arr[i], we have two choices
    # (1) We do not include it first set
    # (2) We include it in first set
    # We return minimum of two choices
    return min(findMinRec(arr, i-1, sumCalculated+arr[i-1], sumTotal),
               findMinRec(arr, i-1, sumCalculated, sumTotal))


# Returns minimum possible difference between sums
# of two subsets
def findMin(arr, n) :

    # Compute total sum of elements
    sumTotal = 0;
    for  i in range(0, n):
        sumTotal += arr[i]

    # Compute result using recursive function
    return findMinRec(arr, n, 0, sumTotal)

# Driver program to test above function
def main() :
    arr = [1, 11, 13, 2, 51]
    n = len(arr)//arr[0]

    return print( findMin(arr, n) )


print('\n------ # Function to find the minimum sum - RECURSIVE SOLUTION -----------')