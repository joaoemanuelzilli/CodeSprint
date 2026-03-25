'''

link: https://judge.beecrowd.com/en/problems/view/1980

Shuffling
By Gustavo Chermout, UNIFESO BR Brazil

Timelimit: 1
Gabriel is a student of computer science course, he always liked to logic games, an example is the rubik's cube, students are surprised to see how easy to him solve it. Gabriel decided to set up his own game involving logic, the first information he will need to mount the game is how many anagrams can be formed with a certain number of distinct characters without spaces.

As he uses much of your time for programming contest, it ends up not having time to check this, so he need your help.
Your task is, given a word with different characters and without spaces, say how many anagrams can be formed.

Input
The input consists of several test cases. Each test case will have a single line S with a maximum of 15 characters. The input ends with S = 0 and shouldn't be processed.

Output
For each test case you should print how many anagrams are possible form with the informed characters.

'''

import math

while True:
    s = input().strip()  
    
    if s == "0":  
        break
    
    num_anagramas = math.factorial(len(s))
    
    print(num_anagramas)
