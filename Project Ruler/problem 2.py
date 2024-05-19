y = 2
x = 1
tot = 2
ask = True
while ask == True:
    z = x+y
    if z > 4000000:
        ask = False
    else:
        if z%2 == 0:
            tot += z
            print(z)
        x = y+z
        if x > 4000000:
            ask = False
        else:
            if x%2 == 0:
                tot += x
                print(x)
            y = x+z
            if y > 4000000:
                ask = False
            else:
                if y%2 == 0:
                    tot += y
                    print(y)
print(tot)
    
