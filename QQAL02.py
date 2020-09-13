#Design a program which will ask the user to enter the date in the form dd/mm/yyyy. Example 23/08/2019

#The date will be printed like below:

#Date: 23
#Month : 08
#Year: 2019



date_entered = input("Please enter your dob in DD/MM/YYY: ")

date_list = date_entered.split('/')

date = date_list[0]

month = date_list[1]

year = date_list[2]

print("Date: " , date)
print("Month: " , month)
print("Year: " , year)




