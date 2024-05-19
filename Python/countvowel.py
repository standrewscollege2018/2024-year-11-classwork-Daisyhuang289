word = input("Word: ")
x = 0
lst = []
for letter in word:
    lst.append(letter)
if " " in lst:
    print("Only enter a single word")
else:
    for letter in lst:
        if letter == "a":
            x += 1
        if letter == "e":
            x += 1
        if letter == "i":
            x += 1
        if letter == "o":
            x += 1
        if letter == "u":
            x += 1
    print(x)
