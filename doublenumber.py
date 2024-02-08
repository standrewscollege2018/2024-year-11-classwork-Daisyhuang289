''' This program takes a number as input and doubles it '''

keepasking = True
while keepasking:
    # Take number input as a float and then print double the number
    try:
        num = float(input())
        keepasking = False
    except ValueError:
        print("Please enter a number")
print(f"{num} doubled is {num * 2}")
