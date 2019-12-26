
count = 0
accepted = []

for i in range(123257, 647015):
    last = '0'
    have_a_double = False
    have_not_decresed = True
    for char in str(i):
        if (char == last):
            have_a_double = True
        if (int(char) < int(last)):
            have_not_decresed = False
        last = char
    if (have_a_double and have_not_decresed):
        count += 1
        accepted.append(i)

print accepted
print count
