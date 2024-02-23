from random import randint
print("Hello,")
lst = []
ask = False
while ask == False:
    name = input("Please enter a name: ")
    if name.strip() == "":
        print("Enter a existing name")
    elif name.lower() == "stop":
        ask = True
    else:
        lst.append(name)
prize = input("Enter the prize: ")
value = randint(0, len(lst)-1)
print(f"{lst[value]} has won the raffle of {prize}")
