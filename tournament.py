print("Welcome to the Super Tournament Points Calculation system")
ask = False
dic = {}
dic[team] = 0
lst = []
#Checking input for name of the team
check = False
while check = False:
    team = input("Enter the name of the team: ")
    if team.strip() == "":
        print("Enter a valid team")
    else:
        check = True
#Checking input for the name of the opponent in a loop till end is entered
while ask == False:
    opponent = input("Enter the name of the opponent: ")
    if opponent.lower() == "done":
        ask = True
    elif team.strip() == "":
        print("Enter a valid team name")
    else:
        lst.append(team)
#Entering scores, calculating the winner/loser and if it is a draw
for i in lst:
    print(f"Game versus {i}")
    checking = False
    while checking == False:
        try:
            score1 = int(input(f"{team} score: "))
            checking = True
        except ValueError:
            print("Enter a integer")
    while checking == True:
        try:
            score2 = int(input(f"{i} score: "))
            checking = False
        except ValueError:
            print("Enter a integer")
    if score1 > score2:
        print("You won")
        dic[team] += 3
    elif score1 == score2:
        print("You drew")
        dic[team] += 2
    elif score1 < score2:
        print("You lost")
        dic[team] += 1
#Printing the end result
print("Competition complete!")
print(f"{team} finished the competition with {dic[team]} points.")

