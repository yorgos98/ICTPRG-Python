Rsalary = 50000
Ryears = 3

Salary = int(input("What is your salary ? : "))
Years = int(input("How many years have you worked? : "))

if Salary >= Rsalary and Years >= Ryears:
      print ("Your Loan application has been proccessed")
   
elif Salary < Rsalary and Years < Ryears:
    print ("Applogies your application has been rejected")
           