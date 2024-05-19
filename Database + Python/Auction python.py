'''Auction program which adds items into the database, and updates values'''
#Setting the connection#
import sqlite3

DATABASE = "../DB Browser/auction.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

#Variables#
ask = True
status = "Unsold"
num = 0

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Start of program~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#Adding items into database#
print("Welcome to the auction program!")
print("Enter quit to stop entering items")
#Loop#
while ask == True:
    #Item name#
    item = input("Enter the item name: ")
    #Check whether value = quit
    if item.strip().lower() == "quit":
        #End loop
        ask = False
    #Check whether value is blank
    elif item.strip() == "":
        #Error message
        print("Please do not enter blanks")
    else:
        #Reserve price#
        reserve = input("Enter the reserve price: ")
        #Check value is integer
        try:
            reserve = float(reserve)
            #Insert values
            cursor.execute("INSERT INTO item (name, reserve, purchaser, salePrice) VALUES (?, ?, ?, ?)", (item, reserve, status, num))
            connection.commit()
        #Value is string
        except ValueError:
            #Check whether value = quit
            if reserve.lower().strip() == "quit":
                #End loop
                ask = False
            else:
                #Error message
                print("Please enter a integer")

#Fetch all information about all items#
cursor.execute("SELECT * FROM item")
results = cursor.fetchall()
#Print information
print(f"{'Item ID':8} {'Item':25} {'Reserve price':13} {'Purchaser':10} {'Sold price':10}")
for item in results:
    if item[4] == 0:
        print(f"{item[0]:8} {item[1]:25} {item[2]:13} {item[3]:10} {'None':10}")
    else:
        print(f"{item[0]:8} {item[1]:25} {item[2]:13} {item[3]:10} {item[4]:10}")

#Entering values for updating#
print("Enter quit to stop")
#Loop#
while ask == False:
    #Item ID#
    ID = input("Enter the item ID: ")
    #Check whether value is integer
    try:
        ID = int(ID)
        #Find all values with same ID
        cursor.execute("SELECT purchaser, reserve FROM item WHERE itemID = ?", (ID, ))
        results = cursor.fetchall()
        #Check whether results were found
        if len(results) == 0:
            #Error message
            print("No results found")
        else:
            #Purchaser#
            purchaser = input("Enter purchaser name: ")
            #Check whether the value = quit
            if purchaser.lower().strip() == "quit":
                #End loop
                ask = True
            #Check whether value is blank
            elif purchaser.strip() == "":
                #Error message
                print("Blanks are not accepted")
            else:
                #Sold price#
                sold = input("Enter the price which it was sold: ")
                #Check whether value is integer
                try:
                    sold = float(sold)
                    #Check whether item has been sold
                    if results[0][0] == "Unsold":
                        #Check whether sold price is under reserve
                        if int(results[0][1]) > sold:
                            print("This price is below the reserve")
                        else:
                            #Update the purchaser value and sale price value for the result with matching ID#
                            cursor.execute("UPDATE item SET salePrice = ? AND purchaser = ? WHERE itemID = ?", (sold, purchaser, ID))
                            connection.commit()
                    else:
                        #Unavailable#
                        print(results[0][0])
                        print("This item has already been sold")
                except ValueError:
                    #Check whether value = quit
                    if sold.lower().strip() == "quit":
                        #End loop
                        ask = True
                    else:
                        #Error message
                        print("Please enter a integer")       
    except ValueError:
        #Check whether value = quit
        if ID.lower().strip() == "quit":
            #End loop
            ask = True
        else:
            #Error message
            print("Please enter a integer")

print("Thanks for using our program")
print("Goodbye!")
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~End program~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
