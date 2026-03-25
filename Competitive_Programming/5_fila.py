n = int(input())  
lista_pessoas_int = list(map(int, input().split()))

m = int(input())  
lista_saida_int = set(map(int, input().split()))  

lista_final = [i for i in lista_pessoas_int if i not in lista_saida_int]

print(" ".join(map(str, lista_final)))
