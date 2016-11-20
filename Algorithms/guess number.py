x=100
h=100
l=0
y=0
print ("Please think of a number between 0 and 100!")
while True:
   if y!='c':
       print ("Is your secret number " + str(int((h+l)/2)) +"?")
       y=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
       if y not in ('h', 'l', 'c'):
            print("Sorry. I did not understand your input.")
            continue
       elif y=='h':
         h=(h+l)//2
         int(h)
       elif y=='l':
        l=(h+l)//2
        int(l)
   else:
    break
print ("Game Over. Your secret number was: " + str(int((l+h)/2)) )