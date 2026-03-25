def fib(n):
    valores = [0, 1]
    if n > 1:
        for i in range(2, n + 1):
            f = valores[i - 1] + valores[i - 2]
            valores.append(f)
    return valores[n]

teste = int(input())

for teste in range(teste):
    n = int(input())
    f = fib(n)
    print('Fib({}) = {}'.format(n, f))