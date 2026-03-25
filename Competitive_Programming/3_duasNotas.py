set_troco = {4, 10, 20, 40, 100, 200, 7, 12, 22, 52, 102, 15, 25, 55, 105, 30, 60, 110, 70, 120, 150}

while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    
    troco = b - a
    
    if troco in set_troco:
        print("possible")
    else:
        print("impossible")
