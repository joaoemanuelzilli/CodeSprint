'''

link: https://judge.beecrowd.com/en/problems/view/3058

Supermarket
By Brazil
Time Limit: 1 second
Maria is participating in an exchange program in the kingdom of Nlogonia. She is enjoying the experience and decided to host a barbecue for her new school friends. Since she doesn’t have much money, Maria will research to buy meat at the cheapest supermarket she can find.
However, she is a bit confused about determining which supermarket offers the lowest price. The currency in Nlogonia is the Bit, abbreviated as B$, but that’s not the issue. The problem is that the custom in Nlogonia is to advertise prices differently from what Maria is used to. Prices are announced as “X Bits for Y grams of the product.”
For example, the price of a given product might be advertised as B$24.00 for 250 grams in one supermarket, B$16.00 for 100 grams in another, B$19.00 for 120 grams in another, and so on.
Can you help Maria? Given the advertised prices from supermarkets in Maria’s neighborhood, determine the minimum amount Maria must spend to buy 1 kilogram (1000 grams) of meat.
Input
The first line contains an integer <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math>, the number of supermarkets near Maria’s house. Each of the following <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math> lines indicates the price of meat at a supermarket and contains a real number <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">P</annotation></semantics></math> and an integer <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>G</mi></mrow><annotation encoding="application/x-tex">G</annotation></semantics></math>, indicating that <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>G</mi></mrow><annotation encoding="application/x-tex">G</annotation></semantics></math> grams of meat cost <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">P</annotation></semantics></math> Bits.
Output
Your program must produce a single line containing a single real number, the minimum price to buy 1 kilogram of meat. The result must be written with exactly two digits after the decimal point.
Constraints

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn></mrow><annotation encoding="application/x-tex">1 \leq N \leq 100</annotation></semantics></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>0</mn><mo>&#x3C;</mo><mi>P</mi><mo>≤</mo><mn>1000.00</mn></mrow><annotation encoding="application/x-tex">0 &#x3C; P \leq 1000.00</annotation></semantics></math>, represented with two digits after the decimal point
<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>≤</mo><mi>G</mi><mo>≤</mo><mn>1000</mn></mrow><annotation encoding="application/x-tex">1 \leq G \leq 1000</annotation></semantics></math>

'''

N = int(input())  
menor_preco = float('inf')  

for _ in range(N):
    P, G = map(float, input().split())
    preco_por_kg = (P / G) * 1000  
    if preco_por_kg < menor_preco:
        menor_preco = preco_por_kg

print(f"{menor_preco:.2f}")
