no = input("Credit card number: ")
lst = []
for number in no:
    lst.append(number)
length = int(len(lst))
x = length-4
print("*"*x + lst[-4] + lst[-3] + lst[-2] + lst[-1])
    
