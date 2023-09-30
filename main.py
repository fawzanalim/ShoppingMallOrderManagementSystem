   
def main():
    option = ""
    while option != "0": #sotto
        print("Welcome to OOMS\n")
        print("Which type of user are you: ")
        print("1. Customer")
        print("2. Guest")
        print("3. Delivery Staff")
        print("4. Admin")
        print("0. Exit")
        
        option = input("Enter choice: ")
        if (option == "1"):
            customer()
        elif (option == "2"):
            guest()
        elif(option == "3"):
            staff(staffLogin())
        elif (option == "4"):
            if(adminLogin() == True):
                admin()

def adminLogin():
    print("Please Login with your credentials\n")

    while True:
        username = input("Username: ")
        password = input("Password: ")


        try:          #Check if the file exists
            fileAdmin = open("admin.txt", "r")
            adminData = fileAdmin.readline()
            fileAdmin.close()
            if (username == adminData.split("\t")[0] and password == adminData.split("\t")[1]):
                print("Login successful admin!\n")
                return True

        except:         #Check if the file doesnt exist
            if (username == "admin" and password == "1223334444"):
                fileAdmin = open("admin.txt", "w")
                
                fileAdmin.write(username + "\t" + password)
                fileAdmin.close()
                print("Login successful admin!\n")
                return True

        print("Login failed. Try again\n")

def admin():
    
    while True:
        print("Admin Menu: ")
        print("\t1. Add Category")
        print("\t2. Add Item")
        print("\t3. Edit Category")
        print("\t4. Edit Item")
        print("\t5. Delete Category")
        print("\t6. Delete Item")
        print("\t7. Display Categories")
        print("\t8. Display Items")
        print("\t9. Display Orders")
        print("\t10. Add delivery Staff")
        print("\t11. Edit delivery Staff")
        print("\t12. Delete delivery Staff")
        print("\t13. Display delivery Staffs")
        print("\t14. Assign Orders")
        print("\t15. Search")
        print("\t16. Change Password")
        print("\t0. Logout\n")
        option = input("Choose an operation: ")
        print()
        
        if(option == "1"):
            addCategory()
        elif(option == "2"):
            addItem()
        elif(option == "3"):
            editCategory()
        elif(option == "4"):
            editItem()
        elif(option == "5"):
            deleteCatetgory()
        elif(option == "6"):
            deleteItem()
        elif(option == "7"):
            displayCategories()
        elif(option == "8"):
            displayItems()
        elif(option == "9"):
            displayOrders()
        elif(option == "10"):
            addStaff()
        elif(option == "11"):
            editStaff()
        elif(option == "12"):
            deleteStaff()
        elif(option == "13"):
            displayStaffs()
        elif(option == "14"):
            assignOrders()
        elif(option == "15"):
            search()
        elif(option == "16"):
            changePassword()
        elif(option == "0"):
            return
        else:
            print("Invalid input. Try again.\n")

def addCategory():
    
    while True:
        catID = input("Category ID: ")
        catName = input("Category Name: ")
        if catID != "" and catName != "":
            break
    
    file = open("categories.txt", "a")
    file.write(catID + "\t" + catName + "\n")
    file.close()

