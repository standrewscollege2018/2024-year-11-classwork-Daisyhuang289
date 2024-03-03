#Function which prints the list of cars
def av_cars(x):
    print("Welcome to the University vehicle rental system\n")
    print("The vehicles are:")
    z = 0
    for i in all_cars:
        z += 1
        print(f"{z}. {x[i]}")
ask = True
all_cars = {"1":"Toyota Corolla(4)", "2":"Honda CRV(4)", "3":"Suzuki Swift(4)", "4":"Mitsubishi Airtrek(4)", "5":"Nissan DC Ute(4)", "6":"Toyota Previa (7)", "7":"Toyota Hi Ace(12)", "8":"Toyota Hi Ace(12)"}
av = []
names = []
cars_rented = []
av_cars(all_cars)
#Continuesly ask for vehicles till 0 is entered
while ask == True:
    num = input("Which vehicle would you like to book? ")
    #Checks if input is a integer
    try:
        y = int(num)
        #Check whether it is a blank response
        if num.strip() == "":
            print("Enter a number please\n")
        #Check whether the value is out of bounds
        elif int(num)>8 or int(num)<0:
            print("Please enter one of the available numbers\n")
        #Check whether the value is 0, if yes end loop
        elif int(num) == 0:
            ask = False
        #Check whether all cars have been rented or not
        elif len(names) == 8:
            ask = False
        #Check whether the vehicle is already rented
        elif num in av:
            print("**This vehicle is already booked. Please choose another**\n")
        #Add the information of the successfully booked vehicle into lists
        else:
            av.append(num)
            cars_rented.append(all_cars[num])
            print(f"You have booked the {all_cars[num]}")
            #Adding "-Unavailable" at the end to show unavailibility
            all_cars[num] += "-Unavailable"
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
            av_cars(all_cars)
    except ValueError:
        print("Enter a number please\n")
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
