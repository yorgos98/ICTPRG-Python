#Write a program that asks the user for their full name, splits it up into words and outputs each word on a new line. For names with 2 words (eg, 'Fred Frank') this would output Fred, then frank on two lines.

g = []

name = input("please enter your first name: ")
namel = input("Please enter your seccond name: ")


g.append(name)
g.append(namel)

print(g[0])
print(g[1])