def addItem():
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Error! There is no existing category. Please add a category first\n")
            return
        
        print("Category ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
        print()
        while True:
            catInput = input("Choose a category ID: ")
            catName = ""
            for category in categories:
                if catInput == category[0]:
                    catName = category[1]
                    break
            if(catName != ""):
                break
            else:
                print("Invalid input. Try again.\n")
        while True:
            itemID = input("Item ID: ")
            if itemID == "":
                print("Invalid input. Try again")
            else:
                break
        
        while True:
            itemName = input("Item Name: ")
            if itemName == "":
                print("Invalid input. Try again")
            else:
                break
        while True:
            try:
                itemQty = int(input("Item Quantity: "))
                if itemQty <= 0:
                    print("Invalid input. Try again")
                else:
                    break
            except:
                print("Invalid input. Try again")
        while True:
            try:
                itemPrice = int(input("Item Price: "))
                if itemPrice <= 0:
                    print("Invalid input. Try again")
                else:
                    break
            except:
                print("Invalid input. Try again")
        
        fileItem = open("items.txt", "a")
        fileItem.write(itemID + "\t" + itemName + "\t" + catInput + "\t" + catName.strip() + "\t" + str(itemQty) + "\t" + str(itemPrice) +"\n")
        fileItem.close()
        
    except:
        print("Error! There is no existing category. Please add a category first\n")
        return
    
def editCategory():
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Error! There is no existing category. Please add a category first\n")
            return
        
        print("Category ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
        print()
        while True:
            catInput = input("Choose a category ID: ")
            catName = ""
            for category in categories:
                if catInput == category[0]:
                    catName = category[1]
                    break
            if(catName != ""):
                break
            else:
                print("Invalid input. Try again.\n")
        while True:
            print("Current Category ID: " + catInput.strip())
            newCatID = input("New Category ID: ")
            if newCatID == "":
                print("Invalid input. Try again.\n")
            else:
                break
        while True:
            print("Current Category Name: " + catName)
            newCatName = input("New Category Name: ")
            if newCatName == "":
                print("Invalid input. Try again.\n")
            else:
                break
        
        for category in categories:
            if catInput == category[0]:
                category[0] = newCatID
                category[1] = newCatName
                break
        
        fileCat = open("categories.txt", "w")
        for category in categories:
            fileCat.write(category[0] + "\t" + category[1].strip() + "\n")
        fileCat.close()
        
        items = []
        fileItem = open("items.txt", "r")
        for line in fileItem:
            items.append(line.split("\t"))
        fileItem.close()
        
        fileItem = open("items.txt", "w")
        
        for item in items:
            if item[2] == catInput:
                item[2] = newCatID
                item[3] = newCatName
            print(item)
            fileItem.write(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3] + "\t" + item[4] + "\t" + item[5].strip() + "\n")
        fileItem.close()
        
    except:
        print("Error! There is no existing category. Please add a category first\n")
        return
    
def editItem():
    try:
        fileItem = open("items.txt", "r")
        items = []
        for line in fileItem:
            items.append(line.split("\t"))
        fileItem.close()
        if(len(items) == 0):
            print("Error! There is no existing item. Please add an item first\n")
            return
        
        print("Item ID\tItem Name\tCategory ID\tCategory Name\tQty\tPrice")
        
        for item in items:
            print(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3] + "\t" + item[4] + "\t" + item[5], end="")
        
        print()
        while True:
            itemInput = input("Choose an item ID: ")
            itemName = ""
            for item in items:
                if itemInput == item[0]:
                    itemName = item[1]
                    itemCat = item[2]
                    itemQty = item[4]
                    itemPrice = item[5]
                    break
            if(itemName != ""):
                break
            else:
                print("Invalid input. Try again.\n")

        while True:
            print("\nCurrent Item ID: " + itemInput)
            newItemID = input("New Item ID: ")
            if newItemID == "":
                print("Invalid input. Try again.\n")
            else:
                break
        while True:
            print("\nCurrent Item Name: ", itemName)
            newItemName = input("New Item Name: ")
            if newItemName == "":
                print("Invalid input. Try again.\n")
            else:
                break
            
        while True:
            print("\nCurrent Item Quantity: ", itemQty.strip())
            try:
                newItemQty = int(input("New Item Quantity: "))
                if newItemQty <= 0:
                    print("Invalid input. Try again")
                else:
                    newItemQty = str(newItemQty)
                    break
            except:
                print("Invalid input. Try again")
        
        while True:
            print("\nCurrent Item Price: ", itemPrice.strip())
            try:
                newItemPrice = int(input("New Item Price: "))
                if newItemPrice <= 0:
                    print("Invalid input. Try again")
                else:
                    newItemPrice = str(newItemPrice)
                    break
            except:
                print("Invalid input. Try again")
                
        print("\nCurrent Item Category: ", itemCat)
            
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()

        print("\nCategory ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
        print()
        while True:
            newItemCat = input("Choose New category ID: ")

            newItemCatName = ""
            for category in categories:
                if newItemCat == category[0]:
                    newItemCatName = category[1]
                    break
            if(newItemCatName != ""):
                break
            else:
                print("Invalid input. Try again.\n")    

        for item in items:
            if itemInput == item[0]:

                item[0] = newItemID

                item[1] = newItemName

                item[2] = newItemCat

                item[3] = newItemCatName

                item[4] = newItemQty
                
                item[5] = newItemPrice
                
                break

        fileItem = open("items.txt", "w")
        for item in items:

            fileItem.write(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3].strip() + "\t" + item[4] + "\t" + item[5].strip() + "\n")

        fileItem.close()
        
        
    except:
        print("Error! There is no existing item. Please add a item first\n")
        return

def deleteCatetgory():
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Error! There is no existing category. Please add a category first\n")
            return
        
        print("Category ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
        print()
        while True:
            catInput = input("Choose a category ID: ")
            catName = ""
            for category in categories:
                if catInput == category[0]:
                    catName = category[1]
                    break
            if(catName != ""):
                break
            else:
                print("Invalid input. Try again.\n")
        
        
        fileCat = open("categories.txt", "w")
        for category in categories:
            if(category[0] != catInput and category[1].strip() != catName):
                fileCat.write(category[0] + "\t" + category[1].strip() + "\n")
        fileCat.close()
        
        items = []
        fileItem = open("items.txt", "r")
        for line in fileItem:
            items.append(line.split("\t"))
        fileItem.close()
        
        fileItem = open("items.txt", "w")
        
        for item in items:
            if(item[2] != catInput and item[3].strip() != catName):
                fileItem.write(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3] + "\t" + item[4] + "\t" + item[5].strip() + "\n")
        fileItem.close()
        
    except:
        print("Error! There is no existing category. Please add a category first\n")
        return
    
