num = 600851475143

prim = 2

while num > 1:
    if num % prim == 0:
        while num % prim == 0:
            num /= prim
        ans = prim
    prim += 1

print(ans)
