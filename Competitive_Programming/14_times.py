qntAlunos, qntTimes = map(int, input().split())

alunos = []

for i in range(qntAlunos):
    nome, habilidade = input().split()
    habilidade = int(habilidade)
    alunos.append((habilidade, nome))

alunos.sort(reverse=True)

times = [[] for i in range(qntTimes)]

for i in range(qntAlunos):
    times[i % qntTimes].append(alunos[i][1])

for i in range(qntTimes):
    print(f"Time {i + 1}")
    for jogador in sorted(times[i]):
        print(jogador)
    print() 