def deleteItem():
    try:
        fileItem = open("items.txt", "r")
        items = []
        for line in fileItem:
            items.append(line.split("\t"))
        fileItem.close()
        if(len(items) == 0):
            print("Error! There is no existing item. Please add an item first\n")
            return
        
        print("Item ID\tItem Name\tCategory ID\tCategory Name\tQty\tPrice")
        
        for item in items:
            print(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3] + "\t" + item[4] + "\t" + item[5], end="")
        
        print()
        while True:
            itemInput = input("Choose an item ID: ")
            itemName = ""
            for item in items:
                if itemInput == item[0]:
                    itemName = item[1]
                    break
            if(itemName != ""):
                break
            else:
                print("Invalid input. Try again.\n")

        
       
        fileItem = open("items.txt", "w")

        for item in items:
            if (item[0] != itemInput):
                fileItem.write(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3].strip() + "\t" + item[4].strip() + "\t" + item[5].strip() + "\n")

        fileItem.close()
        
        
    except:
        print("Error! There is no existing item. Please add a item first\n")
        return

def displayCategories():
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Error! There is no existing category. Please add a category first\n")
            return
        
        print("Category ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
    except:
        print("Error! There is no existing category. Please add a category first\n")
        return

def displayItems():
    print("1. Display all items")
    print("2. Display Category-wise")
    option = input("Choose an option: ")
    
    if (option == "1"):
        try:
            fileItem = open("items.txt", "r")
            items = []
            for line in fileItem:
                items.append(line.split("\t"))
            fileItem.close()
            if(len(items) == 0):
                print("Error! There is no existing item. Please add an item first\n")
                return
            
            print("Item ID\tItem Name\tCategory ID\tCategory Name\tQty\tPrice")
            
            for item in items:
                print(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3] + "\t" + item[4] + "\t" + item[5], end="")

        except:
            print("Error! There is no existing item. Please add a item first\n")
            return
    elif(option == "2"):
        try:
            fileCat = open("categories.txt", "r")
            categories = []
            for line in fileCat:
                categories.append(line.split("\t"))
            fileCat.close()
            if(len(categories) == 0):
                print("Error! There is no existing category. Please add a category first\n")
                return
            
            print("Category ID\tCategory Name")
            
            for category in categories:
                print(category[0] + "\t" + category[1], end="")
            
            print()
            while True:
                catInput = input("Choose a category ID: ")
                catName = ""
                for category in categories:
                    if catInput == category[0]:
                        catName = category[1]
                        break
                if(catName != ""):
                    break
                else:
                    print("Invalid input. Try again.\n")
            
        except:
            print("Error! There is no existing category. Please add a category first\n")
            return
        try:
            fileItem = open("items.txt", "r")
            items = []
            for line in fileItem:
                items.append(line.split("\t"))
            fileItem.close()
            if(len(items) == 0):
                print("Error! There is no existing item. Please add an item first\n")
                return
            
            print("Item ID\tItem Name\tCategory ID\tCategory Name\tQty\tPrice")
            
            for item in items:
                if (item[2] == catInput and item[3].strip() == catName.strip()):
                    print(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3] + "\t" + item[4] + "\t" + item[5], end="")

        except:
            print("Error! There is no existing item. Please add a item first\n")
            return
    else:
        print("Invalid input\n")

def displayOrders():
    print("Order ID\tCustomer ID\tStaff ID\tStatus\tPayment Method\tAddress\tItem ID\tItem Name\tItemQty\tItemPrice\tTotal")
    try:
        fileOrders = open("orders.txt", "r")
        
        for line in fileOrders:
            line = line.strip().split("\t")
            
            for i in range(len(line)-1):
                print(line[i], end="\t")
            print(line[-1])
            
        
        fileOrders.close()
    except:
        print("There is no order in the system. Please wait for the customers to make an order.\n ")
        return

def addStaff():
    try:
        file = open("staffs.txt", "r")
        for line in file:
            id = line.strip().split("\t")[0]
        id = int(id) + 1
        id = str(id).zfill(6)
    except:
        id = "000001"
    while True:
        name = input("Name: ")
        if name == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        ic = input("IC/Passport: ")
        if ic == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        phone = input("Phone Number: ")
        if phone == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        email = input("Email: ")
        if email == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        password = input("Password: ")
        if password == "":
            print("Invalid input. Try again.\n")
        else:
            break
        
    file = open("staffs.txt", "a")
    file.write(id + "\t" + name + "\t" + ic + "\t" + phone + "\t" + email + "\t" + password + "\t" + "ACTIVE" + "\n")
    file.close()
        
