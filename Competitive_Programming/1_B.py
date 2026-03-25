a, b, c = input().split( )
a = int(a)
b = int(b)
c = int(c)

if a + b - c == 0:
    print("S")
elif a + c - b == 0:
    print("S")
elif c + b - a == 0:
    print("S")
elif a - b - c == 0:
    print("S")
elif b - c - a == 0:
    print("S")
elif c - a - b == 0:
    print("S")
elif a == b:
    print("S")
elif b == c:
    print("S")
elif a == c:
    print("S")

else: print("N")