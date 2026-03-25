'''

link: https://judge.beecrowd.com/en/problems/view/1104

Exchanging Cards
Maratona de Programação da SBC  Brazil

Timelimit: 1


Alice and Betty collect Pokémon cards. The cards are printed for a game that imitates the battle system of one of the most popular videogames in history, but Alice and Betty are too young to actually play the game, and are only interested in the actual cards. To make it easier, we'll assume each card has a unique identifier, given as an integer number.

Both girls have a set of cards, and, like most girls their age, like to trade the cards they have. They obviously don't care about identical cards they both have, and they don't want to receive repeated cards in the trade. Besides, the cards are traded in a single operation: Alice gives Betty N distinct cards and receives back other N distinct cards.

The girls want to know what is the maximum number of cards they can trade. For instance, if Alice has cards {1, 1, 2, 3, 5, 7, 8, 8, 9, 15} and Betty has cards {2, 2, 2, 3, 4, 6, 10, 11, 11}, they can trade at most four cards.

Write a program that given the sets of cards owned by Alice and Betty, determines the maximum number of cards they can trade.

Input
The input contains several test cases. The first line of a test case contains two integers A and B, separated by a blank space, indicating respectively the number of cards Alice and Betty have (1 ≤ A ≤ 104 and 1 ≤ B ≤ 104). The second line contains A space-separated integers Xi, each indicating one of Alice\'s cards(1 ≤ Xi ≤ 105). The third line contains B integers Yi separated by whitespaces, each number indicating one of Betty's cards(1 ≤ Yi ≤ 105). Alice and Betty's cards are listed in non-descending order.

The end of input is indicated by a line containing only two zeros, separated by a blank space.

Output
For each test case, your program should print a single line, containing an integer number, indicating the maximum number of cards Alice and Betty can trade.

'''

def max_trocas(alice, beatriz):
    conjunto_alice = set(alice)
    conjunto_beatriz = set(beatriz)
    
    cartas_trocaveis_alice = conjunto_alice - conjunto_beatriz
    cartas_trocaveis_beatriz = conjunto_beatriz - conjunto_alice
    
    return min(len(cartas_trocaveis_alice), len(cartas_trocaveis_beatriz))

def main():
    while True:
        A, B = map(int, input().split())
        
        if A == 0 and B == 0:
            break
        
        cartas_alice = list(map(int, input().split()))
        cartas_beatriz = list(map(int, input().split()))
        
        print(max_trocas(cartas_alice, cartas_beatriz))

if __name__ == "__main__":
    main()