def editStaff():
    try:
        fileStaff = open("staffs.txt", "r")
        staffs = []
        
        for line in fileStaff:
            staffs.append(line.strip().split("\t"))
        
        fileStaff.close()
        print("Staff ID\tStaff Name\tStaff IC/Passport\tStaff Phone No.\tStaff Email\tStatus")
        for staff in staffs:
            print(staff[0] + "\t" + staff[1] + "\t" + staff[2] + "\t" + staff[3] + "\t" + staff[4] + "\t" + staff[6])
            
        while True:
            staffInput = input("Enter an ID of a staff to edit: ")
            staffName = ""
            for staff in staffs:
                if staffInput == staff[0]:
                    staffName = staff[1]
                    staffIC = staff[2]
                    staffPhone = staff[3]
                    staffEmail = staff[4]
                    staffStatus = staff[6]
                    
                    break
            if staffName == "":
                print("Invalid input. Try again.\n")
            else:
                break
        
        while True:
            print("Current Name: " + staffName)
            newName = input("New Name: ")
            if newName == "":
                print("Invalid input. Try again.\n")
            else:
                break
        while True:
            print("Current IC/Passport: " + staffIC)
            newIC = input("New IC/Passport: ")
            if newIC == "":
                print("Invalid input. Try again.\n")
            else:
                break
        while True:
            print("Current Phone: " + staffPhone)
            newPhone = input("New Phone: ")
            if newPhone == "":
                print("Invalid input. Try again.\n")
            else:
                break
        while True:
            print("Current Email: " + staffEmail)
            newEmail = input("New Email: ")
            if newEmail == "":
                print("Invalid input. Try again.\n")
            else:
                break
        while True:
            print("Current Status: " + staffStatus)
            newStatus = input("New Status[ACTIVE/RESTRICTED]: ")
            if newStatus != "ACTIVE" and newStatus != "RESTRICTED":
                print("Invalid input. Try again.\n")
            else:
                break
        
        fileStaff = open("staffs.txt", "w")
        for staff in staffs:
            if staff[0] == staffInput:
                staff[1] = newName
                staff[2] = newIC
                staff[3] = newPhone
                staff[4] = newEmail
            fileStaff.write(staff[0] + "\t" + staff[1] + "\t" + staff[2] + "\t" + staff[3] + "\t" + staff[4] + "\t" + staff[5] + "\t" + staff[6] + "\n")
        fileStaff.close()
        
        
        
        
            
    except:
        print("There is no staff data in the system. Please add a delivery staff first.")
    print()

def deleteStaff():
    try:
        fileStaff = open("staffs.txt", "r")
        staffs = []
        
        for line in fileStaff:
            staffs.append(line.strip().split("\t"))
        
        fileStaff.close()
        print("Staff ID\tStaff Name\tStaff IC/Passport\tStaff Phone No.\tStaff Email\tStatus")
        for staff in staffs:
            print(staff[0] + "\t" + staff[1] + "\t" + staff[2] + "\t" + staff[3] + "\t" + staff[4] + "\t" + staff[6])
            
        while True:
            staffInput = input("Enter an ID of a staff to delete: ")
            staffName = ""
            for staff in staffs:
                if staffInput == staff[0]:
                    staffName = staff[1]
                    
                    break
            if staffName == "":
                print("Invalid input. Try again.\n")
            else:
                break
        
        
        
        fileStaff = open("staffs.txt", "w")
        for staff in staffs:
            if staff[0] != staffInput:
                fileStaff.write(staff[0] + "\t" + staff[1] + "\t" + staff[2] + "\t" + staff[3] + "\t" + staff[4] + "\t" + staff[5] + "\t" + staff[6] + "\n")
            
        fileStaff.close()
        
        
            
    except:
        print("There is no staff data in the system. Please add a delivery staff first.")
    print()

def displayStaffs():
    try:
        fileStaff = open("staffs.txt", "r")
        staffs = []
        
        for line in fileStaff:
            staffs.append(line.strip().split("\t"))
        
        fileStaff.close()
        print("Staff ID\tStaff Name\tStaff IC/Passport\tStaff Phone No.\tStaff Email\tStatus")
        for staff in staffs:
            print(staff[0] + "\t" + staff[1] + "\t" + staff[2] + "\t" + staff[3] + "\t" + staff[4] + "\t" + staff[6])
    except:
        print("There is no staff data in the system. Please add a delivery staff first.")
    print()
    
