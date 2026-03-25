import itertools

def soma_permut(arr):
    max_soma = 0
    for perm in itertools.permutations(arr):
        for i in range(len(perm) - 1):
            soma = sum(abs(perm[i] - perm[i + 1]) )
        max_soma = max(max_soma, soma)
    return max_soma

def main():
    t = int(input())
    for case_num in range(1, t + 1):
        i = list(map(int, input().split()))
        n = i[0]
        arr = i[1:]
        result = soma_permut(arr)
        print(f"Caso #{case_num}: {result}")

if __name__ == "__main__":
    main()
