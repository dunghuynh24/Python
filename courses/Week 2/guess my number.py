"""In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses,
 and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret numbe"""
minnumber = 0
midnumber = 50
maxnumber = 100
print("Please think of a number between 0 and 100!")
print ("Is your secret number: " + str(midnumber) + "?")
a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while a != 'c':
    if  a == 'h':
        maxnumber = midnumber
        midnumber = int((midnumber + minnumber)/2)
    elif a == 'l':
        minnumber = midnumber
        midnumber = int((midnumber + maxnumber)/2)
    else:
        print("Sorry, I did not understand your input.")
    print("Is your secret number: " + str(midnumber) + "?")
    a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
if a == 'c':
    print ("Game over. Your secret number was:" + str(midnumber))
