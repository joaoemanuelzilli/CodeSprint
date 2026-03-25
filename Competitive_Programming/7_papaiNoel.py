list = []
qnt = int(input())
bons = 0
ruins = 0

for i in range(qnt):
    nome = str(input())
    if nome[0] == '+':
        bons += 1
    else: ruins += 1
    nome = nome.strip('+- ')
    list.append(nome)

list.sort()
for i in list:
    print(i)

print(f"Se comportaram: {bons} | Nao se comportaram: {ruins}")

