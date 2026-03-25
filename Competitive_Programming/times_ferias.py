l = []
l1 = []
soma = 0

while True:
    a = int(input())
    if a == 0: break
    for i in range(a):
        b, c = input().split()
        l.append(b)
        c = int(c)
        l1.append(c)
    for i in l1:
        soma += i
    c = soma % a
    