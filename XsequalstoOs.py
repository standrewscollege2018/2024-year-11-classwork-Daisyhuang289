word = input("String: ")
x = 0
o = 0
lst = []
for letter in word:
    lst.append(letter)
for letter in lst:
    if letter == "X":
        x += 1
    if letter == "O":
        o += 1
if x == o:
    print("True")
else:
    print("False")
