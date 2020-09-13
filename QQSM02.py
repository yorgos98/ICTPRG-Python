#Write a program that takes in 2 values one an email and one a number. Print the email address how ever many times the number says with the count prefixing the number. For example i enter 'bob@example.com' and the number '2', I will get an output of '1_bob@example.com' and then '2_bob@example.com'.
import sys
e = input("Please enter an email address: ")
n = int(input("Please enter a number: "))
Num = 0


while Num != n:
    Num += 1     
    print (Num,"_",e)
    