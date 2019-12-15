def a(x, s):
    while (x > 0): s.append(x); x = int(float(x)/3)-2
    return s
with open("i") as f: print(sum([sum(a(int(x.strip()), [-int(x.strip())])) for x in f.readlines()]))