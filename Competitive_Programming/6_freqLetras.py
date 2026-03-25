def letras_mais_frequentes(texto):
    frequencias = [0] * 26
    
    for char in texto:
        if char.isalpha():
            indice = ord(char.lower()) - ord('a')
            frequencias[indice] += 1
    
    maior_frequencia = max(frequencias)
    
    letras_frequentes = []
    for i in range(26):
        if frequencias[i] == maior_frequencia:
            letras_frequentes.append(chr(i + ord('a')))
    
    return ''.join(letras_frequentes)

def main():
    n = int(input())
    
    for i in range(n):
        texto = input().strip()
        print(letras_mais_frequentes(texto))

if __name__ == "__main__":
    main()
