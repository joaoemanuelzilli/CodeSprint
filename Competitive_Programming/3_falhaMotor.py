num = int(input())
lista = list(map(int, input().split()))

resposta = 0

for ind in range(1, num):
    if lista[ind - 1] > lista[ind]:
        resposta = ind + 1
        break

print(resposta)
