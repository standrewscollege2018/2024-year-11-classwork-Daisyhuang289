print("Hello, ")
ask = False
dic = {}
lst = []
while ask == False:
    team = input("Enter the team name: ")
    if team.lower() == "done":
        ask = True
    elif team.strip() == "":
        print("Enter a valid name")
    else:
        lst.append(team)
for i in lst:
    score = input(f"Enter {i} result: ")
    if i in dic:
        if score == "win":
            dic[i] += 3
        elif score == "lose":
            dic[i] += 1
        elif score == "tie":
            dic[i] += 2
    elif i not in dic:
        if score == "win":
            dic[i] = 3
        elif score == "lose":
            dic[i] = 1
        elif score == "tie":
            dic[i] = 2
for i in dic:
    print(f"{i} score {dic[i]} competition points")
