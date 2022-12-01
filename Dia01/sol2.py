f = open('input.txt')
lines = f.readlines()

current_cals = 0
elf_cals_list = []
for line in lines:
    if line != '\n':
        current_cals += int(line)
    else:
        elf_cals_list.append(current_cals)
        current_cals = 0

print(sum(sorted(elf_cals_list, reverse=True)[:3]))