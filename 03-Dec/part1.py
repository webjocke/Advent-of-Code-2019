
def generate_paths(instructions):
    history = []
    now = [0,0]

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
            history.append(tuple(now))

    return history

with open("i") as fp:
    paths = fp.read().split("\n")
    
    history_one = generate_paths([x.strip() for x in paths[0].split(",")])
    history_two = generate_paths([x.strip() for x in paths[1].split(",")])

    overlapping = set(history_one).intersection(history_two)
    create_list_with_distace_to_center = sorted([(abs(point[0])+abs(point[1]), point) for point in overlapping], key=lambda x: x[0], reverse=False)
    
    print "Closed to center of crossed points is", create_list_with_distace_to_center[0][0], "steps"
    
