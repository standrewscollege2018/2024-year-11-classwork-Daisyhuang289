spots = []
canva = input().split()
for i in range(int(canva[0])+1):
    lst = []
    for j in range(int(canva[1])+1):
        lst.append("n")
    spots.append(lst)

for i in range(int(canva[2])):
    colour = input().split()
    x = int(colour[0])
    y = int(canva[0]) - int(colour[1])  
    if spots[y][x] == "n":
        spots[y][x] = colour[3]
    if int(colour[2]) != 0:
        for j in range(1, int(colour[2])+1):
            for dx in range(-j, j+1):
                for dy in range(-j, j+1):
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x <= int(canva[1]) and 0 <= new_y <= int(canva[0]) and spots[new_y][new_x] == "n":
                        spots[new_y][new_x] = colour[3]

final = input().strip()
count = 0
for i in spots:
    count += i.count(final)
print(count)
