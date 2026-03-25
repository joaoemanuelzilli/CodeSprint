a = int(input())
list = []

def c(frase):
    if frase == " ":
        return " "
    else:
        palavras = frase.replace("·", " ").split()
        result = ''.join(palavra[0] for palavra in palavras)
        return result

for i in range(a):
    b = str(input())
    list.append(c(b))

for i in range(a):
    print(list[i])
    