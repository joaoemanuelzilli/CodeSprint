'''

link: https://judge.beecrowd.com/en/problems/view/2453

P Language
By OBI - Brazilian Informatics Olympiad 2014, Brazil

Time Limit: 1 second

A game that children love is communicating in the P language, adding "pê" before each syllable as a form of code to make it harder 
for others to understand the conversation (pê-va pê-mos pê-no pê-ci pê-ne pê-ma?).

Jacy and Kátia adapted the P language for electronic messages by adding a lowercase 'p' before each letter in the words of a message. 
An example of an encoded message and its corresponding decoded message is shown in the figure below.

Your task is to write a program that decodes a message written in Jacy and Kátia’s electronic P language.

Input
The input consists of a single line containing a message written in Jacy and Kátia’s electronic P language. The message contains only 
uppercase and lowercase letters and spaces. The message has between 1 and 1000 characters, and there are no consecutive spaces in the message.

Output
Your program must produce a single line containing the decoded message.

'''

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
