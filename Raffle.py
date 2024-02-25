from random import randint
print("Welcome to the raffle program")
prize = input("What is the prize being raffled? ")
value = int(input("What is the value of the {prize} (do not enter the $ sign) "))
lst = []
ask = False
while ask == False:
    name = input("Enter name of entrant: ")
    if name.strip() == "":
        print("Enter a existing name")
    elif name.lower() == "end":
        ask = True
    else:
        lst.append(name)
num = randint(0, len(lst)-1)
if len(lst) == 1:
    print(f"There is 1 person in the draw for the {prize}")
elif len(lst) > 1:
    print(f"There are {len(lst)} people in the draw for the {prize}")
print(f"And the winner of the {prize}, valued at ${value} is... {lst[num]}!")
