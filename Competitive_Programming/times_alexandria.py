x = int(input("Digite a quantidade de entradas: "))
resultados = []

for _ in range(x):
    entrada = input("Digite a entrada: ")
    n1 = int(entrada[0])  
    n2 = len(entrada) - 1  
    j = 1
    
    while n1 - (n2 * j) >= 1 and j < 10:  
        n1 = n1 * (n1 - (n2 * j))
        j += 1
    
    resultados.append(n1)

for resultado in resultados:
    print(resultado)
