


# Converting an Integer to a String in Any Base

def toStr(n,base):
   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg"
   # print(len(convertString))
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

for i in range(2, 43) :
    print(toStr(43, i), end='  ')




