
def contar_diamantes(frase):
    pilha = []
    diamantes = 0
    
    for caractere in frase:
        if caractere == '<':
            pilha.append(caractere)
        elif caractere == '>' and pilha:
            pilha.pop() 
            diamantes += 1  
    
    return diamantes

n = int(input())

for _ in range(n):
    linha = input().strip()  
    resultado = contar_diamantes(linha)  
    print(resultado)  
