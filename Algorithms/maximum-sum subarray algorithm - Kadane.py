Test_arr = [ -3, -45, 9, 34, -87, 23, 1, -3, 99, 456, -89, 34, -45, 90, -123, 300, 9, -12, -67, 200 ]
print('\n',Test_arr)

def Kadane_algo(arr):
    ''' KADANE's Algorithm
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    '''
    max_current = max_global = arr[0]
    # start, end= 0, 1
    for i in range(len(arr)):
        # if arr[i] > max_current+arr[i] :
        #     start = i
        #     print('new start index :', start,  '     ', arr[i], max_current+arr[i])
        max_current = max (arr[i], max_current+arr[i] )
        if max_current > max_global :
            max_global = max_current
            # end = i+1
    # print('\nStart end indexes : ',start, end , '         ', arr[start:end])
    return max_global

print('\n Kadane_algo : \t', Kadane_algo(Test_arr))

# Just to verify the Kadane's Algorithm !!
print()
for i in range (len(Test_arr)):
    print(i, '    ', sum(Test_arr[i:] ))