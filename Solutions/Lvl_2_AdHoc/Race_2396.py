'''

link: https://judge.beecrowd.com/en/problems/view/2396

Race
By OBI - Brazilian Informatics Olympiad 2011, Brazil

Time Limit: 1 second

Every year, despite internal crises, the inhabitants of Mlogonia unite around a sport that is a national passion: car racing. 
The annual Great Race is a major event organized by the Mlogonia Racing Association (ACM), widely broadcast on television and 
covered by newspapers and magazines across the country. The race results dominate conversations for weeks.

For a long time, the Great Race results were compiled manually. Specialized observers would go to the track to measure the time 
of each of the N cars, numbered from 1 to N, for each of the M laps, recording the results in tables for later analysis by teams 
and journalists. This process introduced many errors, prompting the organization to computerize the entire system.

The ACM realized that building the system would require significant effort and decided to enlist the help of a team of programmers. 
Percival was hired to write the part of the software that determines the winning cars but is struggling and needs your help. 
Your task in this problem is to determine the top three cars, given the times each car took to complete each lap of the race.

In the second test case below, there are 5 cars in a two-lap race. The times for each car in each lap are as shown in the following table.

-----------------------------
| Car | Lap 1 | Lap 2 | Total
Car 1:    3       7      10
Car 2:    2       5      7
Car 3:    1       1      2
Car 4:    15      2      17
Car 5:    2       2      4
-----------------------------

Thus, the winner was car 3 (with a total time of 2), followed by car 5 (with a total time of 4), and car 2 (with a total time of 7).

Input
The first line of the input contains two integers N (3 ≤ N ≤ 100) and M (1 ≤ M ≤ 100), representing the number of cars and the 
number of laps in the race, respectively.

Each of the following N lines represents a car: the first line corresponds to car 1, the second to car 2, and so on. Each 
line contains M integers representing the times for each lap of the race: the first integer is the time for the first lap, 
the second is the time for the second lap, and so forth (1 ≤ any input number representing a lap time ≤ 10^6).

It is guaranteed that no two cars have the same total time to complete the entire race.

Output
The output consists of three lines, each containing a single integer. The first line contains the number of the car that 
won the race, the second contains the number of the second-place car, and the third contains the number of the third-place car.

'''

carros, voltas = map(int, input().split())
tempos_totais = []

for i in range(carros):
    tempos_voltas = list(map(int, input().split()))
    tempo_total = sum(tempos_voltas)
    tempos_totais.append((tempo_total, i + 1))

tempos_totais.sort()

print(tempos_totais[0][1]) 
print(tempos_totais[1][1])  
print(tempos_totais[2][1]) 
