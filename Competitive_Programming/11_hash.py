def processar_entrada():
    N = int(input())
    
    resultados = []
    
    for _ in range(N):
        L = int(input())
        caso = [input().strip() for _ in range(L)]
        
        valor_hash = 0
        for i, linha in enumerate(caso):
            for j, letra in enumerate(linha):
                valor_hash += (ord(letra) - ord('A')) + i + j
        
        resultados.append(valor_hash)
    
    for resultado in resultados:
        print(resultado)

# processar_entrada()
