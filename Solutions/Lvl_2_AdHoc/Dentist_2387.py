'''

link: https://judge.beecrowd.com/en/problems/view/2387

Dentist
By OBI - Brazilian Informatics Olympiad 2010, Brazil

Time Limit: 1 second

Dentists are extremely meticulous in their work, requiring precision in all their activities. Pedro is a dentist as meticulous as any other. Unfortunately, his secretary is not very organized and, in an effort to accommodate patients, allows them to schedule appointments at any time they wish, disregarding other scheduled times. This leads to multiple scheduling conflicts, which have greatly frustrated Pedro and his patients. For example, if an appointment starts at 9 AM and lasts 2 hours, no other appointment should be scheduled to start at 10 AM.

Upon realizing his schedule had conflicts, Pedro asked for your help to determine the maximum number of appointments that can be attended without overlap.

You must write a program that, given the start and end times of the appointments scheduled by the secretary, outputs the maximum number of appointments that can be attended without any overlap.

Input
The first line of the input contains an integer N (1 ≤ N ≤ 10,000), indicating the number of appointments scheduled by the secretary. Each of the following N lines contains a pair of integers X and Y, separated by a single space (0 ≤ X < Y ≤ 1,000,000), representing the start and end times of an appointment, respectively. Assume that if one appointment starts at the exact moment another ends, there is no overlap. The start times are provided in order, and multiple appointments may start at the same time.

Output
Your program must print a single line containing an integer representing the maximum number of appointments that can be attended without any overlap.

'''

def max_consultas(consultas):
    consultas.sort(key=lambda x: x[1])
    
    count = 0
    fim_anterior = 0
    
    for inicio, fim in consultas:
        if inicio >= fim_anterior:
            count += 1
            fim_anterior = fim
    
    return count

n = int(input())
consultas = []

for _ in range(n):
    x, y = map(int, input().split())
    consultas.append((x, y))

print(max_consultas(consultas))
