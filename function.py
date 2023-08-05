import datetime

#the given below function displays the welcome message to the user
def welcome_to_program():
    print("\n")
    print("                                                    ***********************************************                                                  ")
    print("               KISHOR BAMJAN TAMANG                 *WELCOME TO THE BIKE MANAGEMENT SYSTEM PROGRAM*                 LONDON-MET ID 21040608           ")
    print("                                                    ***********************************************                                                  ")
    print("\n")

#the given function displays the bikes from the text file to the user
def bike_display():
        print("\n")
        print("----------------------------------------------------------------------------------------------------------------")
        print("Bike ID \t Bike-Name \t\t Company Name \t\t Colour \t\t Quantity \t Price |")
        print("----------------------------------------------------------------------------------------------------------------")
        try:
         file = open("bike.txt","r")
         a=1
         for line in file:
            print(a,"\t\t"+ line.replace(",","\t\t"))
            a=a+1
         print("----------------------------------------------------------------------------------------------------------------")
         print("\n")
         file.close()
        except:
             print("file name misplaced!")

#the given function adds the bikes from the text file to the 2D list
def add_bike_to_2D_list():
    read_file = open("bike.txt","r")
    my_list = []
    for i in read_file:
        i = i.replace("\n","")
        my_list.append(i.split(","))
    
    return my_list

#the given below function displays options for the users in the system
def ask_user_for_operation():
    print("+++++++++++++++++++++++++++++++++++++")
    print("Enter 1 to purchase the bike:    ++++")
    print("Enter 2 to add stock:            ++++")
    print("Enter 3 to exit:                 ++++")
    print("+++++++++++++++++++++++++++++++++++++")
    print("\n")

def ask_user_for_operation1():
    print("+++++++++++++++++++++++++++++++++++++")
    print("++++++++      Enter Yes       +++++++")
    print("++++++++      Enter No:       +++++++")
    print("+++++++++++++++++++++++++++++++++++++")
    print("\n")    


#the given below function validate the bike ID
def validating_bike_id():
 loop = True
 while loop == True:
   try:
    valid_id = int(input("Enter the ID of bike you want to buy:"))
    print("\n")
    while valid_id<=0 or valid_id>len(add_bike_to_2D_list()):
        print("\n")
        print("+++++++++++++++++++++++++++++++++++++")
        print("Please provide a  valid Bike ID !!!")
        print("+++++++++++++++++++++++++++++++++++++")
        print("\n")
        valid_id = int(input("Enter the ID of bike you want to buy:"))
        bike_display()
        print("\n")
    return valid_id
    loop = False
   except ValueError:
          print("please provide proper integer value!")

def validating_bike_id2():
 loop = True
 while loop == True:
   try:  
    valid_id = int(input("Enter the ID of bike you want to Add:"))
    print("\n")
    while valid_id<=0 or valid_id>len(add_bike_to_2D_list()):
        print("\n")
        print("+++++++++++++++++++++++++++++++++++++")
        print("Please provide a  valid Bike ID !!!")
        print("+++++++++++++++++++++++++++++++++++++")
        print("\n")
        valid_id = int(input("Enter the ID of bike you want to Add:"))
        bike_display()
        print("\n")
    return valid_id
    loop = False
   except ValueError:
          print("please provide proper integer value!")

def technician():    
    global technician_name
    technician_name = input("Enter the Technician Name: ")
    
#the given below function is called when user press 1
def adding_bike_to_stock():
    print("\n")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("The Bike has been added to the stock")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("\n")

#the given below function is called when user press 2
def purchasing_bike():
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++")
    print("Thank you for purchasing the bike")
    print("++++++++++++++++++++++++++++++++++++++++")
    print("\n")    

#the given below function is called when the user gives invalid input
def invalid_user_input():
    print("\n")
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("invalid input!!!")
    print("Please provide value as 1,2 or 3.")
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("\n")

#the given below function is called when user press 3
def exit_system():
    print("\n")
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("Thank you for using our system")
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("\n")

