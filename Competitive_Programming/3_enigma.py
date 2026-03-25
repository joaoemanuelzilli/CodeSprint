def posicoes_possiveis(msn_cifrada, crib):
    len_msn = len(msn_cifrada)
    len_crib = len(crib)

    count = 0
    for x in range(len_msn - len_crib + 1):
        posicao_valida = True
        for y in range(len_crib):
            if msn_cifrada[x + y] == crib[y]:
                posicao_valida = False
                break
        if posicao_valida:
            count += 1
    return count

msn_cifrada = input().strip()
crib = input().strip()
qnt_posicoes_possiveis = posicoes_possiveis(msn_cifrada, crib)

print(qnt_posicoes_possiveis)
