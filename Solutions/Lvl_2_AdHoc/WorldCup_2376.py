'''

link: https://judge.beecrowd.com/en/problems/view/2376

World Cup
By OBI - Brazilian Informatics Olympiad 2010, Brazil

Time Limit: 1 second

This year is a World Cup year! The entire country is gearing up to cheer for the "canarinho" team to win another title, becoming the six-time champion.

In the World Cup, after a group stage, sixteen teams compete in the knockout stage, which consists of fifteen elimination matches. The figure below shows the knockout stage match schedule:

In the match schedule, the sixteen finalist teams are represented by uppercase letters (from A to P), and the matches are numbered from 1 to 15. For example, match 3 is between the teams identified by E and F; the winner of this match will face the winner of match 4, and the loser will be eliminated. The team that wins all four matches in the knockout stage will be the champion (for example, for team K to become champion, it must win matches 6, 11, 14, and 15).

Given the results of the fifteen knockout stage matches, write a program to determine the champion team.

Input
The input consists of fifteen lines, each containing the result of a match. The first line contains the result of match number 1, the second line the result of match number 2, and so on. The result of a match is represented by two integers, M and N, separated by a single space, indicating the number of goals scored by the team on the left and the team on the right in the match schedule, respectively (0 ≤ M ≤ 20, 0 ≤ N ≤ 20, and M ≠ N).

Output
Your program must print a single line containing the letter identifying the champion team.

'''

equipes = [chr(i) for i in range(ord('A'), ord('P')+1)]

vencedores = []

index = 0

for i in range(15):
    M, N = map(int, input().split())
    
    if M > N:
        vencedores.append(equipes[index])
    else:
        vencedores.append(equipes[index + 1])
    
    index += 2
    
    if len(vencedores) == len(equipes) // 2:
        equipes = vencedores
        vencedores = []
        index = 0

print(equipes[0])
