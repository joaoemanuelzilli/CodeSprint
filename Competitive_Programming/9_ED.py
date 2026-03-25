from queue import PriorityQueue, Queue
import sys

for line in sys.stdin:

    try:
        N = int(line.strip())  
    except ValueError:
        break

    ehFila = True
    ehPilha = True
    ehPQ = True

    pilha = []
    fila = Queue()
    pq = []  

    for i in range(N):
        acao, X = map(int, input().split())

        if acao == 1:
            fila.put(X)
            pilha.append(X)
            pq.append(-X)  

        elif acao == 2:
            if len(pilha) == 0 or pilha[-1] != X:
                ehPilha = False
            else:
                pilha.pop()

            if fila.empty() or fila.queue[0] != X:
                ehFila = False
            else:
                fila.get()

            if len(pq) == 0 or -max(pq) != X:  
                ehPQ = False
            else:
                pq.remove(-max(pq))  

    if not ehFila and not ehPilha and not ehPQ:
        print("impossible")
    elif (ehFila and ehPilha) or (ehFila and ehPQ) or (ehPilha and ehPQ):
        print("not sure")
    elif ehPilha:
        print("stack")
    elif ehFila:
        print("queue")
    elif ehPQ:
        print("priority queue")
