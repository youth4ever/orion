#!/usr/bin/python3
# Solved by Bogdan Trif @ 2016-09-05 17:00
#The  Euler Project  https://projecteuler.net
''' Power digit sum     -       Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
'''

def main():
    a = str(raise_to_power(2, 1000))

    print(type(a),'    ',a)
    my_array = [int(i) for i in str(a) ]
    print("This is the list (the array) containing all elements of the number", my_array, '     ',type(my_array))
    print("The sum of all digits in the number is:", sum(my_array))

def raise_to_power(base, power):
    return base**power


if __name__ == "__main__": main()


#print ("Last element of the array is: ", my_array[-1], '... which is also the 10001-th prime')
#print ("Number of elements in the array is : ", len(my_array))
#print ("Good bye!")