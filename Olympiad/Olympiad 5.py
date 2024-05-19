preference = {"g":0, "c":0, "e":0, "p":0, "l":0, "s":0}
tea = ["g", "c", "e", "p", "l", "s"]
personal = {}
all_host = []

people = input().split()
for i in range(int(people[0])):
    name = input().split()
    preference[name[1].lower()] += 1

for i in range(int(people[0])):
    stock = input().split()
    personal[stock[0]] = [int(stock[1]), int(stock[2]), int(stock[3]), int(stock[4]), int(stock[5]), int(stock[6])]

for i in range(int(people[1])):
    host = input()
    all_host.append(host)

for host in all_host:
    x = 0
    num = 0
    for version in tea:
        if int(personal[host][num]) < int(preference[version]):
            difference = int(preference[version]) - int(personal[host][num])
            x += difference
        num += 1
    if x == 0:
        print(f"{host} Successful")
    elif x == 1 or x == 2:
        print(f"{host} Mildly Successful ({x})")
    elif x > 2:
        print(f"{host} Disaster ({x})")
