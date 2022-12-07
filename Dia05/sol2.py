import re

f = open('input.txt')
# lines = [i for i in f.readlines()]
lines = list(f.readlines())

stacks = [[] for i in range(9)]
for line in lines[7::-1]:
    values = [line[1+4*i] for i in range(9)]
    for j in range(9):
        if values[j] != ' ':
            stacks[j].append(values[j])

# Now parse the moves
for line in lines[10:]:
    cuant,from_col, to_col = [int(i) for i in re.findall('\d+',line)]
    moved_crates = stacks[from_col-1][-cuant:]
    stacks[from_col-1] = stacks[from_col-1][:-cuant]
    stacks[to_col-1] = stacks[to_col-1] + moved_crates

print(stacks)
print(''.join([i[-1] for i in stacks]))
f.close()
