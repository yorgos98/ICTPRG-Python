#Write a program that enters a string containing a person's full name and then output their initials. Example:

#Full Name: Lachlan van der Velden
#Initials: LVDV
#Full Name: Dave Verg Douglas
#Initials: DVD




g = ''

n = input("please enter your name: ")

nl = n.split(' ')

for x in nl:
    g  += x[0]


print('Initials: ' + g.upper(), end="")