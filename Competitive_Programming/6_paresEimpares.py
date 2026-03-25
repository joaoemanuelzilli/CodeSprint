n = int(input())
listP = []
listI = []

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        listP.append(num)
    else:
        listI.append(num)

listP.sort()
listI.sort(reverse=True)

for i in listP:
    print(i)
for i in listI:
    print(i)