def resolver():
    T = int(input())

    for i in range(1, T):
        N, P = map(int, input().split())
        renas = []

        for _ in range(N):
            dados = input().split()
            nome = dados[0]
            peso = dados[1]
            idade = dados[2]
            altura = dados[3]

            renas.append((nome, peso, idade, altura))

        renas_ordenadas = sorted(renas, key=lambda r:(r[3], r[2], r[1], r[0]))

        print(f"Caso {T}")

        for i in range(P):
            print(renas_ordenadas[i][0])

if __name__ == "__main__":
    resolver()