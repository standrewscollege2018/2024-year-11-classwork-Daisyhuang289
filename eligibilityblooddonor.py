age = int(input("Enter your age: "))
while age:
    try:
        age1 = int(age)
        weight = int(input("Enter your weight: "))
        if age1 < 0 or weight < 0:
            print("Enter a proper weight/age")
        else:
            if age1 >= 16 and weight >= 50:
                print("You are eligible")
            else:
                print("You are not eligible")
    except ValueError:
        print("Enter a number")
    age = input("Enter your age: ")
