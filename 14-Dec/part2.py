''' Webjocke, Advent of Code 14 dec '''
import time

def read_input_file(filepath):
    formulas = {}
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            # Format output
            output = line.rstrip().split("=>")[1].strip()
            output_amount = int(output.split()[0])
            output_type = output.split()[1]

            # Format input(s)
            inputs = map(str.strip, line.rstrip().split("=>")[0].split(","))
            all_inputs = []
            for input in inputs:
                all_inputs.append([input.split()[1], int(input.split(" ")[0])])

            # Add line's values to formulas and read in next line
            formulas[output_type] = [output_amount, all_inputs]
            line = fp.readline()

    return formulas

def add_to_dic(chem_type, amount, dic):
    if chem_type in dic:
        dic[chem_type] += amount
    else:
        dic[chem_type] = amount
    return dic

def remove_from_dic(chem_type, amount, dic):
    dic[chem_type] -= amount
    return dic

def if_enough_stock(chem_type, amount, stock):
    #print chem_type, amount, stock
    if chem_type in stock:
        if stock[chem_type] >= amount:
            return True
    return False

def make_convertion(chemical_wanted, ore_spent, stock, formulas):
    
    for input in formulas[chemical_wanted][1]:

        # Check if we already have enough of this chemical in stock
        if input[0] == "ORE":
            # We need more ore to proceed
            ore_spent += input[1]
        else:
            while not if_enough_stock(input[0], input[1], stock):

                # If we need to make more
                ore_spent, stock = make_convertion(input[0], ore_spent, stock, formulas)

            # We now have enoght in stock
            remove_from_dic(input[0], input[1], stock)

    stock = add_to_dic(chemical_wanted, formulas[chemical_wanted][0], stock)
    return ore_spent, stock

def main():
    print("Program Start")

    formulas = read_input_file('input.txt')
    ore_spent = 0
    stock = {}

    ores_goal = 1000000000000 # 1000000000000

    amount_fuel = 0
    while (ore_spent < ores_goal): # 1000000000000
        start = time.time()
        ore_spent, stock = make_convertion("FUEL", ore_spent, stock, formulas)
        amount_fuel += 1
        if (amount_fuel % 100 == 0):
            print (round((time.time() - start)*1000), "ms per FUEL - PROG", round(float(ore_spent)/ores_goal*100, 3), "%", "FUEL", amount_fuel)
    amount_fuel -= 1

    #print formulas
    print("Stock left", stock)
    print("ORE's spent", ore_spent)
    print("Max FUEL per 1 tri ORE's", amount_fuel)

main()