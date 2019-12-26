
print "="*40
print "="*40
print "="*40
print "PROGRAM START"

with open("i") as fp:
    steps = [int(x.strip()) for x in fp.read().split(",")]

    # Print the starting memory data
    print steps

    i = 0
    while (i <= len(steps)):

        param_modes = []
        opcode = []

        temp = [char for char in str(steps[i])]
        temp.reverse()

        for index, code in enumerate(temp):
            if (index == 0 or index == 1): opcode.append(code)
            else: param_modes.append(code)

        opcode.reverse()
        opcode = int(''.join(opcode))


        # ==================
        # ALL INSTRUCTIONS
        # ==================

        if (opcode == 1):
            # Instruction 1
            # Adds two numbers together

            param1 = steps[steps[i+1]] if len(param_modes) < 1 or param_modes[0] == "0" else steps[i+1]
            param2 = steps[steps[i+2]] if len(param_modes) < 2 or param_modes[1] == "0" else steps[i+2]
            steps[steps[i+3]] = param2 + param1
            i += 4

        elif (opcode == 2):
            # Instruction 2
            # Multiplies two numbers together

            param1 = steps[steps[i+1]] if len(param_modes) < 1 or param_modes[0] == "0" else steps[i+1]
            param2 = steps[steps[i+2]] if len(param_modes) < 2 or param_modes[1] == "0" else steps[i+2]
            steps[steps[i+3]] = param2 * param1
            i += 4

        elif (opcode == 3):
            # Instruction 3
            # Input, takes value from user

            steps[steps[i+1]] = int(input("ID of air conditioner unit to test: "))
            i += 2

        elif (opcode == 4):
            # Instruction 4
            # Output, prints a value to console

            param1 = steps[steps[i+1]] if len(param_modes) < 1 or param_modes[0] == "0" else steps[i+1]
            print "=O=", param1
            i += 2
        
        elif (opcode == 5):
            # Instruction 5
            # jump-if-true. If the first parameter is non-zero, it sets the instruction pointer to
            # the value from the second parameter. Otherwise, it does nothing.

            param1 = steps[steps[i+1]] if len(param_modes) < 1 or param_modes[0] == "0" else steps[i+1]
            param2 = steps[steps[i+2]] if len(param_modes) < 2 or param_modes[1] == "0" else steps[i+2]

            if (param1 != 0):
                i = param2
            else:
                i += 3
        
        elif (opcode == 6):
            # Instruction 6
            # jump-if-false. if the first parameter is zero, it sets the instruction pointer to
            # the value from the second parameter. Otherwise, it does nothing.

            param1 = steps[steps[i+1]] if len(param_modes) < 1 or param_modes[0] == "0" else steps[i+1]
            param2 = steps[steps[i+2]] if len(param_modes) < 2 or param_modes[1] == "0" else steps[i+2]

            if (param1 == 0):
                i = param2
            else:
                i += 3
        
        elif (opcode == 7):
            # Instruction 7
            # less than. if the first parameter is less than the second parameter, it stores 1 in
            # the position given by the third parameter. Otherwise, it stores 0.

            param1 = steps[steps[i+1]] if len(param_modes) < 1 or param_modes[0] == "0" else steps[i+1]
            param2 = steps[steps[i+2]] if len(param_modes) < 2 or param_modes[1] == "0" else steps[i+2]

            if (param1 < param2):
                steps[steps[i+3]] = 1
            else:
                steps[steps[i+3]] = 0
            i += 4
        
        elif (opcode == 8):
            # Instruction 8
            # equals. if the first parameter is equal to the second parameter, it stores 1 in
            # the position given by the third parameter. Otherwise, it stores 0

            param1 = steps[steps[i+1]] if len(param_modes) < 1 or param_modes[0] == "0" else steps[i+1]
            param2 = steps[steps[i+2]] if len(param_modes) < 2 or param_modes[1] == "0" else steps[i+2]

            if (param1 == param2):
                steps[steps[i+3]] = 1
            else:
                steps[steps[i+3]] = 0
            i += 4

        elif (opcode == 99):
            # Instruction 99
            break
    
    # Print the resulting memory data
    print steps