from random import randint
print("Hello,")
lst = []
ask = False
while ask == False:
    name = input("Please enter a name: ")
    if name.strip() == "":
        print("Enter a existing name")
    elif name.lower() == "end":
        ask = True
    else:
        lst.append(name)
while ask == True:
    try:
        prize = int(input("Enter the prize: "))
        ask = False
    except ValueError:
        print("Enter a money value")
value = randint(0, len(lst)-1)
if len(lst) == 1:
    print(f"1 person has entered this raffle")
elif len(lst) > 1:
    print(f"{len(lst)} people has entered this raffle")
print(f"The prize is ${prize}")
print(f"{lst[value]} has won the raffle of ${prize}")
