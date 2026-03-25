list = input().split(' ')
list1 = []

for i in list:
    list1.append(int(i))

c = 0

for i in list1: 
    if i == 9:
        c += 1

if c == 0: print('S') 
else: print('F')

