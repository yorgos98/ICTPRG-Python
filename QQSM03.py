#Write a program that ask the user for a random set of characters. If the entered characters length is over 7, print a string made of the middle three characters only

string = input("Please enter some characters: ")

if len(string) > 7:
    m = int(len(string)/2)
    print (string[m-1:m+2])
