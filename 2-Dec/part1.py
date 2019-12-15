with open("i") as fp:
    steps = [int(x.strip()) for x in fp.read().split(",")]
    i = 0
    while (i <= len(steps)):
        if (steps[i] == 1): steps[steps[i+3]] = steps[steps[i+2]] + steps[steps[i+1]]
        elif (steps[i] == 2): steps[steps[i+3]] = steps[steps[i+2]] * steps[steps[i+1]]
        elif (steps[i] == 99): break
        i += 4
    print(steps[0])