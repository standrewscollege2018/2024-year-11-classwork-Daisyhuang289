lst = []
name = input()
y = name.lower()
while y != "stop":
    if name == "":
        print("Enter a valid name")
        name = input()
        y = name.lower()
    else:
        lst.append(name)
        name = input()
        y = name.lower()
x= 0
for i in lst:
    x += 1
    print(f"{x}. {i}")
