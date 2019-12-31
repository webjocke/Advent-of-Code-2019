
with open("i") as fp:

    found = []
    for index, pixel in enumerate(fp.read()):
        if (index%(25*6) == 0):
            found.append([0,0,0])
        if pixel == "0": found[-1][0] += 1 
        if pixel == "1": found[-1][1] += 1 
        if pixel == "2": found[-1][2] += 1 

    found.sort(key=lambda tup: tup[0])
    print found[0][1]*found[0][2]
