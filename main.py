import function
import datetime

def check_user_input():
    global name, address, contact, buyer
    loop = True
    while loop == True:
        try:
             function.ask_user_for_operation()
             user_input = int(input("Enter the number: "))
             dt = datetime.datetime.now()
             t = dt.strftime("%H:%M:%S")
             d = dt.strftime("%d/%m/%Y")
             S = 0
             if user_input == 1:
                bid = function.add_bike_to_2D_list()
                function.bike_display()
                name = input("Enter the Customer Name: ")
                address = input("Enter the Customer Address: ")
                contact = input ("Enter the Customer Contact number: ")
                function.bike_display() 
                the_bike_id = function.validating_bike_id()
                the_q = function.quantity_validation(the_bike_id)
                buyer = int(input("Enter the Amount paid by Customer: "))
                function.finalize_sell(the_bike_id, the_q)
                the_price = function.total_price(the_bike_id, the_q)
                print("Customer Name: ",name)
                print("Customer Address: ",address)
                print("Customer Contact: ",contact)
                print("Amount paid by customer: ", buyer)
                print("The purchased bike  is: " + bid[the_bike_id-1][0]+"\n")
                print("The Company is: " + bid[the_bike_id-1][1]+"\n")
                print("The Bike Color is: " + bid[the_bike_id-1][2]+"\n")
                print("The Quantity: " + str(the_q) +"\n")
                print("The total price of the Bike is:",int(the_price))
                function.customer(the_price, buyer)
                function.purchase_bill(the_bike_id, name, address, contact, the_q, the_price)
                function.purchasing_bike()
                function.purchase_more(the_bike_id,name, address, contact, the_q, the_price)
                print("\n") 

             elif user_input == 2:
                bid1 = function.add_bike_to_2D_list()
                function.bike_display()
                function.technician()
                function.add()
                function.bike_display()
                the_bike_id = function.validating_bike_id2()
                stock = function.quantity_validation2(the_bike_id)
                function.adding_stock(the_bike_id, stock)
                function.adding_bike_to_stock()
                print("Enter Technician Name: ",function.technician_name)
                print("Shipping Company: ",function.shipping_company)
                print("Shipping Cost: ",function.shipping_cost)
                print("The Added bike  is: "+bid1[the_bike_id-1][0]+"\n")
                print("The Added Company name is: " + bid1[the_bike_id-1][1]+"\n")
                print("The Added Bike Color is: " + bid1[the_bike_id-1][2]+"\n")
                print("The Total Quantity Added: " + str(stock) +"\n")
                function.add_to_stock_bill(the_bike_id, function.technician_name, function.shipping_company, function.shipping_cost, stock)
                function.add_more(the_bike_id, stock)
                print("\n")
             elif user_input == 3:
                function.exit_system()
                loop = False
             else:
                function.invalid_user_input()
        except ValueError:
                print("please provide Valid Input!")


check_user_input()
