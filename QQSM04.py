#Write a program that takes in a sentence and counts all of the letter 'a' and 'e' (case insensitive) and outputs the total. For example "Hello how are you there today?" would output "a: 2" 

string = input("Please enter a sentence:").lower()

count1 = 0
count2 = 0

for i in string:
    if i == 'e':
        count1 += 1
print("e:  ",count1)


for g in string:
    if g == 'a':
        count2 += 1
print('a:  ',count2)
