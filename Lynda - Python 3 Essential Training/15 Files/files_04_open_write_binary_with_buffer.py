#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


def main():
    buffersize = 5000
    infile = open('olives.jpg', 'rb')
    outfile = open('olives_output.jpg','wb')
    buffer = infile.read(buffersize)
    
    while len(buffer):
        outfile.write(buffer)
        print('.',end = '')
        buffer = infile.read(buffersize)
    print()
    print('Done.')
        
    
if __name__ == "__main__": main()
