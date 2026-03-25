def robot_scarecrow(N, C, S, commands):
    current_station = 1
    visit_count = 0

    if current_station == S:
        visit_count += 1

    for command in commands:
        if command == 1:
            current_station += 1
            if current_station > N:
                current_station = 1
        elif command == -1:
            current_station -= 1
            if current_station < 1:
                current_station = N
        
        if current_station == S:
            visit_count += 1
    
    return visit_count

N, C, S = map(int, input().split())
commands = list(map(int, input().split()))

result = robot_scarecrow(N, C, S, commands)
print(result)
