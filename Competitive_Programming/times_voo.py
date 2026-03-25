oeste1 = []
norte1 = []
sul1 = []
leste1 = []
list=[]
oeste = False
sul = False
leste = False
norte = False
list_final = []
list_p = []

while True:
    entrada = input()
    if entrada == '0': break
    if entrada in ['-1', '-2', '-3', '-4']:
        entrada = int(entrada)
        if entrada == -1:
            oeste = True
            norte = False
            sul = False
            leste = False
        elif entrada == -2:
            norte = False
            oeste = False
            sul = True
            leste = False
        elif entrada == -3:
            norte = True
            oeste = False
            sul = False
            leste = False
        elif entrada == -4:
            leste = True
            oeste = False
            norte = False
            sul = False

    else:
        if oeste:
            oeste1.append(entrada)
        elif sul:
            sul1.append(entrada)
        elif leste:
            leste1.append(entrada)
        elif norte:
            norte1.append(entrada)

listas = [oeste1, norte1, sul1, leste1]
max_length = max(len(lista) for lista in listas)

for i in range(max_length):
    for lista in listas:
        if i < len(lista): 
            list_final.append(lista[i])

print(" ".join(list_final))
