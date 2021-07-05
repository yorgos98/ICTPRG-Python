
while True:
    
    fname = input('Please enter your first name: ').lower()
    
    if fname =='':
        break
    lname = input('Please enter your last name: ').lower()
    age = int(input('Please enter your age: '))
    year = 2020
    DOB = year - age + 4
    print(fname[0]+lname+'@'+'Huawow.io'+'|'+fname+lname.upper()[0]+'_'+str(DOB))





