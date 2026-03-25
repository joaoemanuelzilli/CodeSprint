# (a+b*(2-c)-2+a)*2  está correto

# enquanto

# (a*b-(2+c)         está incorreto

#t = str(input())
#cont = 0
#tam = len(t)
#for i in range(tam):
   # if t[i] == "(":
   #     cont +=1
  #  elif t[i] == ")":
 #       cont -=1
#    else: continue

#if t[0] == ")":
#   print('incorrect')
#elif cont == 0:
#    print('correct')
#else: print('incorrect')


import sys

def verifica_parenteses(expressao):
    cont = 0
    for char in expressao:
        if char == "(":
            cont += 1
        elif char == ")":
            cont -= 1
        if cont < 0:
            return "incorrect"
    if cont == 0:
        return "correct"
    else:
        return "incorrect"

for linha in sys.stdin:
    expressao = linha.strip()
    if expressao:
        print(verifica_parenteses(expressao))


