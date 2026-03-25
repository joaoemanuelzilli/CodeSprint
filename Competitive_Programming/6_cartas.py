def cards(n):
    if n == 0:
        return
    
    queue = list(range(1, n + 1))  
    discarded = []
    index = 0  

    while len(queue) - index > 1:
        discarded.append(queue[index])  
        index += 1
        queue.append(queue[index])      
        index += 1

    remaining_card = queue[index] 

    discarded_str = ', '.join(map(str, discarded))
    print(f"Discarded cards: {discarded_str}")
    print(f"Remaining card: {remaining_card}")

if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        cards(n)
