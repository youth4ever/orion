#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.swapcase())
    print(s.find('is'))
    print(s.replace('this', 'I remember you THIS'))
    print(s.strip())
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.isprintable())
    print(len(s))
    print('This is a string {}'.format(42))

if __name__ == "__main__": main()
