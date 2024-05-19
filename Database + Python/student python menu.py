''' This program enables users to add students to the database '''

####### This is the setup stuff that will appear on every program ############

# Start by importing the sqlite3 library
import sqlite3

# Set the database that we will connect to
DATABASE = "../DB Browser/students.db"

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

#### Menu system for the program #######
run_program = True
check = True
while run_program:
    print("Main Menu")
    print("=========")
    print("1. Add student")
    print("2. Search for student")
    print("3. See all students")
    print("4. Update student")
    print("5. Quit")

    # get menu selection
    get_selection = True
    while get_selection:
        try:
            selection = int(input("Enter selection: "))
            if selection <1 or selection > 5:
                print("You must enter a number from 1-5")
            else:
                get_selection = False
        except ValueError:
            print("Only numbers from 1-5 allowed")

    # Now that we have the selection, do what the user wants

    ### Add student ###
    if selection == 1:
        print("\nAdd new student")
        #Get info about student
        first_name = input("First name: ")
        last_name = input("Last name: ")
        tutor_group = input("Tutor group: ")
        city = input("City: ")
        while check = True:
            try:
                year_group = int(input("Year group: "))
                if year_group > 13 or year_group < 9:
                    print("Please enter a year between 9 and 13")
                else:
                    cursor.execute("INSERT INTO student (firstName, lastName, tutorGroup, city, yearGroup) VALUES (?, ?, ?, ?, ?)", (first_name.strip(), last_name.strip(), tutor_group.strip(), city.strip(), year_group))
                    #You must add connection.commit() or else the changes will not be saved when you stop the program
                    connection.commit()
                    check = False
            except ValueError:
                print("Please enter a integer")
        
    ### Search for a student ###
    elif selection == 2:
        print("\nSearch for a student")
        name = input("Name: ").strip()
        like_name = f"%{name}%"
        cursor.execute("SELECT * FROM student WHERE firstName LIKE ? or lastName LIKE ?", (like_name, like_name,))
        results = cursor.fetchall()
        if len(results) == 0:
            print("No results found")
        else:
            print(f"{'StudentID':10} {'First Name':10} {'Last Name':10} {'Tutor Group':12} {'City':12} {'Year Group':10}")
            for student in results:
                print(f"{student[0]:10} {student[1]:10} {student[2]:10} {student[3]:12} {student[4]:12 } {student[5]:10}")
    ### Show all students ###
    elif selection == 3:
        print("\nAll students")
        cursor.execute("SELECT firstName, lastName, tutorGroup, city, yearGroup FROM student")
        results = cursor.fetchall()
        print(f"{'First name':11} {'Last name':11} {'Tutor group':12} {'City':13} {'Year group':13}")
        for i in results:
            print(f"{i[0]:11} {i[1]:11} {i[2]:12} {i[3]:13} {i[4]:11}")
    ### Update a student ###
    elif selection == 4:
        print("\nUpdate a student")
        print("\nSearch for a student")
        name = input("Name: ").strip()
        like_name = f"%{name}%"
        cursor.execute("SELECT studentID, firstName, lastName FROM student WHERE firstName LIKE ? or lastName LIKE ?", (like_name, like_name,))
        results = cursor.fetchall()
        if len(results) == 0:
            print("No results found")
        else:
            print("{'StudentID':10} {'First Name':10} {'Last Name':10}")
            ids = []
            for student in results:
                print(f"{student[0]:10} {student[1]:10}")
                ids.append(student[0])
            studentID = int(input("Enter ID: "))
            new_tutor = input("New tutor code: ")
            cursor.execute("UPDATE student SET tutorGroup = ? WHERE studentID = ?", (new_tutor, studentID))
            connection.commit()
            
    ### Quit program ###
    else:
        run_program = False
