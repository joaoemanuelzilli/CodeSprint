equipes = [chr(i) for i in range(ord('A'), ord('P')+1)]

vencedores = []

index = 0

for i in range(15):
    M, N = map(int, input().split())
    
    if M > N:
        vencedores.append(equipes[index])
    else:
        vencedores.append(equipes[index + 1])
    
    index += 2
    
    if len(vencedores) == len(equipes) // 2:
        equipes = vencedores
        vencedores = []
        index = 0

print(equipes[0])
