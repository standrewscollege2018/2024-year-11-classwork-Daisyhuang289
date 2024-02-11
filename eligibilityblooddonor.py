age = int(input("Enter your age: "))
try:
    age = int(input("Enter your age: "))
    weight = int(input("Enter your weight: "))
    if age < 0 or weight < 0:
        print("Enter a proper weight/age")
    else:
        if age >= 16 and weight >= 50:
            print("You are eligible")
        else:
            print("You are not eligible")
except ValueError:
    print("Enter a number")
