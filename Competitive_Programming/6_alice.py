

def verificar_transcricao(transcricao):
    x_count = transcricao.count('X')
    o_count = transcricao.count('O')
    
    if x_count < o_count or x_count > o_count + 1:
        return '?'
    
    if 'XX' in transcricao:
        return 'Alice'
    
    if x_count + o_count == 3:
        return '*'
    
    return '?'

transcricao = input()

resultado = verificar_transcricao(transcricao)
print(resultado)
