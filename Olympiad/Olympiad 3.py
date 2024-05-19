struts=0
platforms=0
stories = int(input())
for i in range(stories+1):
    x = i*2
    struts += x
for i in range(stories):
    platforms += i
print(platforms+struts)