def assignOrders():
    print("Order ID\tCustomer ID\tStaff ID\tStatus\tPayment Method\tAddress\tItem ID\tItem Name\tItemQty\tItemPrice\tTotal")
    try:
        fileOrders = open("orders.txt", "r")
        orders = []
        for line in fileOrders:
            orders.append(line.strip().split("\t"))
            line = line.strip().split("\t")
            
            for i in range(len(line)-1):
                print(line[i], end="\t")
            print(line[-1])
            
        
        fileOrders.close()
    except:
        print("There is no order in the system. Please wait for the customers to make an order.\n ")
        return
    
    while True:
        orderID = input("Choose an order: ")
        if orderID == "":
            print("Invalid Input. Try again.\n")
        else:
            chosenOrder = ""
            for order in orders:
                if orderID == order[0]:
                    chosenOrder = order
                    break
            if chosenOrder == "":
                print("Invalid Input. Try again.\n")
            else:
                break
    
    try:
        fileStaff = open("staffs.txt", "r")
        staffs = []
        
        for line in fileStaff:
            staffs.append(line.strip().split("\t"))
        
        fileStaff.close()
        print("Staff ID\tStaff Name\tStaff IC/Passport\tStaff Phone No.\tStaff Email\tStatus")
        for staff in staffs:
            print(staff[0] + "\t" + staff[1] + "\t" + staff[2] + "\t" + staff[3] + "\t" + staff[4] + "\t" + staff[6])
            
        while True:
            staffInput = input("Choose a staff: ")
            staffName = ""
            for staff in staffs:
                if staffInput == staff[0]:
                    staffName = staff[1]
                    
                    break
            if staffName == "":
                print("Invalid input. Try again.\n")
            else:
                break
        
        
        
        fileOrders = open("orders.txt", "w")
        for order in orders:

            if order[0] == orderID:
                order[2] = staffInput
                order[3] = "Assigned"
            fileOrders.write(order[0] + "\t" + order[1] + "\t" + order[2] + "\t" + order[3] + "\t" + order[4] + "\t" + order[5] + "\t" + order[6] + "\t" + order[7] + "\t" + order[8] + "\t" + order[9] + "\t" + order[10] + "\n")
            
        fileOrders.close()
        
        
            
    except:
        print("There is no staff data in the system. Please add a delivery staff first.")
    print()
    
def search():
    
    while True:
        print()
        print("1. Search Item")
        print("2. Search Order")
        print("0. Go Back")
        option = input("Enter your choice: ")
        
        if option == "1":
            try:
                
                fileItem = open("items.txt", "r")
                searchKey = input("Search Keyword: ")
                items = []
                for line in fileItem:
                    items.append(line.split("\t"))
                fileItem.close()
                if(len(items) == 0):
                    print("Error! There is no existing item. Please add an item first\n")
                    return
                
                print("Item ID\tItem Name\tCategory ID\tCategory Name\tQty\tPrice")
                
                for item in items:
                    for i in item:
                        if searchKey.lower() in i.lower():
                            print(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3] + "\t" + item[4] + "\t" + item[5], end="")

            except:
                print("Error! There is no existing item. Please add an item first\n")
                return
        elif option == "2":
            try:
                
                fileOrder = open("orders.txt", "r")
                searchKey = input("Search Keyword: ")
                orders = []
                for line in fileOrder:
                    orders.append(line.split("\t"))
                fileOrder.close()
                if(len(orders) == 0):
                    print("Error! There is no existing order. Please add an order first\n")
                    return
                
                print("Order ID\tCustomer ID\tStaff ID\tStatus\tPayment Method\tAddress\tItem ID\tItem Name\tItemQty\tItemPrice\tTotal")
                
                for order in orders:
                    for o in order:
                        if searchKey.lower() in o.lower():
                            print(order[0] + "\t" + order[1] + "\t" + order[2] + "\t" + order[3] + "\t" + order[4] + "\t" + order[5] + "\t" + order[6] + "\t" + order[7] + "\t" + order[8] + "\t" + order[9] + "\t" + order[10], end="")

            except:
                print("Error! There is no existing item. Please add an item first\n")
                return          

def changePassword():
    fileAdmin = open("admin.txt", "r")
    
    username, currentPass = fileAdmin.readline().strip().split("\t")
    fileAdmin.close()
    
    while True:
        inputPass = input("Enter Current Password: ")
        if(currentPass == inputPass):
            break
    
    while True:
        newPass = input("Enter New Password: ").strip()
        if newPass != "":
            break
        else:
            print("Invalid input. Try again.\n")
    
    fileAdmin = open("admin.txt", "w")
    
    fileAdmin.write(username + "\t" + newPass)
    fileAdmin.close()
  
