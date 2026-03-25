'''

link: https://judge.beecrowd.com/en/problems/view/3424

In this problem we will be dealing with character sequences, often called strings. A sequence is non-trivial if it contains at least two elements.

Given a sequence s, we say that a chunk si, ... ,sj is monotone if all its characters are equal, and we say that it is maximal if this chunk cannot be extended to left or right without losing the monotonicity.

Given a sequence composed only of characters “a” and “b”, determine how many characters “a” occur in non-trivial maximal monotone chunks.

Input
The input consists of two lines. The first line contains a single integer N, where 1≤  N ≤105. The second line contains a string with exactly N characters, composed only of the characters “a” and “b”.

Output
Print a single line containing an integer representing the total number of times the character “a” occurs in non-trivial maximal monotone chunks.

'''

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

#to do 3432