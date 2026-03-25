p = int(input())
original = list(range(1, p + 1))
current = original[:]
count = 0

while True:
    count += 1
    shuffled = []
    n = p // 2
    for i in range(n):
        shuffled.append(current[n + i])
        shuffled.append(current[i])
    if shuffled == original:
        print(count)
        break
    current = shuffled
