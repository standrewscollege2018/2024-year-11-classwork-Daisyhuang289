people = []
get_details = True
while get_details:
    person = []
    name = input()
    if name.strip(" ") == "":
        print("Enter a valid name")
    elif name.lower() == "stop":
        get_details = False
    else:
        person.append(name)
        try:
            age = int(input())

            person.append(age)
            people.append(person)
        except ValueError:
            print("Enter a valid age")
x= 0
for i in people:
    x += 1
    print(f"{x}. {i[0]} {i[1]}")
