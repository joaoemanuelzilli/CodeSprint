a = int(input())
list = input().split(' ')
list2 = []

for i in (list):
    list2.append(int(i))

soma = (sum(list2))/2

b = 0
c = 0

while b != soma:
    b += list2[c]
    c += 1



print(c)
