oeste1, norte1, sul1, leste1 = [], [], [], []
listas = [oeste1, norte1, sul1, leste1]
direcoes = {'-1': oeste1, '-2': sul1, '-3': norte1, '-4': leste1}
direcao_atual = None

while True:
    entrada = input()
    if entrada == '0': break
    if entrada in direcoes:
        direcao_atual = direcoes[entrada]
    elif direcao_atual is not None:
        direcao_atual.append(entrada)

list_final = []
for i in range(max(len(oeste1), len(norte1), len(sul1), len(leste1))):
    if i < len(oeste1): list_final.append(oeste1[i])
    if i < len(norte1): list_final.append(norte1[i])
    if i < len(sul1): list_final.append(sul1[i])
    if i < len(leste1): list_final.append(leste1[i])

print(" ".join(list_final))
