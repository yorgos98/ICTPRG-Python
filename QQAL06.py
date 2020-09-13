#Write a program that asks the user for a large number, and then sums all of the digits in that number: Example:

#Enter a large number: 29834892
#Sum of the digits: 2 + 9 + 8 + 3 + 4 + 8 + 9 + 2 = 45



ln = input("Please enter a large number:")



output = [int(x) if x.isdigit() else x  
          for z in ln for x in str(z)] 


print ("sum: " + "+" .join(map(str, output, )))
print(sum(output))