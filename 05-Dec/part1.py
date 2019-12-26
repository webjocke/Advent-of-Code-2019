
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
            # Takes a input from console and puts in memory

            steps[steps[i+1]] = int(input("ID of air conditioner unit to test: "))
            i += 2

        elif (opcode == 4):
            # Instruction 4
            # Prints a value from memory to console

            param1 = steps[steps[i+1]] if len(param_modes) < 1 or param_modes[0] == "0" else steps[i+1]
            print "=O=", param1
            i += 2

        elif (opcode == 99):
            # Instruction 99
            break
    
    # Print the resulting memory data
    print steps