x = 1
y = 1
num = 0
count = 2

while len(str(num)) < 1000:
    count += 1
    num = x + y
    x, y = y, num

print(count)
