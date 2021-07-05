# import only needed because of assumption about the year 
import datetime

try:
    # variable to store data in after read from file
    people = []
    
    # get details from file
    with open('people.txt') as f:
        lines = f.read().splitlines()
        person = []

        for l in lines:
            person = l.split('|')

        # detects invalid data doesn't have all three fields
            if  len(person) != 3:
                raise Exception("Invalid Data Input : " + str(l))

            # detects invalid data age is not number
            try:
                test = int(person[2])
            except:
                raise Exception("Invalid Age Input : " + str(l))

            # Filters Data as Specified
            if int(person[2]) <= 50 \
                and str(person[1])[:1].lower() != 'b':
            
                people.append(person)
            else:
                print("Ommitted because of filters : " + str(person))
        # end loop - for l in lines:
    # end with
###############################################

    # output to new file
    with open('userpass.txt', 'w') as f:
        
        for p in people:
            email = p[0][:1].lower() + p[1].lower() + "@DodnGy.net"

            # assumed need to use current year to generate password 
            
            year = datetime.datetime.now().year

            # broke the password into parts to make it a bit simpler
            birthyear = str(year - int(p[2]))
            surname = str(p[1])[:1].upper() + p[1][1:len(p[1])].lower()
            inital = str(p[0])[0].upper()

            # put the parts to
            password = "!" + birthyear + surname + inital + "_\n"
            f.write("|".join([email, password]))
        
        # end loop for p in people
    # end with
    print("Successful Completion")

except Exception as e:
    print(e)
