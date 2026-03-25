N = int(input())
s = input().strip()

count_a_in_maximal = 0
i = 0

while i < N:
    if s[i] == 'a':
        j = i
        while j < N and s[j] == 'a':
            j += 1
        
        if j - i >= 2:
            count_a_in_maximal += j - i
        
        i = j
    else:
        i += 1

print(count_a_in_maximal)
