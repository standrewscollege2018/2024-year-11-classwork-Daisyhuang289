function = input("What function would you like to apply? Plus, subtract, multiply, and divide. All lower case! ")
x = int(input("Enter your first value: "))
y = int(input("Enter your second value: "))
if function == "plus":
    z = x + y
elif function == "subtract":
    z = x - y
elif function == "divide":
    z = x/y
elif function == "multiply":
    z = x * y
else:
    print("This function is unavailable")
    z = "NOTHING"
print(z)
