x = 100
dig = 1
num = 0
while x != 0:
    dig = dig * x
    x -=1
for i in str(dig):
    num += int(i)
print(num)
    
