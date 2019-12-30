
def f(o, a, d=0, r=0):
    for b in a:
        if b[0] == o:
            r = d + 1 + f(b[1], a, d+1, r)
    return r

with open("i") as i:
    print (f("COM", [(x.split(')')[0], x.split(')')[1]) for x in i.read().split("\n")]))
