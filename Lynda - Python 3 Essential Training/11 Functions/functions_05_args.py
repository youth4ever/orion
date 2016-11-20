#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(1, 2, 3 ,42, 43, 45, 46)

def testfunc(this, that, other, *args):         # None is a special value
   
    print(this, that, other, args)      # an excelent way to get an arbitrary list of arguments into the function
    for n in args: print(n, end=' ')        # args is a tuple

if __name__ == "__main__": main()
