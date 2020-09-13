
Numbers = []
rn= []

while True:
    n = input("Please enter a number:")
    
    if n == "x":
        break

    else:
            Numbers.append(n)

for x in Numbers:
    if Numbers.count(x) >1:
        if rn.count(x) == 0:
             rn.append(x)



print("Repeating numbers:", rn)            







