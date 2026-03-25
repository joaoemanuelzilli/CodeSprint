resultados = []  
while True:
    num = int(input())
    if num == 0:
        break 

    primeiro_planeta = ""
    menor_ano_envio = float('inf')  
    for _ in range(num):
        entrada = input().split()
        planeta = entrada[0]
        ano_recebido = int(entrada[1])
        tempo_viagem = int(entrada[2])

        ano_envio = ano_recebido - tempo_viagem  

        if ano_envio < menor_ano_envio:
            menor_ano_envio = ano_envio
            primeiro_planeta = planeta  

    resultados.append(primeiro_planeta)  

for resultado in resultados:
    print(resultado)
