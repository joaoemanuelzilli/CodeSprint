def process_insc():
    yes_insc = []
    no_insc = []
    void = []
    registrations = {}

    while True:
        entry = input().strip()
        if entry == "FIM":
            break
        name, choice = entry.split()
        if choice == "YES":
            if name in registrations:
                registrations[name] += 1
            else:
                registrations[name] = 1
            yes_insc.append(name)
        else:
            no_insc.append(name)

    yes_insc = list(dict.fromkeys(yes_insc))
    yes_insc.sort()
    no_insc.sort()
    max_name_length = -1
    winner = None
    for name in yes_insc:
        if len(name) > max_name_length or (len(name) == max_name_length and registrations[name] > registrations[winner]):
            max_name_length = len(name)
            winner = name

    for name in yes_insc:
        print(name)
    
    for name in no_insc:
        print(name)
    
    print(void)
    print("Amigo do Habay:")
    print(winner)

process_insc()
