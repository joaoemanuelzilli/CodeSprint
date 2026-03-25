num = int(input())
list = []

for i in range(num):
    aux = input().split()
    N = int(aux[0])
    K = int(aux[1])

    cheias = N // K
    vazias = N % K

    t = vazias + cheias
    list.append(t)

for i in list:
    print(i)
