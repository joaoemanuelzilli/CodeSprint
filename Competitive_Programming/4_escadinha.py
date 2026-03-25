def count(sequence):
    num = len(sequence)
    if num <= 2:
        return 1

    count = 0
    i = 0

    while i < num - 1:
        j = i
        diff = sequence[j + 1] - sequence[j]
        while j < num - 1 and sequence[j + 1] - sequence[j] == diff:
            j += 1
        count += 1
        i = j
    return count

N = int(input())
sequence = list(map(int, input().split()))
print(count(sequence))