def quantity_validation(the_bike_id):
 loop = True
 while loop == True:
   try:     
    bike_list = add_bike_to_2D_list()
    user_quantity = int(input("Enter the quantity you want to purchase: "))
    print("\n")
    while user_quantity <=0 or user_quantity>int(bike_list[the_bike_id - 1][3]):
        print("\n")
        print("+++++++++++++++++++++++++++++++++++++")
        print("Please provide a  valid Qunatity ID !!!")
        print("+++++++++++++++++++++++++++++++++++++")
        print("\n")
        user_quantity = int(input("Enter the quantity you want to purchase: "))
        bike_display()
        print("\n")
    return user_quantity
    loop = False
   except ValueError:
          print("please provide proper integer value!")

def purchase_more(the_bike_id,name, address, contact, the_q, the_price):
 loop = True
 while loop == True:
    ask_user_for_operation1()
    user_quantity = str(input("Do you want to purchase another bike: "))
    print("\n") 
    if user_quantity.upper() == "YES":
        bid = add_bike_to_2D_list()
        bike_display()
        name = input("Enter the Customer Name: ")
        address = input("Enter the Customer Address: ")
        contact = input ("Enter the Customer Contact number: ")
        bike_display()
        the_bike_id = validating_bike_id()
        the_price1 = total_price(the_bike_id, the_q)
        the_q = quantity_validation(the_bike_id)
        print("The total price of the Bike is:",the_price1)
        buyer = int(input("Enter the Amount paid by Customer: "))
        finalize_sell(the_bike_id, the_q)
        print("Customer Name: ",name)
        print("Customer Address: ",address)
        print("Customer Contact: ",contact)
        print("Amount paid by customer: ", buyer)
        print("The purchased bike  is: " + bid[the_bike_id-1][0]+"\n")
        print("The Company is: " + bid[the_bike_id-1][1]+"\n")
        print("The Bike Color is: " + bid[the_bike_id-1][2]+"\n")
        print("The Quantity: " + str(the_q) +"\n")
        customer2(the_price1, buyer)
        print("\n")
        purchase_bill_2(the_bike_id, name, address, contact, the_q, the_price1)
    elif user_quantity.upper() == "NO":
        exit_system()
        loop = False
    else:
        print("please provide the Valid Input!")

def add_more(the_bike_id, stock):
 loop = True
 while loop == True:
    ask_user_for_operation1()
    user_quantity = str(input("Do you want to Add another Bike: "))
    print("\n") 
    if user_quantity.upper() == "YES":
        bid1 = add_bike_to_2D_list()
        bike_display()
        the_bike_id = validating_bike_id2()
        stock = quantity_validation2(the_bike_id)
        adding_stock(the_bike_id, stock)
        adding_bike_to_stock()
        print("Enter Technician Name: ",technician_name)
        print("Shipping Company: ",shipping_company)
        print("Shipping Cost: ",shipping_cost)
        print("The Added bike  is: "+bid1[the_bike_id-1][0]+"\n")
        print("The Added Company name is: " + bid1[the_bike_id-1][1]+"\n")
        print("The Added Bike Color is: " + bid1[the_bike_id-1][2]+"\n")
        print("The Total Quantity Added: " + str(stock) +"\n")
        print("\n")
        add_to_stock_bill_2(the_bike_id, technician_name, shipping_company, shipping_cost, stock)
    elif user_quantity.upper() == "NO":
        exit_system()
        loop = False
    else:
        print("please provide the Valid Input!")
      
def quantity_validation2(the_bike_id):
 loop = True
 while loop == True:
   try:    
    bike_list = add_bike_to_2D_list()
    user_quantity = int(input("Enter the quantity you want to ADD: "))
    print("\n")
    while user_quantity <= 0:
        print("\n")
        print("+++++++++++++++++++++++++++++++++++++")
        print("Please provide a  valid Qunatity ID !!!")
        print("+++++++++++++++++++++++++++++++++++++")
        print("\n")
        user_quantity = int(input("Enter the quantity you want to Add: "))
        bike_display()
        print("\n")
    return user_quantity
    loop = False
   except ValueError:
        print("please provide proper integer value!")

def update_stock(bike_list):
    file = open("bike.txt","w")
    for i in bike_list:
        file.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+"\n")
    file.close()
    bike_display()