def guest():
    print("1. Browse through categories")
    print("2. Search item")
    option = input("Enter your choice: ")
    if(option == "1"):
        try:
            fileCat = open("categories.txt", "r")
            categories = []
            for line in fileCat:
                categories.append(line.split("\t"))
            fileCat.close()
            if(len(categories) == 0):
                print("Sorry! There is no existing category at the moment. We are working on it\n")
                return
            
            print("Category ID\tCategory Name")
            
            for category in categories:
                print(category[0] + "\t" + category[1], end="")
            
            print()
            while True:
                catInput = input("Choose a category ID: ")
                catName = ""
                for category in categories:
                    if catInput == category[0]:
                        catName = category[1]
                        break
                if(catName != ""):
                    break
                else:
                    print("Invalid input. Try again.\n")
            
            items = []
            fileItem = open("items.txt", "r")
            for line in fileItem:
                items.append(line.split("\t"))
            fileItem.close()
            
            print("\nItem ID\tItemName")
            for item in items:
                
                if(item[2] == catInput and item[3].strip() == catName.strip()):
                    print(item[0] + "\t" + item[1])
            print("Please login as a customer to get more details about the products. Thank you.\n")
        
            
        except:
            print("Sorry! There is no existing category at the moment. We are working on it\n")

            return
    elif(option == "2"):
        searchKey = input("Search Key: ")
        items = []
        fileItem = open("items.txt", "r")
        for line in fileItem:
            items.append(line.split("\t"))
        fileItem.close()
        
        print("\nItem ID\tItemName")
        for item in items:

            for i in item[0:2]:
                if searchKey.lower() in i.lower():
                    print(item[0] + "\t" + item[1])
        print("Please login as a customer to get more details about the products. Thank you.\n")
    else:
        print("Invalid input.\n")
        
def customer():
    while True:
        print("1. Login")
        print("2. Register")
        print("0. Main Menu")
        
        option = input("Enter your choice: ")
        if(option == "1"):
                customerMenu(customerLogin())
        elif(option == "2"):
                customerMenu(customerRegister())
        elif(option == "0"):
            return
        else:
            print("Invalid input. Try again.\n")

def customerLogin():
    print("Please Login with your credentials\n")

    while True:
        email = input("Email: ")
        if email == "-1":
            return False
        password = input("Password: ")

        
        try:          #Check if the file exists
            file = open("customers.txt", "r")
            for line in file:
                if line.strip().split("\t")[2] == email and line.strip().split("\t")[4] == password:
                    print("Welcome Back " + line.strip().split("\t")[1] + "!\n")
                    file.close()
                    return line.strip().split("\t")[0]
            file.close()
            print("Login Failed. Try again or register.\n")
            print("Type \'-1\' to go back\n")

        except:         #Check if the file doesnt exist
            print("Login failed. Try again or register.")
            print("Type \'-1\' to go back\n")
   
def customerRegister():
    print("Welcome new user!")
    try:
        file = open("customers.txt", "r")
        for line in file:
            id = line.strip().split("\t")[0]
        id = int(id) + 1
        id = str(id).zfill(6)
    except:
        id = "000001"
    
    while True:
        name = input("Enter Name: ")
        if name == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        email = input("Enter Email: ")
        if email == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        phone = input("Enter Phone Number: ")
        if phone == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        password = input("Enter Password: ")
        if password == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        address = input("Enter Address: ")
        if address == "":
            print("Invalid input. Try again.\n")
        else:
            break
        
    file = open("customers.txt", "a")
    file.write(id + "\t" + name + "\t" + email + "\t" + phone + "\t" + password + "\t" + address + "\n")
    file.close()
    return id

def customerMenu(customerID):
    if customerID == False:
        return
    while True:
        print()
        print("1. Browse Items")
        print("2. Search Item")
        print("3. Check Orders")
        print("0. Logout")
        
        option = input("Enter your choice: ")
        if (option == "1"):
            browseItems(customerID)
        elif(option == "2"):
            searchItem(customerID)
        elif(option == "3"):
            customerCheckOrders(customerID)
        elif(option == "0"):
            return
    
