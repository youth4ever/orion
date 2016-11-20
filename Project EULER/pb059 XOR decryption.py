#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 17 Nov 2016, 17:37
#The  Euler Project  https://projecteuler.net
'''
XOR decryption      -       Problem 59
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text;
for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.
The user would keep the encrypted message and the encryption key in different locations, and without both "halves",
it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge
that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
'''
import time

print('---------------TESTS ----------------------')

ASCII={}
for i in range(32,128): ASCII[chr(i)] = i
print(ASCII)

for k, v in ASCII.items():    print(k, v, end='  ')

print('\n',ASCII)
print('The \ key corresponds to the value : ',ASCII['\\'])
print('The ~ key has the value of : ',ASCII.get('~'))
print('The index 78 corresponds to : ',list(ASCII.keys())[list(ASCII.values()).index(78)])

print('\nReverse the Dictionary , keys become values :')
ascii = dict(zip(ASCII.values(),ASCII.keys()))
print(ascii)
print(ascii[43])

print('-----'*15,'\n')

filename = 'pb059_cipher.txt'
f = open(filename , 'r')
text = f.read()
f.close()
ASCII_ciphered = []

for row in text.split(','):
    ASCII_ciphered.append(int(row))

print('The original ciphered message text containing ASCII Numbers representation which are encrypted:\n',ASCII_ciphered)
for i in ASCII_ciphered:  print(i,end=' ')



# TESTS :            65 XOR 42 = 107, then 107 XOR 42 = 65.
print('\n\nXOR Test 1 :  ', 65^42 )
print('XOR Test 2 :  ', 107^42 )

#############################################

print('-----'*15,'\n')

# Stupid XOR demo
print('----- Stupid XOR demo --------')
from itertools import cycle

message = 'attack at dawn'
key = 's3cr3t'

print('The message encoded in ASCII :  ', [ ord(i) for i in message    ] )
print('Converted back from ASCII : ', ''.join( chr(i) for i in  [ ord(i) for i in message    ] ) ,'\n' )

cyphered = ''.join(chr(ord(c)^ord(k)) for c,k in zip(message, cycle(key)))

print('The encrypted message encoded in ASCII :  ',[ord(i) for i in cyphered    ],'\n' )

print(' Encryption of the message:       %s ^ %s = %s' % (message, key, cyphered))
message = ''.join(chr(ord(c)^ord(k)) for c,k in zip(cyphered, cycle(key)))
print(' Decryption of the message:       %s ^ %s = %s' % (cyphered, key, message))

print('\n---------------------  A RANDOM KEY TEST --------------------')

key = 'asl'
test_msg =  ''.join( chr(i) for i in  ASCII_ciphered     )
print(' Conversion into letters of the encrypted text : ', type(test_msg),'\n' , test_msg[0:100])
test_decoded = ''.join(  chr(ord(c)^ord(k))  for c, k in zip(test_msg, cycle(key) ))
print('Use XOR decryption to test a random key :  \n', test_decoded)

print('\n--------------------------- END TEST ---------------------')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()



string_msg =  ''.join( chr(i) for i in  ASCII_ciphered     )

def decode_encrypted_XOR_string(encrypted_string ):
    for i in range(ord('a'), ord('z')+1):
        for j in range(ord('a'), ord('z')+1):
            for k in range(ord('a'), ord('z')+1):
                key = chr(i)+chr(j)+chr(k)
                # print(key, ':    ' ,end='  ')
                decoded_message = ''.join( chr( ord(c)^ord(k) ) for c, k in zip(encrypted_string , cycle(key)))
                if decoded_message.find('there') != -1 :
                    print('Encryption key :   ',key , '\nThe Text :\n\n' , decoded_message)
                    return decoded_message

decrypted_message = decode_encrypted_XOR_string(string_msg)
print('\n',decrypted_message.replace('.', '.\n'))
# print('Loius is back home '.find('ist'))

decoded_ASCII = [ord(i) for i in decrypted_message]
print('decoded_ASCII : \n',  decoded_ASCII )
print('\nFinal Answer : ', sum(decoded_ASCII))

