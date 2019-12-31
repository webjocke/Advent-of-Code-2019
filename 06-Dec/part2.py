from copy import deepcopy

def f(orbit, all_o, path_to_here=[]):
    path_to_here = deepcopy(path_to_here)
    for orbit_local in all_o:
        if orbit_local[1] == orbit:
            path_to_here.append(orbit_local[0])
            path_to_here = f(orbit_local[0], all_o, path_to_here)
    return path_to_here

with open("i") as i:
    lst = [(x.split(')')[0], x.split(')')[1]) for x in i.read().split("\n")]
    yous = f("YOU", lst)
    yous.reverse()
    sans = f("SAN", lst)

    orbit_steps = []
    for san in sans:
        orbit_steps.append(san)
        if san in yous:
            on = False
            for you in yous:
                if on:
                    orbit_steps.append(you)
                if you == san:
                    on = True
            break
    print orbit_steps
    print len(orbit_steps)-1
    