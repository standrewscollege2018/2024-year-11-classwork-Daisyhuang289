ask = True
all_cars = {"1":["Toyota Corolla", 4], "2":["Honda CRV", 4], "3":["Suzuki Swift", 4], "4":["Mitsubishi Airtrek", 4], "5":["Nissan DC Ute", 4], "6":["Toyota Previa", 7], "7":["Toyota Hi Ace", 12], "8":["Toyota Hi Ace", 12]}
av = []
names = []
cars_rented = []

#Continuesly ask for vehicles till 0 is enterewhile ask == True:
while ask == True:
    print("Welcome to the University vheicle rental system")
    askseat = True
    #Continuesly ask for the number of seats, until valid input
    while askseat == True:
        try:
            seats = int(input("How many seats would you like? "))
            #If 0 is entered end the ask loop
            if seats == 0:
                ask = False
                break
            #If there are no cars with that amount of seats
            elif seats != 4 and seats != 7 and seats !=12:
                print(f"There are no {seats} seater cars\n")
            else:
                #Else print the vehicles and number of seats which suit conditions
                m = 0
                for i in all_cars:
                    if all_cars[i][1] == seats:
                        m += 1
                        print(f"{m}. {all_cars[i][0]}({all_cars[i][1]})")
                askseat = False
        #If the seat value is a string
        except ValueError:
            print("Please enter a number\n")
    #Check whether all the cars have been rented
    if len(names) == 8:
        ask = False
    check = True
    #A loop checking whether the number fufills the conditions
    while check == True:
        #If seats value was 0 skip check
        if seats == 0:
            ask = False
            break
        else:
            num = input("Which vehicle would you like to book? ")
            #Checks if input is a integer
            try:
                y = int(num)
                #Check if number is 0, if yes end ask loop
                if y == 0:
                    ask = False
                    break
                #Check whether the value is out of bounds
                if y>m or y<0:
                    print("Please enter one of the available numbers\n")
                #Add the information of the successfully booked vehicle into lists
                else:
                    k=0
                    for i in all_cars:
                        if all_cars[i][1] == seats:
                            k += 1
                            if k == y:
                                #Check whether the vehicle is already booked
                                if i in av:
                                    print("**This vehicle is already booked. Please choose another**\n")
                                #Print the details of the rented vehicle, and append details
                                else:
                                    av.append(i)
                                    cars_rented.append(all_cars[i][0])
                                    print(f"You have booked the {all_cars[i][0]}({all_cars[i][1]})")
                                    all_cars[i][0] += "-Unavailable"
                                    check = False
            #If it is a string
            except ValueError:
                print("Enter a number please\n")
    test = True
    #Check whether the name is blank, if yes keep asking
    while test == True:
        #If the num or seats value equals 0, finish ask loop
        if num == 0 or seats == 0:
            ask = False
            break
        else:
            #If the name value equals zero, end loop
            name = input("What is your name? ")
            if name == "0":
                ask = False
                break
            else:
                #Checks whether the name is blank
                if name.strip() == "":
                    print("Please enter a name\n")
                else:
                    #Add the name which passes the tests into a list
                    names.append(name)
                    print(f"Thanks {name}\n")
                    test = False
#Check whether any cars had been rented
if len(names) == 0:
    print("No cars were rented")
else:
    print("\nDaily Summary")
    x = 0
    #Printing the daily summary
    for i in range(len(names)):
        print(f"{cars_rented[x]} - {names[x]}")
        x += 1
