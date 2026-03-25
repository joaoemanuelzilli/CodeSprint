n1, n2 = input().split( )
n1 = int(n1)
n2 = int(n2)
lista = []

for i in range(n2):
    lista.append(input())

for i in lista:
    if i == 'fechou':
        n1 += 1
    else:
        n1 -= 1

print(n1)