x  = input()
lista = []
listaf = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000]
while x != 0:
    lista.append(listaf[len(x)-1])
    x = input()
    if x.isnumeric():
        x = int(x)

for i in lista:
    print(i)
    