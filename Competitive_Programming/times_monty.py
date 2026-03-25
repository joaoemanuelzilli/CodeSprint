num = int(input())
b = 0

for i in range(num):
    a = int(input())
    if a == 1:
        continue
    else: b += 1

print(b)