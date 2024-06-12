day = 365
even = [4, 6, 9, 11]
count = 0

def check():
    global count
    if day % 7 == 0:
        count += 1

for i in range(1901, 2001):
    for j in range(1, 13):
        check()
        if j == 2:
            if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                day += 29
            else:
                day += 28
        elif j in even:
            day += 30
        else:
            day += 31

print(count)
