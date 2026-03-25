resultados = []

while True:
    D, N = input().split()
    
    D = str(D)
    
    if D == "0" and N == "0":
        break

    resultado = N.replace(D, "")
    
    if resultado == "":
        resultado = "0"
    
    resultado = str(int(resultado))
    
    resultados.append(resultado)

for res in resultados:
    print(res)
