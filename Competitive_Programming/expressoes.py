def verifica_cadeia_bem_definida(cadeia):
    pilha = []
    pares = {'(': ')', '[': ']', '{': '}'}

    for caractere in cadeia:
        if caractere in pares:  
            pilha.append(caractere)
        elif caractere in pares.values():  
            if pilha and pares[pilha[-1]] == caractere:
                pilha.pop()  
            else:
                return 'N' 

    return 'S' if not pilha else 'N'  


n = int(input()) 

for _ in range(n):
    cadeia = input().strip()  
    resultado = verifica_cadeia_bem_definida(cadeia)
    print(resultado)
