#Function which prints the list of cars
def av_cars(x):
    print("The vehicles are:")
    z = 0
    for i in x:
        z += 1
        print(f"{z}. {x[i][0]}")
def check(x,y):
    try:
        z = int(x)
        av_cars(y)
        #Check whether it is a blank response
        if x.strip() == "":
            print("Enter a number please\n")
        #Check whether the value is 0, if yes end loop
        elif int(x) == 0:
            ask = False
        #Check whether all cars have been rented or not
        elif len(names) == 8:
            ask = False
        #Check whether the vehicle is already rented
        elif x in av:
            print("**This vehicle is already booked. Please choose another**\n")
        #Add the information of the successfully booked vehicle into lists
        else:
            av.append(x)
            cars_rented.append(y[x][0])
            print(f"You have booked the {y[x][0]}")
            #Adding "-Unavailable" at the end to show unavailibility
            y[x] += "-Unavailable"
            test = True
            #Check whether the name is blank, if yes keep asking
            while test == True:
                name = input("What is your name? ")
                if name.strip() == "":
                    print("Please enter a name")
                else:
                    #Add the name which passes the tests into a list
                    names.append(name)
                    print(f"Thanks {name}\n")
                    test = False
    except ValueError:
        print("Enter a number please\n")
ask = True
fourseat = {"1":["Toyota Corolla(4)", "1"], "2":["Honda CRV(4)", "2"], "3":["Suzuki Swift(4)", "3"], "4":["Mitsubishi Airtrek(4)", "4"], "5":["Nissan DC Ute(4)", "5"]}
sevenseat = {"1":["Toyota Previa (7)", "6"]}
twelveseat = {"1":["Toyota Hi Ace(12)", "7"], "2":["Toyota Hi Ace(12)", "8"]}
av = []
names = []
cars_rented = []
#Continuesly ask for vehicles till 0 is entered
while ask == True:
    print("Welcome to the University vehicle rental system\n")
    askseat = True
    while askseat == True:
        try:
            seats = int(input("How many seats would you like? "))
            if seats == 4:
                av_cars(fourseat)
                num = input("Which vehicle would you like to book? ")
                check(num, fourseat)
                askseat = False
            elif seats == 7:
                av_cars(sevenseat)
                num = input("Which vehicle would you like to book? ")
                check(num, sevenseat)
                askseat = False
            elif seats == 12:
                av_cars(twelveseat)
                num = input("Which vehicle would you like to book? ")
                check(num, twelveseat)
                askseat = False
            else:
                print(f"There are no cars with {seats} seats")
        except ValueError:
            print("Please a number")
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
