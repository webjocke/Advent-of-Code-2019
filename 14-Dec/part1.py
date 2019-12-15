''' Webjocke, Advent of Code 14 dec '''

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
            formulas[output_type] = {"amount": output_amount, "inputs": all_inputs}
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
        else:
            return False
    else:
        return False

def make_convertion(chemical_wanted, ore_spent, stock, formulas):
    
    for input in formulas[chemical_wanted]["inputs"]:

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

    stock = add_to_dic(chemical_wanted, formulas[chemical_wanted]["amount"], stock)
    return ore_spent, stock

def main():
    print("Program Start")

    formulas = read_input_file('input.txt')
    ore_spent = 0
    stock = {}

    ore_spent, stock = make_convertion("FUEL", ore_spent, stock, formulas)

    #print formulas
    print("Spent", ore_spent)
    print("Stock", stock)

main()