def browseItems(customerID):
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Sorry! There is no existing category at the moment. We are working on it\n")
            return
        
        print("Category ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
        print()
        while True:
            catInput = input("Choose a category ID: ")
            catName = ""
            for category in categories:
                if catInput == category[0]:
                    catName = category[1]
                    break
            if(catName != ""):
                break
            else:
                print("Invalid input. Try again.\n")
        
        items = []
        fileItem = open("items.txt", "r")
        for line in fileItem:
            items.append(line.split("\t"))
        fileItem.close()
        
        print("\nItem ID\tItem Name\tQuantity\tPrice")
        for item in items:
            
            if(item[2] == catInput and item[3].strip() == catName.strip()):
                print(item[0] + "\t" + item[1] + "\t" + item[4] + "\t" + item[5].strip())
        
        cartChoice = input("Anything of your interest? Want to add to cart? [Yes/No]: ")
        if(cartChoice.lower() not in ["yes", "y", "yeah", "yup", "ya"]):
            return
        while True:
            itemID = input("Enter Item ID: ")
            if (itemID == "-1"):
                return
            chosenItem = ""
            for item in items:
                
                if item[0] == itemID:
                    
                    chosenItem = item
                    
                    break
            if chosenItem == "":
                print("Invalid input. Try again.")
                print("To go back, enter \'-1\'")
            else:
                break
        while True:
            try:
                itemQty = int(input("Enter Quantity: "))
                if itemQty > int(chosenItem[4]):
                    print("Not enough in stock. Choose less than " + chosenItem[4].strip() + "\n")
                elif itemQty < 0:
                    print("Invalid input. Try again.\n")
                else:
                    break
            except:
                print("Invalid input. Try again.\n")
        order(customerID, chosenItem, itemQty)
        
    except:
        print("Sorry! There is no existing category at the moment. We are working on it\n")

        return

def searchItem(customerID):
    try:
        items = []
        fileItem = open("items.txt", "r")
        for line in fileItem:
            items.append(line.split("\t"))
        fileItem.close()
        while True:
            searchKey = input("Search Key: ")
            if searchKey == "":
                print("Invalid input. Try again.\n")
            else:
                break
        
        print("\nItem ID\tItem Name\tQuantity\tPrice")
        for item in items:
            for i in item[0:2]:
                if searchKey.lower() in i.lower():
                    print(item[0] + "\t" + item[1] + "\t" + item[4] + "\t" + item[5].strip())
        
        cartChoice = input("Anything of your interest? Want to add to cart? [Yes/No]: ")
        if(cartChoice.lower() not in ["yes", "y", "yeah", "yup", "ya"]):
            return
        while True:
            itemID = input("Enter Item ID: ")
            if (itemID == "-1"):
                return
            chosenItem = ""
            for item in items:
                
                if item[0] == itemID:
                    
                    chosenItem = item
                    
                    break
            if chosenItem == "":
                print("Invalid input. Try again.")
                print("To go back, enter \'-1\'")
            else:
                break
        while True:
            try:
                itemQty = int(input("Enter Quantity: "))
                if itemQty > int(chosenItem[4]):
                    print("Not enough in stock. Choose less than " + chosenItem[4].strip() + "\n")
                elif itemQty < 0:
                    print("Invalid input. Try again.\n")
                else:
                    break
            except:
                print("Invalid input. Try again.\n")
        order(customerID, chosenItem, itemQty)
    except:
        print("We dont have any item at the moment. Please wait while we are updating our inventory. TQ\n")
        return

def order(customerID, product, qty):

    if qty == 0:
        return

    total = qty * int(product[5].strip())
    print("\nYour total is RM " + str(total))
    print("Pay by card")
    print("Cancel payment by entering \'-1\'")
    while True:
        cardNumber = input("Card Number: ")[-4:]
        if cardNumber == -1:
            return
        if cardNumber == "":
            print("Invalid Input. Try again.\n")
        else:
            break
    while True:
        cardExpiry = input("Expiry Date[MM/YY]: ")
        if cardExpiry == "":
            print("Invalid Input. Try again.\n")
        else:
            break
    while True:
        cardCVV = input("CVV: ")
        if cardCVV == "":
            print("Invalid Input. Try again.\n")
        else:
            break
    
    
    fileItem = open("items.txt", "r")
    items = []
    for line in fileItem:
        items.append(line.split("\t"))
    fileItem.close()
    
    
    for item in items:
        if product[0] == item[0]:
            item[4] = str(int(item[4].strip()) - qty)
            break
        

    fileItem = open("items.txt", "w")
    for item in items:

        fileItem.write(item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3].strip() + "\t" + item[4] + "\t" + item[5].strip() + "\n")

    fileItem.close()
    
    try:
        file = open("orders.txt", "r")
        for line in file:
            orderID = line.strip().split("\t")[0]
        orderID = int(orderID) + 1
        orderID = str(orderID).zfill(6)
        file.close()
    except:
        orderID = "000001"
    
    fileCustomer = open("customers.txt", "r")
    for line in fileCustomer:
        if customerID == line.strip().split("\t")[0]:
            customerAdd = line.strip().split("\t")[5]
    fileCustomer.close()

    
    
    fileOrder = open("orders.txt", "a")
    fileOrder.write(orderID + "\t" + customerID + "\t000000\tPaid\tCard-" + cardNumber + "\t" + customerAdd + "\t" + product[0] + "\t" + product[1] + "\t" + str(qty) + "\t" + product[5].strip() + "\t" + str(total) + "\n")
    fileOrder.close()

