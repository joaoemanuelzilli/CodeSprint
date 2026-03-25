
/*

link: https://judge.beecrowd.com/en/problems/view/3428

Eliminating Ballons
By Sociedade Brasileira de Computação (SBC), Maratona de Programação da SBC - ICPC - 2022 BR Brazil

Timelimit: 1
An enourmous number of balloons are floating about in the Convention Hall after the Awarding Ceremony of the ICPC Subregional Contest. The manager of the Convention Hall is angry, because he will host another event tomorrow and the ballons must be removed. Fortunately this year Carlinhos came prepared with his bow and arrows to pop the balloons.

Also, luckily, due to the air conditioning flow, the balloons are all in the same vertical plane (that is, a plane parallel to a wall), although in distinct heights and positions.

Carlinhos will shoot from the left side of the convention hall, at a chosen height, in the direction of the right side of the Convention Hall. Each arrow moves from left to right, at the height it was shot, in the same vertical plane of the baloons. When an arrow touches a balloon, the baloon pops and the arrow continues its movement to the right, at a height decreased by 1. In other words, if the arrow was at height H, after popping a balloon it continues at height H-1.

Carlinhos wants to pop all balloons shooting as few arrows as possible. Can you help him?

Input
The first line of input contains an integer N, the number of balloons (1≤N≤5*105). Since all balloons are in the same vertical plane, lets define that the height of a ballon is given in relation to the y-axis and the position of a balloon is given in relation to the x-axis. Balloons are numbered from 1 to N. Balloon numbers indicate theis positions, from leftmost (balloon number 1) to rightmost (balloon number N), independent of their heights. The position of balloon number i is different from the position of balloon number i+1, for all 1. The second line contains N integers Hi, where Hi indicates the height of balloon number i (1≤Hi≤106 for 1≤i≤N).

Output
Your program must output a single line, containing a single integer, the miminum number of arrows that Carlinhos needs to shoot to pop all balloons.

*/


#include <stdio.h>

#define MAX_HEIGHT 1000000

int main() {
    int n;
    scanf("%d", &n);

    int alturas[MAX_HEIGHT + 1] = {0};
    int flechas = 0;

    for (int i = 0; i < n; i++) {
        int h;
        scanf("%d", &h);

        if (alturas[h] > 0) {
            alturas[h]--;
            alturas[h - 1]++;
        } else {
            flechas++;
            alturas[h - 1]++;
        }
    }

    printf("%d\n", flechas);

    return 0;
}
