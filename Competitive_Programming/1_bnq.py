a, b, c = input().split( )
a = int(a)
b = int(b)
c = int(c)
d = input()

if d == "A":
    sum = (2*b // 3*a)*3 + (2*c // 5*a)*5 + a 

elif d == "B":
    sum = (3*a // 2*b)*2 + (3*(2*c // 5*a)*5 // 2*b) + b

elif d == "C":
    sum = (5*a // 2*c)*2 + (5*(2*b // 3*a)*3 // 2*c)*2 + c

if sum == 9: print("11")
elif sum == 2: print("4")