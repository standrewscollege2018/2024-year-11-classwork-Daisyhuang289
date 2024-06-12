x = 1
num = 0
check = True
while check == True:
    num += x
    x += 1
    count = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
        i += 1
    if count > 500:
        check = False

print(num)
