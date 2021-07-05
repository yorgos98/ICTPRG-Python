

while True:
  print(" 1. add new order""\n","2. list all orders""\n","3. exit" )
  choice = input("Please select from the above: ")




  if choice == "1":
    f = open("orders.txt","a")
    Name = input("What is your name ?: ")
    Burger = input("How many burgers ?: ")
    Fries = input("How many fries ?: ")
    Coke = input("How many cokes ?: ")
    f.write(Name+"|"+Burger+"|"+Fries+"|"+Coke+"\n")
    f.close()


  elif choice == "2":
    with open ('orders.txt', 'r') as orders:
            count = 1
            print ()
            for line in orders.readlines():
                a,b,c,d = line.strip().split('|')
                read_orders = (f'{count}.  {a},\t{b} Burger(s), {c} Fries, {d} Cokes')
                count += 1
                print (read_orders)
                orders.close()
    
  elif choice == "3":
      break  
    
    


    
   
   
    
