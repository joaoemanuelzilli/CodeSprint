'''

link: https://judge.beecrowd.com/en/problems/view/2420

War for Territory
By OBI - Brazilian Informatics Olympiad 2012, Brazil

Time Limit: 1 second
West Tombólia and East Tombólia waged a 50-year war over the size of their territories. For the sake of their populations, 
the governments decided to sign a treaty to end the conflict. The treaty involves a fair and contiguous division of the territory. 
They have asked for your help to calculate the division point of the territory. After so many years of war, the countries cannot afford 
to pay for your trip to inspect the territory beforehand. Instead, they provided a list of integers <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>a</mi><mn>2</mn></msub><mo separator="true">,</mo><mo>…</mo><mo separator="true">,</mo><msub><mi>a</mi><mi>N</mi></msub></mrow><annotation encoding="application/x-tex">a_1, a_2, \ldots, a_N</annotation></semantics></math> indicating the size of each section of the territory. Section <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">a_1</annotation></semantics></math> is adjacent to section <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub></mrow><annotation encoding="application/x-tex">a_2</annotation></semantics></math>, which is adjacent to section <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mn>3</mn></msub></mrow><annotation encoding="application/x-tex">a_3</annotation></semantics></math>, and so on. The governments want a division at section <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>k</mi></mrow><annotation encoding="application/x-tex">k</annotation></semantics></math> such that the sum of the lengths of sections <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">a_1</annotation></semantics></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mi>k</mi></msub></mrow><annotation encoding="application/x-tex">a_k</annotation></semantics></math> equals the sum of the lengths of.sections <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><annotation encoding="application/x-tex">a_{k+1}</annotation></semantics></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mi>N</mi></msub></mrow><annotation encoding="application/x-tex">a_N</annotation></semantics></math>.
Your task is, given a list of positive integers <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>a</mi><mn>2</mn></msub><mo separator="true">,</mo><mo>…</mo><mo separator="true">,</mo><msub><mi>a</mi><mi>N</mi></msub></mrow><annotation encoding="application/x-tex">a_1, a_2, \ldots, a_N</annotation></semantics></math>, to determine the section <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>k</mi></mrow><annotation encoding="application/x-tex">k</annotation></semantics></math> where the sum of the lengths of sections <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">a_1</annotation></semantics></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mi>k</mi></msub></mrow><annotation encoding="application/x-tex">a_k</annotation></semantics></math> is equal to the sum of the lengths of sections <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><annotation encoding="application/x-tex">a_{k+1}</annotation></semantics></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mi>N</mi></msub></mrow><annotation encoding="application/x-tex">a_N</annotation></semantics></math>.
Input
The first line of the input contains an integer <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><msup><mn>0</mn><mn>5</mn></msup></mrow><annotation encoding="application/x-tex">1 \leq N \leq 10^5</annotation></semantics></math>), indicating the number of territory sections. The second line contains <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math> integers <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>a</mi><mn>2</mn></msub><mo separator="true">,</mo><mo>…</mo><mo separator="true">,</mo><msub><mi>a</mi><mi>N</mi></msub></mrow><annotation encoding="application/x-tex">a_1, a_2, \ldots, a_N</annotation></semantics></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>≤</mo><msub><mi>a</mi><mi>i</mi></msub><mo>≤</mo><mn>100</mn></mrow><annotation encoding="application/x-tex">1 \leq a_i \leq 100</annotation></semantics></math>, for <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi><mo>=</mo><mn>1</mn><mo separator="true">,</mo><mn>2</mn><mo separator="true">,</mo><mo>…</mo><mo separator="true">,</mo><mi>N</mi></mrow><annotation encoding="application/x-tex">i = 1, 2, \ldots, N</annotation></semantics></math>), separated by single spaces, representing the lengths of the sections.
Output
Your program must print a single line containing an integer indicating the section of the territory where the division will occur. (It is guaranteed that there is always a division that satisfies the countries' conditions.)

'''
a = int(input())
list = input().split(' ')
list2 = []

for i in (list):
    list2.append(int(i))

soma = (sum(list2))/2

b = 0
c = 0

while b != soma:
    b += list2[c]
    c += 1



print(c)
