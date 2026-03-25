a, b = input().split( )
a = int(a)
b = int(b)

list = []
list2 = []
num = 0

def parse_time(time_str):
    minutes, seconds, milliseconds = map(int, time_str.split(':'))
    return minutes * 60000 + seconds * 1000 + milliseconds

for i in range(a):
    aux = input().split(' ')
    list.append([])
    list[i].append(int(aux[0]))
    for j in range(1,b+1, 1):
        list[i].append(parse_time(aux[j]))
print (list)