print('\n\nchr again :) : \n', [chr(i) for i in decoded_ASCII] )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, che_sac, USA  --------------------------')
t1  = time.time()
# Brute Force. Instantaneous.

cipher_text = ASCII_ciphered

#print(cipher_text)
small_alphas = [chr(i) for i in range(97,123)]
for first in small_alphas:
	for second in small_alphas:
		for third in small_alphas:
			decipher_text = []
			actual_text = []
			encryption_key = [first,second,third]
			encryption_key = encryption_key * 400 + [encryption_key[0]]
			for index in range(1201):
				c = cipher_text[index]
				e = ord(encryption_key[index])
				c ^= e

				if c in range(65,91) or c in range(97, 123) or \
						c in range(32, 60):
					actual_text.append(chr(c))
					decipher_text.append(c)
				else:
					break
			else:
				print('Sum of ASCII values in original text = ',sum(decipher_text))
				print('Encryption key = ',first + second + third)
				print(''.join(actual_text))
				break


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 732.041836 ms

print('\n--------------------------SOLUTION 2, VERY NICE FUNCTIONS and OPEN URL,  dorbt12,  --------------------------')
t1  = time.time()

# First i run the solve function to find the key then cal the ascii sum

import urllib.request

def url_to_txt():
    response = urllib.request.urlopen('https://projecteuler.net/project/resources/p059_cipher.txt')
    data = response.read()
    txt = data.decode('utf-8')
    return txt


def ascii_to_string(txt):
    new_txt = ''
    for c in txt.split(','):
        new_txt += chr(int(c))
    return new_txt


def decrypt(msg, key):
    return ''.join([chr(ord(a) ^ ord(b)) for (a, b) in zip(msg, key * len(msg))])


def solve():
    alphabet = list(map(chr, range(97, 123)))
    txt = ascii_to_string(url_to_txt())
    for c1 in alphabet:
        for c2 in alphabet:
            for c3 in alphabet:
                key = c1 + c2 + c3
                msg = decrypt(txt, key)
                if "the" in msg and "be" in msg and "to" in msg and "of" in msg and 'and' in msg:
                    print(msg)
                    print(key)


def ascii_sum(msg, key):
    string_txt = decrypt(msg, key)
    ascii_list = [ord(c) for c in string_txt]
    s = 0
    for i in ascii_list:
        s += i
    print(s)


# solve()
ascii_sum(ascii_to_string(url_to_txt()), 'god')


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')              # Completed in : 694.039822 ms

print('\n--------------------------SOLUTION 3, VERY VERY FAST , chiong, Australia --------------------------')
t1  = time.time()

# This is fun. And I have broken my first encrypted message!!!


import random
import re

"""
q059
Note:
1. Information given:
   a. 3 letter key
   b. key in [a-z]
   c. key is repeated cyclically
Algorithm:
1. Define list english_pattern of english word letters together with
   possible punctuation.
2. For each encoded[0::KEY_LEN] find first letter key such that all
   decoded[0::KEY_LEN] are in english_pattern.
3. Repeat step 2 for decoded[1::KEY_LEN] for second letter key, and so on.

Alternate algorithm (without assuming key candidate)
1. Define list english_pattern of english word letters together with
   possible punctuation.
2. Get key[i=0] candidates using key_cand[i=0] = encoded[i=0] ^ each letter in english_pattern.
3. For each candidate of key_cand[i=0],
   a. find decoded[KEY_LEN+0::KEY_LEN] = (key_cand[i=0] ^ encoded[KEY_LEN+0::KEY_LEN]).
   b. if any decoded[KEY_LEN+0::KEY_LEN] not in english_pattern, try next key_cand[i=0]
      and repeat Step 3a and 3b.
   c. Correct key[i=0] is given by key_cand[i=0] such that all decoded[KEY_LEN+0::KEY_LEN] are
      in english_pattern
4. Continue for key[i=1], ..., key[n] by repeating Step 2 to 3 for each key[i].
"""

