###This code is connected to a database formatting different information about the Premier League###

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Setting Connection~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
import sqlite3

DATABASE = "../DB Browser/PL.db"
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
ask = True

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Start of Program~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
print("Welcome to the Premier League football clubs program")
#Loop of Menu#
while ask == True:
    #Menu#
    print("\nFootball Clubs Menu")
    print("===================")
    print("1. See all statistics")
    print("2. See the top 5 oldest/youngest teams")
    print("3. See the top 5 teams which retained most/least possesion")
    print("4. See the top 5 teams scored the most/least goals")
    print("5. See teams which outperformed/underperformed their expected goals")
    print("6. Quit program")
    check = True
    #Selection#
    select = input("Selection: ").strip()
    #Errorcatching#
    while check == True:
        #Testing Integer or String
        try:
            select = int(select)
            #Testing Boundaries
            if select > 7 or select < 1:
                print("Unvalid selection. Please enter a number from 1-6")
                select = input()
            else:
                #End loop
                check = False
        except ValueError:
            print("Unvalid selection. Please enter a number from 1-6")
            select = input()
            
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~First Selection~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    if select == 1:
        print("\nAll statistics")
        print("==============")
        cursor.execute("SELECT * FROM Football")
        results = cursor.fetchall()
        
        print(f"{'Team':15} {'Average Age':^12} {'Possession':10} {'Goals':^6} {'Assists':^8} {'Expected Goals':14}")
        for i in results:
            xg = round(float(i[5]), 1)
            age = round(float(i[1]), 1)
            print(f"{i[0]:15} {age:^12} {i[2]:^10} {i[3]:^6} {i[4]:^8} {xg:^14}")
            
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Second Selection~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    elif select == 2:
        check = True
        print("\nTop 5 Oldest/Youngest Teams")
        print("===========================")
        #Selection#
        pick = input("Oldest or Youngest (O or Y): ").strip().lower()
        #Errorcatching#
        while check == True:
            #Check whether unvalid selection
            if pick != "oldest" and pick != "youngest" and pick != "o" and pick != "y":
                print("Unvalid selection. Please enter 'oldest' or 'youngest' or 'o' or 'y'")
                pick = input().strip().lower()
            else:
                #End loop
                check = False
                
        #If oldest is selected
        if pick == "oldest" or pick == "o":
            cursor.execute("SELECT * FROM Football ORDER BY average_age DESC LIMIT 5")
        #If youngest is selected
        else:
            cursor.execute("SELECT * FROM Football ORDER BY average_age LIMIT 5")
        results = cursor.fetchall()
        
        print(f"{'Team':15} {'Average Age':^12} {'Possession':10} {'Goals':^6} {'Assists':^8} {'Expected Goals':14}")
        for i in results:
            xg = round(float(i[5]), 1)
            age = round(float(i[1]), 1)
            print(f"{i[0]:15} {age:^12} {i[2]:^10} {i[3]:^6} {i[4]:^8} {xg:^14}")

        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Third Selection~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    elif select == 3:
        check = True
        print("\nTop 5 teams retaining most/least possession")
        print("===========================================")
        #Selection#
        pick = input("Most or Least (M or L): ").strip().lower()
        #Errorcatching#
        while check == True:
            #Check whether unvalid selection
            if pick != "most" and pick != "least" and pick != "m" and pick != "l":
                print("Unvalid selection. Please enter 'most' or 'least' or 'm' or 'l'")
                pick = input().strip().lower()
            else:
                #End loop
                check = False

        #If most is selected
        if pick == "most" or "m":
            cursor.execute("SELECT * FROM Football ORDER BY possession DESC LIMIT 5")
        #If least is selected
        else:
            cursor.execute("SELECT * FROM Football ORDER BY possession LIMIT 5")
        results = cursor.fetchall()
        
        print(f"{'Team':15} {'Average Age':^12} {'Possession':10} {'Goals':^6} {'Assists':^8} {'Expected Goals':14}")
        for i in results:
            xg = round(float(i[5]), 1)
            age = round(float(i[1]), 1)
            print(f"{i[0]:15} {age:^12} {i[2]:^10} {i[3]:^6} {i[4]:^8} {xg:^14}")

        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Fourth Selection~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    elif select == 4:
        check = True
        print("\nTop 5 teams scoring the most/least goals")
        print("========================================")
        #Selection#
        pick = input("Most or Least (M or L): ").strip().lower()
        #Errorcatching#
        while check == True:
            #Check whether unvalid selection
            if pick != "most" and pick != "least" and pick != "m" and pick != "l":
                print("Unvalid selection. Please enter 'most' or 'least' or 'm' or 'l'")
                pick = input().strip().lower()
            else:
                #End loop
                check = False

        #If most is selected
        if pick == "most" or pick == "m":
            cursor.execute("SELECT * FROM Football ORDER BY goals DESC LIMIT 5")
        #If least is selected
        else:
            cursor.execute("SELECT * FROM Football ORDER BY goals LIMIT 5")
        results = cursor.fetchall()
        
        print(f"{'Team':15} {'Average Age':^12} {'Possession':10} {'Goals':^6} {'Assists':^8} {'Expected Goals':14}")
        for i in results:
            xg = round(float(i[5]), 1)
            age = round(float(i[1]), 1)
            print(f"{i[0]:15} {age:^12} {i[2]:^10} {i[3]:^6} {i[4]:^8} {xg:^14}")

        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Fifth Selection~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    elif select == 5:
        check = True
        print("\nTeams which outperformed/underperformed expected goals")
        print("======================================================")
        #Selection#
        pick = input("Outperformed or Underperformed (O or U): ").strip().lower()
        #Errorcatching#
        while check == True:
            #Check whether unvalid selection
            if pick != "outperformed" and pick != "underperformed" and pick != "o" and pick != "u":
                print("Unvalid selection. Please enter 'outperformed' or 'underperformed' or 'o' or 'u'")
                pick = input().strip().lower()
            else:
                #End loop
                check = False
        
        cursor.execute("SELECT * FROM Football")
        results = cursor.fetchall()
        
        print(f"{'Team':15} {'Average Age':^12} {'Possession':10} {'Goals':^6} {'Assists':^8} {'Expected Goals':14}")
        #If outperformed is selected
        if pick == "outperformed" or pick == "o":
            for i in results:
                if i[3] > i[5]:
                    xg = round(float(i[5]), 1)
                    age = round(float(i[1]), 1)
                    print(f"{i[0]:15} {age:^12} {i[2]:^10} {i[3]:^6} {i[4]:^8} {xg:^14}")
        #If underperformed is selected
        else:
            for i in results:
                if i[3] < i[5]:
                    xg = round(float(i[5]), 1)
                    age = round(float(i[1]), 1)
                    print(f"{i[0]:15} {age:^12} {i[2]:^10} {i[3]:^6} {i[4]:^8} {xg:^14}")
                    
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Sixth Selection~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    else:
        print("Goodbye!")
        ask = False
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~End of Program~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