def customer(the_price, buyer):
    toptbpbb = the_price
    byr = buyer
    p1 = int(toptbpbb-byr)
    p2 = int(byr-toptbpbb)
    if toptbpbb<byr:
        print("The Return Amount: ",p2)
    elif toptbpbb>byr:
        print("The Due amount",p1)
    else:
        print("The Amount is Cleared")

def customer2(the_price1, buyer):
    toptbpbb = the_price1
    byr = buyer
    p1 = int(toptbpbb-byr)
    p2 = int(byr-toptbpbb)
    if toptbpbb<byr:
        print("The Return Amount: ",p2)
    elif toptbpbb>byr:
        print("The Due amount",p1)
    else:
        print("The Amount is Cleared")        
              

def finalize_sell(the_bike_id, the_q):
    bike_list = add_bike_to_2D_list()
    bike_list[the_bike_id - 1][3] = int(bike_list[the_bike_id - 1] [3])- the_q
    update_stock(bike_list)

def purchase_bill(the_bike_id, name, address, contact, the_q, the_price):
    dt = datetime.datetime.now()
    t = dt.strftime("%H:%M:%S")
    d = dt.strftime("%d/%m/%Y")
    S = 0
    bike_list = add_bike_to_2D_list()
    bikeid = the_bike_id
    mycn = name
    myca = address
    mycc = contact
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    second = str(datetime.datetime.now().second)
    pbike = str(bike_list[the_bike_id-1][0])
    pcompany = str(bike_list[the_bike_id-1][1])
    bike_coloo = str(bike_list[the_bike_id-1][2])
    quantity = str(the_q)
    pricee = str(the_price)
    
    with open("Purchase-"+ name +"-"+ year + month+".txt", "w") as b:
        b.write("                                                                   ************************                                                                    \n")
        b.write("                                                                   *LONDON-MET_ID-21040608*                                                                    \n")
        b.write("                       *******************                         ************************                              ****************                      \n")
        b.write("                       *ISLONGTON_COLLEGE*                     *******************************                           *NP01NT4A210045*                      \n")
        b.write("                       *******************                     *Bike Management Purchase Bill*                           ****************                      \n")
        b.write("                                                               *******************************                                                                 \n\n\n\n")
        b.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------- \n")
        b.write("S.N  |   Name       |   Address   |     Bike_Name  |   Company_Name   |  Color       |  Quntity  |    Date     |      Time      |     Contact  |   TOtal ""\n")
        b.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------- \n")
        b.write(str(the_bike_id) +" \t "+mycn+"\t\t"+myca+"\t\t"+pbike+"\t"+pcompany+"\t"+bike_coloo+"\t    "+quantity+"\t   "+d+"\t   "+t+"\t\t"+mycc+"\t  "+str(pricee)+"\n")
        
        
def purchase_bill_2(the_bike_id, name, address, contact, the_q, the_price1):
    dt = datetime.datetime.now()
    tt = dt.strftime("%H:%M:%S")
    dd = dt.strftime("%d/%m/%Y")
    S = 0
    bike_list = add_bike_to_2D_list()
    bikeid = the_bike_id
    na = name
    ad = address
    co = contact
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    second = str(datetime.datetime.now().second)
    pbikee = str(bike_list[the_bike_id-1][0])
    pcompanyy = str(bike_list[the_bike_id-1][1])
    bike_coloor = str(bike_list[the_bike_id-1][2])
    quantityyy = str(the_q)
    tpricee = str(the_price1)

    with open("Purchase-"+ name+"-"+ year +month+".txt", "a") as b:
        b.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------- \n")
        b.write(str(the_bike_id) +" \t "+na+"\t\t"+ad+"\t\t"+pbikee+"\t"+pcompanyy+"\t"+bike_coloor+"\t    "+quantityyy+"\t   "+dd+"\t   "+ tt+"\t\t"+co+"\t  "+str(tpricee)+"\n")
        b.write("------------------------------------------------------------------------------------------------------------------------------------------------------------- \n")
               
def add():
    global shipping_company, shipping_cost
    shipping_company = input("Enter the Name of Shipping Company: ")
    loop = True
    while loop == True:
        try:
            shipping_cost = int(input("Enter the shipping cost: "))
            loop = False
        except ValueError:
            print("please provide integer Value!")


