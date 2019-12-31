with open("i")as fp:
    e,f=enumerate,[2 for a in range(25*6)]
    for i,p in e(fp.read()):
        if p!="2"and f[i%(25*6)]==2:f[i%(25*6)]=p
    for i,c in e(f):print("X\n"if c=="1"and i%25==24 else"X"if c=="1"else"\n"if i%25==24 else" ",end='')