#!/usr/bin/python3
# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string\n the snake is snoring something\n.such things are the smallest.'
    for c in s:
        if c == 's': continue   #continue shortcuts the loop
        print(c, end='')

if __name__ == "__main__": main()
