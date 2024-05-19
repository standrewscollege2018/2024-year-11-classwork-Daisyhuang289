'''~~~~~~~~~~~~~~~~~~~~~~~~~~Speeders Fine Calculation Program~~~~~~~~~~~~~~~~~~~~~~~~~~'''

#Variables#
wanted = ['john smith', 'helga norman', 'zach conroy']
ask = True
speeders = []

'''~~~~~~~~~~~~~~~~~~~~~~~Start of Program~~~~~~~~~~~~~~~~~~~~~~~'''
print("Welcome to the Speeders Fine Calculation system")

#Loop of Menu#
while ask == True:
    #Name of Offender#
    offender = input("\nEnter the name of the offender: ").strip().lower()
    #Errorcatching#
    while offender == '':
        print("Blank is not accepted. Please enter a name")
        offender = input().strip().lower()
    if offender == 'end':
        #End Program#
        ask = False
    else:
        #Check if they are a offender#
        if offender in wanted:
            print(f"** ALERT! There is an arrest warrant for {offender.title()}")

        check = True
        #Speed Limit#
        limit = input("Enter the speed limit (in km/h): ")
        #Errorcatching#
        while check == True:
            try:
                limit = int(limit)
                if limit < 1:
                    print("Unvalid input. Please enter a positive number over 0.")
                    limit = input()
                else:
                    check = False
            except ValueError:
                print("Unvalid input. Please enter a number.")
                limit = input()

        check = True
        #Offender's Speed#
        speed = input("Enter the offender's speed: ")
        #Errorcatching#
        while check == True:
            try:
                speed = int(speed)
                if speed > limit:
                    check = False
                else:
                    print("The speed must be more than the limit")
                    speed = input()
            except ValueError:
                print("Unvalid input. Please enter a number.")
                speed = input()

        #Difference of the offender's speed and the speed limit#
        difference = speed - limit
        #Different Fines#
        if difference < 10:
            fine = 30
        elif difference > 29:
            fine = 180
        elif difference > 19:
            fine = 130
        else:
            fine = 80

        #Print offender's name and fine#
        print(f"{offender.title()} should be fined ${fine}")

        #Create list for offender#
        info = []
        info.append(offender)
        info.append(fine)

        #Create Nested List#
        speeders.append(info)

#Summary#
print("\nEnd of day summary")

#Number of Offenders#
print(f"Total number of fines charged: {len(speeders)}")

#Adding the cost of the fines#
money = 0
for i in speeders:
    money += i[1]

#Printing the total of the fines#
print(f"Total amount of fines: ${money}")

num = 1
#Print the speeders and their fines#
for i in speeders:
    print(f"{num}. {i[0].title()}: ${i[1]}")
    num += 1
'''~~~~~~~~~~~~~~~~~~~End of Program~~~~~~~~~~~~~~~~~~~'''
