ask = True
teanum = {"g":0, "c":0, "e":0, "p":0, "l":0, "s":0}
types = ["g", "c", "e", "p", "l", "s"]
def check(tea):
    if tea in teanum:
        print(f"{teanum[tea]} ", end="")
while ask == True:
    tea = input()
    if tea.strip().lower() == "d":
        ask = False
    else:
        teasplit = tea.split()
        teanum[teasplit[0].lower()] += int(teasplit[1])
for item in types:
    check(item)