KEY_LEN = 3
KEY_CANDIDATE = "abcdefghijklmnopqrstuvwxyz"
english_pattern = r"[a-zA-Z0-9 ,.'\"!?();:]"

with open(filename, "r") as f:
    txt = f.read()
    txt_list = txt.split(",")
    encoded_list = [int(c) for c in txt_list]

tic = time.time()
regex = re.compile(english_pattern)

key_list = [ord(c) for c in KEY_CANDIDATE]
random.shuffle(key_list)
key = [0 for _ in range(KEY_LEN)]
decoded_list = list(encoded_list)
for i in range(KEY_LEN):
    for j in key_list:
        k = i
        while k < len(encoded_list):
            decoded_list[k] = encoded_list[k] ^ j

            kkk = chr(decoded_list[k])

            if not regex.match(str(chr(decoded_list[k]))):
                break

            k += KEY_LEN
        else:
            key[i] = j
            break

res = sum(decoded_list)


data_str = "".join([str(chr(c)) for c in decoded_list])
key_str = "".join([str(chr(c)) for c in key])

print ('Result: ', res ,'\n' ,key_str, '\n' ,data_str )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')              # Completed in : 8.000374 ms

print('\n--------------------------SOLUTION 4,  froycard, Venezuela --------------------------')
t1  = time.time()

text= ASCII_ciphered
code=[]

for i in range(103,123):
    for j in range(97,123):
        for k in range(97,123):
            code.append([i,j,k])

for k in code:
    back=[text[i]^k[i%3] for i in range(len(text))]
    outp = ''.join([chr(i) for i in back])
    if 'The ' in outp or 'the ' in outp:
        outp = ''.join([chr(i) for i in back])
        print (k, outp)
        break
print (sum([ord(i) for i in outp]))
print ("DONE")


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, VERY VERY INTERESTING, ,dragonegghead1 , USA  --------------------------')
t1  = time.time()

# One thing I knew was that there were very probably going to be a lot of spaces.
# So I worked from that logic and took it from there:

import csv
import itertools

#Load the values
with open(filename , newline='') as a:
	values = [int(i) for i in list(csv.reader(a))[0]]

#Spaces should be the most numerous character.
spaces = sorted(set(values),key=lambda x: values.count(x))[-3:]

#Build an array of letters.
letters = []
for i in range(ord("a"),ord("z")+1):
	if ord(" ") in [i^x for x in spaces]:
		letters.append(i)

if len(letters) != 3:
	print("Something's wrong with your logic. Take another crack at it.")

else:
	for possibility in itertools.permutations(letters):
		message = list(map(lambda x: x[0]^x[1], zip(values, itertools.cycle(possibility))))
		total = sum(message)
		print(possibility)
		print(total)
		print(''.join(chr(i) for i in message))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  Avi Levy, USA --------------------------')
t1  = time.time()

from statistics import mode

message = [int(num) for line in open(filename) for num in line.split(',')]

size = 3
m = len(message)
cipher = [mode([message[j] for j in range(i, m-1, size)]) ^ ord(' ') for i in range(size)]

print(sum(cipher[i % size] ^ message[i] for i in range(m)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 6,   Sandamnit, USA --------------------------')
t1  = time.time()
import operator

key = []
with open(filename, 'rt') as handle:
   # read the cipher
   cipher = handle.read().split(",")
   cipher = [ int(x) for x in cipher ]

   for n in range(3):
      # initialize counts for cipher values at positions == n (mod 3)
      counts = [0]*256
      for x in range(len(cipher[n::3])):
         counts[cipher[n::3][x]] += 1

      # recover the most frequent cipher character for the n-th key value
      # this is expected to be the space character (ASCII value == 32)
      k, _ = max(enumerate(counts), key=operator.itemgetter(1))

      # xor with 32 to recover n-th key value
      key.append(k ^ 32)

print(sum([ cipher[n] ^ key[n%3] for n in range(len(cipher)) ]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



