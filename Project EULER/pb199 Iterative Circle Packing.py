#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Iterative Circle Packing            -       Problem 199

Three circles of equal radius are placed inside a larger circle such that each pair of circles
is tangent to one another and the inner circles do not overlap.
There are four uncovered "gaps" which are to be filled iteratively with more tangent circles.


At each iteration, a maximally sized circle is placed in each gap,
which creates more gaps for the next iteration.
After 3 iterations (pictured), there are 108 gaps and the fraction of the area
which is not covered by circles is 0.06790342, rounded to eight decimal places.

What fraction of the area is not covered by circles after 10 iterations?
Give your answer rounded to eight decimal places using the format x.xxxxxxxx .


'''
import time

http://www.sciencedirect.com/science/article/pii/S0925772102000998
https://en.wikipedia.org/wiki/Circle_packing_theorem
https://theses.lib.vt.edu/theses/available/etd-05082008-175931/unrestricted/draft.pdf
http://www.grasshopper3d.com/forum/topics/circle-packing-in-grasshopper-of-fixed-radius
https://books.google.ro/books?id=38PxEmKKhysC&pg=PA293&lpg=PA293&dq=Iterative+Circle+Packing&source=bl&ots=z20FpIUJAS&sig=v75cx2IKeE-akKryzqSzL9lIe7c&hl=en&sa=X&ved=0ahUKEwic7JLsnrbSAhXsCJoKHZrxAuk4ChDoAQgoMAY#v=onepage&q=Iterative%20Circle%20Packing&f=false









print('\n--------------------------TESTS------------------------------')
t1  = time.time()






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
