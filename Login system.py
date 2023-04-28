# main file 
import getpass
import time
#def manager():
 #   import manager
#def employee():
#    import employee
medicines = {"A tablet":50 , "B tablet":50 ,"C tablet":60 ,"D tablet":50 ,"E tablet":100 ,
            "F tablet":80 ,"G tablet":20 ,"H tablet":50 ,"I tablet":60 ,"J tablet":90 ,
            "K tablet":40 ,"L tablet":90 ,"M tablet":100 ,"N tablet":100 ,"O tablet":90 ,
            "P tablet":90 ,"Q tablet":80 ,"R tablet":80 ,"S tablet":80 ,"T tablet":100 ,
            "U tablet":80 ,"V tablet":100 ,"W tablet":90 ,"X tablet":90 ,"Y tablet":100 ,"Z tablet":100}
prices  = {"A tablet":10 , "B tablet":20 ,"C tablet":60 ,"D tablet":50 ,"E tablet":95 ,
        "F tablet":80 ,"G tablet":20 ,"H tablet":50 ,"I tablet":60 ,"J tablet":35 ,
        "K tablet":40 ,"L tablet":90 ,"M tablet":90 ,"N tablet":100 ,"O tablet":90 ,
        "P tablet":90 ,"Q tablet":80 ,"R tablet":80 ,"S tablet":80 ,"T tablet":100 ,
        "U tablet":80 ,"V tablet":100 ,"W tablet":90 ,"X tablet":90 ,"Y tablet":100 ,"Z tablet":100}
global profit 
profit = 0
sales = {}
def slp(sec):
    time.sleep(sec)
def slp2(sec):
    print("\t\t Loading",end="")
    for i in range(sec):
        print(".",end="",flush=True)
        time.sleep(1)
class employee_1():
    def Add_medicine(self):
        print("\n\t\t 1. Add new medicine")
        print("\t\t 2. Add quantity in existing medicine")
        try: uc = int(input("\n\t\t Enter your choice: "))
        except: print("Invalid choice because you have entered a string")
        if uc == 1:
            name1 = input("\n\t\t Enter name of medicine: ")
            quantity1 = int(input("\t\t Enter quantity of medicine: "))
            price1 = int(input("\t\t Enter price of medicine per tablet : "))
            if name1 == "":
                print("\t\t Medicine name cannot be empty.Try Again!")
            elif quantity1 == "":
                print("\t\t Quantity cannot be empty.Try Again!")
            elif price1 == "":
                print("\t\t Price cannot be empty.Try Again!")
            elif name1=="" and quantity1=="" and price1=="":
                print("\t\t Medicine name and quantity and price fields cannot be empty.Try Again!")
            else:
                medicines[name1] = quantity1
                prices[name1] = price1
                slp2(2)
                print("\n\t\t Medicine added successfully")
                slp(1)
        elif uc == 2:
            name2 = input("\n\t\t Enter name of medicine : ")
            quantity2 = int(input("\t\tEnter quantity : "))
            for i2 in medicines:
                if i2 == name2:
                    medicines[i2] += quantity2
                    slp2(2)
                    print("\n\t\t Quantity added successfully")
                    slp(1)
                    break
            else:
                slp2(2)
                print("\n\t\t Medicine not found")
                slp(1)
        else:
            print("\n\t\t Invalid Choice.Kindly enter your decision in form of 1 or 2 to perform given task.")  
            slp(1)
    def Delete_medicine(self):
        name_d = input("\n\t\t Enter name of medicine: ")
        for i_i in medicines:
            if i_i == name_d:
                for i_p in prices:
                    if i_p == name_d:
                        prices.pop(i_p)
                        break
                medicines.pop(i_i)
                slp2(2)
                print("\n\t\t Medicine deleted successfully")
                slp(1)
                break
        else:
            slp2(2)
            print("\n\t\t Medicine not found")
            slp(1)
    def Update_medicine(self):
        print("\n\t\t 1. Update name of medicine")
        print("\t\t 2. Update quantity of medicine")
        print("\t\t 3. Update price of medicine")
        try: uc_update = int(input("\t\t Enter your choice: "))
        except: print("\n\t\t Invalid choice because you have entered a string")
        if uc_update == 1:
            previous_m = input("\n\t\t Enter name of medicine: ")
            new_m = input("\t\t Enter new name : ")
            for up_medicines in medicines:
                if up_medicines == previous_m:
                    just = medicines[up_medicines]
                    just2 = prices[up_medicines]
                    medicines.pop(previous_m)
                    prices.pop(previous_m)
                    medicines[new_m] = just
                    prices[new_m] = just2
                    slp2(2)
                    print("\n\t\tMedicine updated successfully")
                    slp(1)
                    break
            else:
                slp2(2)
                print("\n\t\tMedicine not found")
                slp(1)    
        elif uc_update == 2:
            name_u2 = input("\n\t\t Enter name of medicine: ")
            quantity_u2 = int(input("\t\t Enter quantity: "))
            for up_medicinesw in medicines:
                if up_medicinesw == name_u2:
                    store = medicines[up_medicinesw]
                    medicines[up_medicinesw] = quantity_u2
                    slp2(2)
                    print("\n\t\tQuantity updated successfully")
                    print("\t\tPrevious quantity was",store)
                    print("\t\tCurrent quantity is",medicines[up_medicinesw])
                    slp(1)
                    break
            else:
                slp2(2)
                print("\n\t\tMedicine not found")
                slp(2) 
        elif uc_update == 3:
            name_u3 = input("\n\t\t Enter name of medicine: ")
            price_u3 = int(input("\t\t Enter price: "))
            for up_medicinesw3 in prices:
                if up_medicinesw3 == name_u3:
                    store3 = prices[up_medicinesw3]
                    prices[up_medicinesw3] = price_u3
                    slp2(2)
                    print("\n\t\t Price updated successfully")
                    print("\t\t Previous price was",store3)
                    print("\t\t Current price is",prices[up_medicinesw3])
                    slp(1)
                    break
            else:
                slp2(2)
                print("\n\t\t Medicine not found")
                slp(1)       
        else:
            print("\n\t\tInvalid Choice.Kindly enter your decision in form of 1 or 2 to perform given task.")
            slp(1)
    def Search_medicine(self):
        name_s = input("\n\t\t Enter name of medicine: ")
        for i_s in medicines:
            if i_s == name_s:
                slp2(2)
                print("\n\t\t Medicine found")
                print("\t\tName of medicine is : ",i_s)
                print("\t\tQuantity of medicine is : ",medicines[i_s])
                print("\t\tPrice of medicine per tablet is : ",prices[i_s])
                slp(1)
                break
        else:
            slp2(2)
            print("\n\t\tMedicine not found")
            slp(1)
    def Display_medicine(self):
        for i in medicines:
            print("\t\t",i,":",medicines[i],":",prices[i])
        print("\n\t\t Total number of medicines are : ",len(medicines))
        slp(1)

