
count = 0
accepted = []

#for i in range(123257, 647015):
for i in range(271973, 785962):
    behind_behind_last = '0'
    behind_last = '0'
    last = '0'
    have_a_double = False
    have_not_decresed = True
    for index, char in enumerate(str(i)):
        if (char != last and last == behind_last and behind_last != behind_behind_last):
            have_a_double = True
        if (int(char) < int(last)):
            have_not_decresed = False
        if (index == len(str(i))-1 and char == last and char != behind_last):
            have_a_double = True
        behind_behind_last = behind_last
        behind_last = last
        last = char
    if (have_a_double and have_not_decresed):
        count += 1
        accepted.append(i)

print accepted
print count
