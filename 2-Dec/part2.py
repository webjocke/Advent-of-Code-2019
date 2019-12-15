
with open("i") as fp:
    original_steps = [int(x.strip()) for x in fp.read().split(",")]
    all_combinations = [(a,b) for a in range(100) for b in range(100)]
    
    combination_index = 0
    flip = False
    index_zero = 0
    index_one = 0
    index_two = 0
    while index_zero != 19690720:
        index_one = all_combinations[combination_index][0] if flip else all_combinations[combination_index][1]
        index_two = all_combinations[combination_index][1] if flip else all_combinations[combination_index][0]

        steps = original_steps.copy()
        steps[1] = index_one
        steps[2] = index_two

        i = 0
        while (i <= len(steps)):
            #print(i)
            if (steps[i] == 1): steps[steps[i+3]] = steps[steps[i+2]] + steps[steps[i+1]]
            elif (steps[i] == 2): steps[steps[i+3]] = steps[steps[i+2]] * steps[steps[i+1]]
            elif (steps[i] == 99): break
            i += 4

        index_zero = steps[0]
        if flip == True:
            combination_index += 1
        flip = not flip

    print(index_zero, index_one, index_two)
    print(100*index_one+index_two)