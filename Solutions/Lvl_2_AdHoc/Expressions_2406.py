'''

link: https://judge.beecrowd.com/en/problems/view/2406

Expressions
By OBI - Brazilian Informatics Olympiad 2011, Brazil

Time Limit: 1 second

Pedrinho and Zezinho need to study the evaluation of mathematical expressions for an upcoming test. To prepare, 
they want to solve many practice problems before the test. Since they know how to program, they decided to create a mathematical expression generator.

Their expression generator works in two phases. In the first phase, a string is generated containing only the 
characters '{', '[', '(', '}', ']', and ')'. In the second phase, the generator adds numbers and operators to the 
structure created in the first phase. A string is considered well-formed (or valid) if it satisfies the following properties:

It is an empty string (contains no characters).
It consists of a well-formed string enclosed in parentheses, square brackets, or curly braces. Thus, if the string 
S is well-formed, then the strings (S), [S], and {S} are also well-formed.
It is formed by the concatenation of two well-formed strings. Therefore, if the strings X and Y are well-formed, 
the string XY is also well-formed.
After generating several mathematical expressions, Pedrinho and Zezinho noticed that there was an error in the first 
phase of the generator. Some strings were not well-formed. They want to start solving the expressions as soon as possible 
and, knowing that you are an excellent programmer (and participate in the OBI), they asked you to write a program that, 
given several strings generated in the first phase, determines which ones are well-formed and which are not.

Input
The input consists of multiple test cases. The first line contains an integer T (1 ≤ T ≤ 20), indicating the number of 
test cases. The following T lines each contain a string A (the string A has between 1 and 100,000 characters, and contains 
only the characters '{', '[', '(', '}', ']', and ')').

Output
For each test case, print a single line containing the letter 'S' if the string is well-formed, or the letter 'N' otherwise.

'''

def verifica_cadeia_bem_definida(cadeia):
    pilha = []
    pares = {'(': ')', '[': ']', '{': '}'}

    for caractere in cadeia:
        if caractere in pares:  
            pilha.append(caractere)
        elif caractere in pares.values():  
            if pilha and pares[pilha[-1]] == caractere:
                pilha.pop()  
            else:
                return 'N' 

    return 'S' if not pilha else 'N'  


n = int(input()) 

for _ in range(n):
    cadeia = input().strip()  
    resultado = verifica_cadeia_bem_definida(cadeia)
    print(resultado)
