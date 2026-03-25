def calcular_idade():
    nome = input()
    data_atual = input()
    data_nascimento = input()
    
    dia_atual, mes_atual, ano_atual = map(int, data_atual.split('/'))
    dia_nasc, mes_nasc, ano_nasc = map(int, data_nascimento.split('/'))
    
    idade = ano_atual - ano_nasc
    
    if (mes_atual < mes_nasc) or (mes_atual == mes_nasc and dia_atual < dia_nasc):
        idade -= 1
    
    if (dia_atual == dia_nasc and mes_atual == mes_nasc):
        print("Feliz aniversario!")
    
    print(f"Voce tem {idade} anos {nome}.")

calcular_idade()
