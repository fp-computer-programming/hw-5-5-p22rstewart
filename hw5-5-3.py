# Author RTS 11/3/21

word = input("Enter a string: ")

if word == word[:: -1]:
    print("The string " + word + " is a palindrome because the reverse is " + word[:: -1])
else:
    print("The string " + word + " is not a palindrome because the reverse is " + word[:: -1])