def customerCheckOrders(customerID):
    print("Order ID\tStatus\tPayment Method\tAddress\tItem ID\tItem Name\tItemQty\tItemPrice\tTotal")
    try:
        fileOrders = open("orders.txt", "r")
        
        for line in fileOrders:
            line = line.strip().split("\t")
            if(customerID == line[1]):
                print(line[0] + "\t" + line[3] + "\t" + line[4] + "\t" + line[5] + "\t" + line[6] + "\t" + line[7] + "\t" + line[8] + "\t" + line[9] + "\t" + line[10])
        
        fileOrders.close()
    except:
        print("There is no order in the system. Please wait for the customers to make an order.\n ")
        return

def staffLogin():
    print("Please Login with your credentials\n")

    while True:
        email = input("Email: ")
        if email == "-1":
            return False
        password = input("Password: ")

        
        try:          #Check if the file exists
            file = open("staffs.txt", "r")
            for line in file:
                
                if line.strip().split("\t")[4] == email and line.strip().split("\t")[5] == password:
                    print("Welcome Back " + line.strip().split("\t")[1] + "!\n")
                    file.close()
                    return line.strip().split("\t")[0]
            file.close()
            print("Login Failed. Try again.")
            print("Type \'-1\' to go back\n")

        except:         #Check if the file doesnt exist
            print("Login failed. Try again.")
            print("Type \'-1\' to go back\n")
        
def staff(staffID):
    if staffID == False:
        return
    
    
    while True:
        print("\n1. Check Assigned Orders")
        print("2. Check Delivered Orders")
        print("3. Update Order Status")
        
        print("0. Logout")
        
        option = input("Enter your choice: ")
        
        if option == "1":
            print("Order ID\tCustomer ID\tStaff ID\tStatus\tPayment Method\tAddress\tItem ID\tItem Name\tItemQty\tItemPrice\tTotal")
            try:
                fileOrders = open("orders.txt", "r")
                
                for line in fileOrders:
                    line = line.strip().split("\t")
                    
                    if line[2] == staffID and line[3] == "Assigned":
                        for i in range(len(line)-1):
                            print(line[i], end="\t")
                        print(line[-1])
                    
                
                fileOrders.close()
            except:
                print("There is no order in the system. Please wait for the customers to make an order.\n ")
                return
        elif option == "2":
            print("Order ID\tCustomer ID\tStaff ID\tStatus\tPayment Method\tAddress\tItem ID\tItem Name\tItemQty\tItemPrice\tTotal")
            try:
                fileOrders = open("orders.txt", "r")
                
                for line in fileOrders:
                    line = line.strip().split("\t")
                    
                    if line[2] == staffID and line[3] == "Delivered":
                        for i in range(len(line)-1):
                            print(line[i], end="\t")
                        print(line[-1])
                    
                
                fileOrders.close()
            except:
                print("There is no order in the system. Please wait for the customers to make an order.\n ")
                return
        elif option == "3":
            count = 0
            print("Order ID\tCustomer ID\tStaff ID\tStatus\tPayment Method\tAddress\tItem ID\tItem Name\tItemQty\tItemPrice\tTotal")
            try:
                fileOrders = open("orders.txt", "r")
                orders = []
                
                for line in fileOrders:
                    orders.append(line.strip().split("\t"))
                    line = line.strip().split("\t")
                    
                    if line[2] == staffID and line[3] == "Assigned":
                        count += 1
                        for i in range(len(line)-1):
                            print(line[i], end="\t")
                        print(line[-1])
                    
                
                fileOrders.close()
            except:
                print("There is no order in the system. Please wait for the customers to make an order.\n ")
                return
            
            if count == 0:
                print("You do not have anymore assigned order.")
                continue
            while True:
                orderID = input("Choose an order: ")
                if orderID == "":
                    print("Invalid Input. Try again.\n")
                else:
                    chosenOrder = ""
                    for order in orders:
                        if orderID == order[0]:
                            chosenOrder = order
                            break
                    if chosenOrder == "":
                        print("Invalid Input. Try again.\n")
                    else:
                        break
            
            
            confirmation = input("Change status from ASSIGNED to DELIVERED? [Yes/No]: ").lower()
            
            if confirmation not in ["yes", "y"]:
                continue
            fileOrders = open("orders.txt", "w")
            for order in orders:

                if order[0] == orderID and order[2] == staffID:
                    order[3] = "Delivered"
                    
                fileOrders.write(order[0] + "\t" + order[1] + "\t" + order[2] + "\t" + order[3] + "\t" + order[4] + "\t" + order[5] + "\t" + order[6] + "\t" + order[7] + "\t" + order[8] + "\t" + order[9] + "\t" + order[10] + "\n")
                
            fileOrders.close()
                

            print()
        elif option == "0":
            return
        else:
            print("Invalid input. Try again.")
    

if __name__ == "__main__":
    main()