'''

link: https://judge.beecrowd.com/en/problems/view/2460

Queue
By OBI - Brazilian Informatics Olympiad 2014, Brazil

Time Limit: 1 second
With the World Cup approaching, the number of people queuing to buy tickets has increased significantly. As the queues grow longer, 
less patient individuals tend to give up on purchasing tickets and leave the queue, freeing up spots for others. When a person leaves 
the queue, everyone behind them moves one step forward, ensuring there is never an empty space between two people. The queue initially 
contains <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N<
/annotation></semantics></math> people, each with a unique identifier. Joãozinho knows the initial state of the queue and the identifier
s of the people who left the queue, in the order they left. Knowing that no one else joined the queue after the initial state, Joãozinho 
wants to know the final state of the queue.

Input
The first line contains an integer <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi></mrow><annotation 
encoding="application/x-tex">N</annotation></semantics></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow>
<mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>50</mn><mo separator="true">,</mo><mn>000</mn></mrow><annotation encoding="application/
x-tex">1 \leq N \leq 50,000</annotation></semantics></math>), representing the initial number of people in the queue. The second line 
contains <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N
</annotation></semantics></math> integers representing the identifiers of the people in the queue. The first identifier corresponds to 
the person at the front of the queue. It is guaranteed that no two people have the same identifier. The third line contains an integer 
<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>M</mi></mrow><annotation encoding="application/x-tex">M</annotation>
</semantics></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>≤</mo><mi>M</mi><mo>≤</mo><mn>50</mn><mo s
eparator="true">,</mo><mn>000</mn></mrow><annotation encoding="application/x-tex">1 \leq M \leq 50,000</annotation></semantics></math> and <math 
xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>M</mi><mo>&#x3C;</mo><mi>N</mi></mrow><annotation encoding="application/x-tex">M &#x3C; 
N</annotation></semantics></math>), representing the number of people who left the queue. The fourth line contains <math xmlns="
http://www.w3.org/1998/Math/MathML"><><mrow><mi>M</mi></mrow><annotation encoding="application/x-tex">M</annotation></
semantics></math> integers representing the identifiers of the people who left the queue (each identifier is between 1 and 100,000), 

in the order they left. It is guaranteed that no identifier appears twice in this list.
Output
Your program must print a single line containing <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi><mo>−</mo><mi>
M</mi></mrow><annotation encoding="application/x-tex">N - M</annotation></semantics></math> integers representing the identifiers of the people
 who remained in the queue, in their order of arrival.

'''

n = int(input())  
lista_pessoas_int = list(map(int, input().split()))

m = int(input())  
lista_saida_int = set(map(int, input().split()))  

lista_final = [i for i in lista_pessoas_int if i not in lista_saida_int]

print(" ".join(map(str, lista_final)))