def add_to_stock_bill(the_bike_id, technician_name, shipping_company, shipping_cost, stock):
    dt = datetime.datetime.now()
    t = dt.strftime("%H:%M:%S")
    d = dt.strftime("%d/%m/%Y")
    S = 0
    bike_list1 = add_bike_to_2D_list()
    bikeidd = the_bike_id
    tn = technician_name
    sc = shipping_company
    scc = shipping_cost
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    second = str(datetime.datetime.now().second)
    addedbike = str(bike_list1[the_bike_id-1][0])
    addedcompany = str(bike_list1[the_bike_id-1][1])
    bikecolor = str(bike_list1[the_bike_id-1][2])
    tqadded = str(stock)
    tpotb = str(int(stock) *int(bike_list1[the_bike_id-1][4].replace("$","")))
    
    with open("Add-"+technician_name+"-" + year + month+".txt", "w") as f:
        f.write("                                                                   ************************                                                                    \n")
        f.write("                                                                   *LONDON-MET_ID-21040608*                                                                    \n")
        f.write("                       *******************                         ************************                              ****************                      \n")
        f.write("                       *ISLONGTON_COLLEGE*                     *******************************                           *NP01NT4A210045*                      \n")
        f.write("                       *******************                     * Stock Added In the System    *                           ****************                      \n")
        f.write("                                                               *******************************                                                                 \n\n\n\n")
        f.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------- \n")
        f.write("S.N  |   Technician_Name   |    Shipping_Company   |    Shipping_Cost  |    Bike_Name   |    Company_Name       |  Color       |    Date      |     Time  |  Quantity  | Total""\n")
        f.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------- \n")
        f.write(str(the_bike_id) +" \t "+tn+"\t\t\t"+sc+"\t\t        "+str(scc)+"\t\t   "+addedbike+"\t   "+addedcompany+"\t    "+bikecolor+"\t    "+d+"\t    "+t+"\t "+str(tqadded)+" \t "+str(tpotb)+"\n")
        
        

def add_to_stock_bill_2(the_bike_id, technician_name, shipping_company, shipping_cost, stock):
    dt = datetime.datetime.now()
    t = dt.strftime("%H:%M:%S")
    d = dt.strftime("%d/%m/%Y")
    S = 0
    bike_list1 = add_bike_to_2D_list()
    bikeidd = the_bike_id
    tn = technician_name
    sc = shipping_company
    scc = shipping_cost
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    second = str(datetime.datetime.now().second)
    addedbike = str(bike_list1[the_bike_id-1][0])
    addedcompany = str(bike_list1[the_bike_id-1][1])
    bikecolor = str(bike_list1[the_bike_id-1][2])
    tqadded = str(stock)
    tpotb = str(int(stock) *int(bike_list1[the_bike_id-1][4].replace("$","")))
    
    with open("Add-"+technician_name+"-" + year + month+".txt", "a") as f:
        f.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------- \n")
        f.write(str(the_bike_id) +" \t "+tn+"\t\t\t"+sc+"\t\t        "+str(scc)+"\t\t   "+addedbike+"\t   "+addedcompany+"\t    "+bikecolor+"\t    "+d+"\t    "+t+"\t "+str(tqadded)+" \t "+str(tpotb)+"\n")
        f.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------- \n")

def total_price(the_bike_id, the_q):
    bike_list = add_bike_to_2D_list()
    total_price = int(bike_list[the_bike_id-1] [4].replace("$",""))*the_q
    return total_price    
    
def update_stock1(bike_list1):
    file = open("bike.txt", "w")
    for i in bike_list1:
        file.write(str(i[0])+","+str(i[1])+","+str(i[2]) + ","+str(i[3])+","+str(i[4])+"\n")
    file.close()
    
    bike_display()    

def adding_stock(the_bike_id, stock):
    bike_list = add_bike_to_2D_list()
    bike_list[the_bike_id - 1][3] = int(bike_list[the_bike_id-1] [3]) + stock
    update_stock(bike_list)


#calling function to execute the function
welcome_to_program()
bike_display()
