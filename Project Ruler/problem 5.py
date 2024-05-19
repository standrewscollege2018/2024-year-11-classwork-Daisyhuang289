num = 0
ask = True
while ask == True:
    num += 1
    divis = 0
    for i in range(1, 21):
        if num%i == 0:
            divis += 1
    if divis == 20:
        print(num)
        ask = False
