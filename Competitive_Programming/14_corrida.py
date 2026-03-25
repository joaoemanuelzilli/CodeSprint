carros, voltas = map(int, input().split())
list = []
tempos_totais = []

for i in range(carros):
    tempos_voltas = list(map(int, input().split()))
    tempo_total = sum(tempos_voltas)
    tempos_totais.append((tempo_total, i + 1))

tempos_totais.sort()

print(tempos_totais[0][1]) 
print(tempos_totais[1][1])  
print(tempos_totais[2][1]) 