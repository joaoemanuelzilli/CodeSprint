a = int(input())
list = []

for i in range(a):
    b = int(input())
    list.append(b)


maior = max(list, key=int)
if (maior) == list[0]:
    print("S")
else: print("N")

