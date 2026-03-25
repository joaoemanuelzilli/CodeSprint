a = int(input())
l = []
l2 = []
l3 = []
l4 = []
c = 0
for i in range(1, 1+a):
    l.append(i)

n = 2
aux = l
while True:
    c += 1
    l2 = aux[:n]
    l3 = aux[n:]
    for i in range(max(len(l2), len(l3))):
        if i < len(l3):
            l4.append(l3[i])
        if i < len(l2):
            l4.append(l2[i])
    if l4 == l:
        print(c)
        break
    else:
        l2 = []
        l3 = []
        aux = l4
        l4 = []