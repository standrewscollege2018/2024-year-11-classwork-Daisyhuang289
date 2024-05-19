'''A program which asks for input to find names which match conditions'''
'''It will repeat until "quit" is entered'''
import sqlite3

#Conditions
ask = True
keep_ask = True

#Importing database
DATABASE = "../DB Browser/titanic.db"

#Connecting database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

#Instructions on how to quit
print("Enter 'quit' to exit the program")

#Repeatedly ask for the class number untill available input is entered
while ask == True:
    #Ask for input
    classnum = input("\nWhat class do you want to search on? (1-3)  ")
    #Repeatedly check input
    while keep_ask == True:
        #Check whether it is a integer or not
        try:
            #Turn the value to a integer
            class_int = int(classnum)
            #Check whether the value is out of bounds
            if class_int < 1 or class_int > 3:
                #If it is enter error message, and ask for another input
                print("Please enter a available class")
                classnum = input()
            else:
                #Otherwise end the loop
                keep_ask = False
        #If the value is a string
        except ValueError:
            #Check whether the string value is quit (in any form)
            if classnum.strip().lower() == "quit":
                #If it is end the loop
                keep_ask = False
                ask = False
            #Otherwise continue asking for correct input
            else:
                #Print error message, and recieve input
                print("Please enter a integer")
                classnum = input()

    #Check whether quit was entered
    if classnum.strip().lower() == "quit":
        keep_ask = True
    #If it wasn't start the loop asking for survival info
    else:
        #Ask what survival status is wanted for the citeria of the names
        survival = input("\nEnter 1 for list of survivors or 0 for deceased: ")
        #Repeatedly ask until correct input is entered
        while keep_ask == False:
            #Check whether the value is a string or integer
            try:
                #Turn the value into a integer
                survival_int = int(survival)
                #Check whether the value is in the boundaries
                if survival_int < 0 or survival_int > 1:
                    #Print error message and ask for different input
                    print("Please enter a available value")
                    survival = input()
                else:
                    #Find the number of results matching the condition
                    cursor.execute("SELECT COUNT(passenger_id) FROM titanic WHERE class = ? AND survived = ?", (classnum, survival))
                    results = cursor.fetchall()
                    #Print the number of results
                    print(f"\nThere are {results[0][0]} results found")
                    #Find the name of people matching the conditions
                    cursor.execute("SELECT survived, class, name FROM titanic WHERE class = ? AND survived = ?", (classnum, survival))
                    results = cursor.fetchall()
                    #Print all the names
                    for person in results:
                        print(f"{person[2]}")
                    keep_ask = True
            #If the value is a string
            except ValueError:
                #Print error message and ask for different input
                print("Please enter a integer")
                survival = input()

