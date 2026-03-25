a = int(input())
b = int(input())

list = []
listf = []

for i in range(b):
    c = int(input())
    list.append(c)

list.sort()
for i in range(len(list)):
    if i+1 <= len(list):
        if list[i] != list[i+1]:
            listf.append(list[i])
        else: continue
    else:continue

r = a - len(listf)


print(r)