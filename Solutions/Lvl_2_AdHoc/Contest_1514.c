/*

link: https://judge.beecrowd.com/en/problems/view/1514

Contest
By Cristhian Bonilha, UTFPR BR Brazil

Timelimit: 1

Most of the programmers who come to write contests with programming exercises agree in four caracteristics that every contest should achieve. Although not all of them are always achieved, more is better. The caracterists are the following:

Nobody solved all the problems.
Every problem was solved by at least one person (not necessarily the same).
There is no problem solved by everyone.
Everyone solved at least one problem (not necessarily the same).
Rafael organized a contest a few days ago, and is worried about how many of these caracteristics he got to achieve with his contest.

Given the information about the contest, with the number of contestants, the number of problems, and which contestant solved which problem, find out the number of caracteristics that were achieved on this contest.

Input
There will be several tests cases. Each test case starts with two integers N and M (3 ≤ N, M ≤ 100).

Then, there will be N lines with M integers each, where the integer on the i-th line and on the j-th column is 1 if the i-th contestant solved the j-th problem, or 0 otherwise.

The last test case is indicated when N = M = 0, which should not be processed.

Output
For each test case, print one line with one integer, representing the amount of caracteristics achieved by the given contest.

*/

#include <stdio.h>

int main() {
    int N, M;

    while (1) {
        scanf("%d %d", &N, &M);
        if (N == 0 && M == 0)
            break;

        int competidores[N][M];
        int i, j;
        int caract = 0;
        int ninguem_resolveu_tudo = 1;
        int todos_resolveram_um = 1;
        int algum_resolveu_tudo = 0;
        int algum_resolvido_por_ninguem = 0;

        for (i = 0; i < N; i++) {
            for (j = 0; j < M; j++) {
                scanf("%d", &competidores[i][j]);
            }
        }

        for (i = 0; i < N; i++) {
            int resolveu_tudo = 1;
            int resolveu_algo = 0;
            for (j = 0; j < M; j++) {
                if (competidores[i][j] == 0) {
                    resolveu_tudo = 0;
                } else {
                    resolveu_algo = 1;
                }
            }
            if (resolveu_tudo) {
                ninguem_resolveu_tudo = 0;
            }
            if (!resolveu_algo) {
                todos_resolveram_um = 0;
            }
        }

        for (j = 0; j < M; j++) {
            int resolvido = 0;
            for (i = 0; i < N; i++) {
                if (competidores[i][j] == 1) {
                    resolvido = 1;
                    break;
                }
            }
            if (!resolvido) {
                algum_resolvido_por_ninguem = 1;
                break;
            }
        }

        for (j = 0; j < M; j++) {
            int resolvido_por_todos = 1;
            for (i = 0; i < N; i++) {
                if (competidores[i][j] == 0) {
                    resolvido_por_todos = 0;
                    break;
                }
            }
            if (resolvido_por_todos) {
                algum_resolveu_tudo = 1;
                break;
            }
        }

        if (ninguem_resolveu_tudo) caract++;
        if (!algum_resolvido_por_ninguem) caract++;
        if (!algum_resolveu_tudo) caract++;
        if (todos_resolveram_um) caract++;

        printf("%d\n", caract);
    }

    return 0;
}
