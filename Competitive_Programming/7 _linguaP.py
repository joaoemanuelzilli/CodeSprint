def decodificar_mensagem(mensagem):
    decodificada = []
    i = 0
    while i < len(mensagem):
        if mensagem[i] == 'p' and i + 1 < len(mensagem):
            decodificada.append(mensagem[i + 1])
            i += 2
        else:
            decodificada.append(mensagem[i])
            i += 1
    return ''.join(decodificada)

entrada = input()

saida = decodificar_mensagem(entrada)

print(saida)
