#Given the following python code

#values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
#Sum all of the numbers and output the result
#Average all of the numbers and output the result
#Output the maximum number in the list 12/13




values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]

total = []


for x in values:
    total.append(x)

print(sum(total))

avg  = sum(values) / len(values)

print(avg)

m_num = values[12]

print(m_num)
