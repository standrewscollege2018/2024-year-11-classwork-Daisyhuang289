count = 0
num = 1
while count < 10001:
    x = 0
    num += 1
    for i in range(1, num):
        if num%i == 0:
            x += 1
    if x == 1:
        count += 1
print(num)
