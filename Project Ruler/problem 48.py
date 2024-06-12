x = 1
num = 0
for i in range(1000):
    num += x**x
    x += 1
tot = str(num)
print(tot[-10:])
