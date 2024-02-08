''' This program takes a number as input and doubles it '''

keepasking = True
while keepasking:
    # Take number input as a float and then print double the number
    try:
        num = float(input())
        print(num*2)
        keepasking = False
    except ValueError:
        print("Please enter a number")