obj = employee_1()
class Customers:
    def customer_services(self):
        print("\n\t\t ************** Customer Services **************")
        name_of_med = input("\n\t\t Enter name of medicine: ")
        # q_of_med = int(input("\t\t Enter quantity of medicine: "))
        for i in medicines:
            if i == name_of_med:
                print("\n\t\t Medicine found")
                print("\t\t Details of medicine are: ")
                name_a = i
                q_a = medicines[i]
                p_a = prices[i]
                print("\n\t\t Name of medicine is: ",name_a)
                print("\t\t Quantity of medicine is: ",q_a)
                print("\t\t Price of medicine per tablet is: ",p_a)
                q_of_med = int(input("\n\t\t Enter quantity of medicine which customer want to purchase : "))
                c_name = input("\n\t\t Enter name of customer: ")
                if medicines[i] >= q_of_med:
                    pp = prices[i]
                    qq = q_of_med
                    result = pp*qq
                    profit=profit +result
                    medicines[i] -= q_of_med
                    print("\n\t\t Medicine purchased successfully")
                    print("\t\t Remaining quantity is",medicines[i])
                    print("\n\t\t ---------- Total price is -----------",result)
                    sales[result]=("Customer name: ",c_name,"Medicine name: ",name_a,"Quantity: ",q_of_med,"Price per tablet : ",pp)
                    break
                else:
                    print("\n\t\t Medicine is out of stock")
                    break
        else:
            print("\n\t\t Medicine not found")
data = Customers()

class LoginSystem:
    def employee(self):
        print("\n\t\t ************** Employee **************")
        print("\t\tEnter your username and password to login")
        u_name = input("\n\t\t Enter your username: ")
        u_pass = getpass.getpass("\t\t Enter your password: ")
        print("\n\t\t Authenticating, please wait ",end="")
        for i in range(3):
            print(".",end="",flush=True)
            time.sleep(1)
        if u_name == "admine" and u_pass == "123":
            while 1:
                print("\n------------------------------------")
                print("1. Customer Services")
                print("2. Exit")
                print("------------------------------------")
                dec = int(input("Enter your choice: "))
                if dec == 1:
                    data.customer_services()
                elif dec == 2:
                    break
                elif dec == 3:
                    print(profit)
                    print(sales)
                else:
                    print("\n\t\t Invalid choice. Try again!")

        elif u_name != "admine":
            print("\n\t\t Invalid username")
        elif u_pass != "123":
            print("\n\t\t Invalid password")
        else:
            print("\n\t\t Invalid username and password")
    def manager(self):
        print("\n\t\t ************** Manager **************")
        print("\t\tEnter your username and password to login")
        u_name = input("\n\t\t Enter your username: ")
        u_pass = getpass.getpass("\t\t Enter your password: ")
        print("\n\t\t Authenticating, please wait ",end="")
        for i in range(3):
            print(".",end="",flush=True)
            time.sleep(1)
        if u_name == "admin" and u_pass == "123":
            while 1:
                slp(1)
                print("\n\n--------------------------------------------------------------------------------------------")
                print("1. Add medicine")
                print("2. Delete medicine")
                print("3. Update medicine")
                print("4. Search medicine")
                print("5. Display all medicines")
                print("6. Exit")
                print("--------------------------------------------------------------------------------------------")
                try: choice = int(input("Enter your choice: "))
                except: print("Invalid choice beacuse you have entered a string")

            # choices = [1,2,3,4,5,6]    
                if choice == 1:
                    obj.Add_medicine()
                elif choice ==2:
                    obj.Delete_medicine()
                elif choice == 3:
                    obj.Update_medicine()
                elif choice == 4:
                    obj.Search_medicine()
                elif choice == 5:
                    obj.Display_medicine()
                elif choice == 6:
                    break
                else:
                    print("Invalid choice.Kindly enter a valid choice from 1 to 6 only") 

        elif u_name != "admin":
            print("\n\t\t Invalid username")
        elif u_pass != "123":
            print("\n\t\t Invalid password")
        else:
            print("\n\t\t Invalid username and password")
    def owner(self):
        pass
    
o = LoginSystem()
while 1:
    print("\n\t\t ************** Login System **************")
    print("\t\t 1. Owner")
    print("\t\t 2. Manager")
    print("\t\t 3. Employee")
    user_dec =  int(input("\n\t\tEnter your choice: "))
    if user_dec == 1:
        o.owner()
    elif user_dec == 2:
        o.manager()
    elif user_dec == 3:
        o.employee()
    else:
        print("\n\t\t Invalid choice. Try again!")    
    