
def generate_paths(instructions):
    full_history = []
    now = [0,0]
    totalt_steps = 0

    for instruction in instructions:
        direction = instruction[0]
        steps = instruction[1:]

        for i in range(int(steps)):
            if direction == "R":
                now[0] += 1
            elif direction == "L":
                now[0] -= 1
            elif direction == "U":
                now[1] += 1
            elif direction == "D":
                now[1] -= 1
            totalt_steps += 1
            full_history.append((totalt_steps, tuple(now)))

    return full_history

with open("i") as fp:
    paths = fp.read().split("\n")
    
    full_history_one = generate_paths([x.strip() for x in paths[0].split(",")])
    full_history_two = generate_paths([x.strip() for x in paths[1].split(",")])
    
    new_list = []
    procent = 0.0
    for index2, i_one in enumerate(full_history_one):
        tal = round(float(index2)/len(full_history_one), 3)
        if tal > procent:
            procent = tal
            print tal*100, " %"
        for i_two in full_history_two:
            if i_one[1] == i_two[1]:
                new_list.append(i_one[0]+i_two[0])
                break
    
    new_list.sort()
    print "RESULT IS", new_list[0]
    
