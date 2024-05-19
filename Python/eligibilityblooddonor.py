def check(a):
    try:
        b = float(a)
        if b < 0:
            return "negative"
        else:
            return True
    except ValueError:
        return False
age = input("Enter your age: ")
if check(age) == False:
    print("Please enter a number")
elif check(age) == "negative":
    print("Please enter positive number")
else:
    weight = input("Enter your weight: ")
    if check(weight) == False:
        print("Please enter a number")
    elif check(weight) == "negative":
        print("Please enter positive number")
    else:
        x = float(weight)
        y = float(age)
        if x >= 50 and y >= 16:
            print("You are eligible")
        else:
            print("You are not eligible")
 
