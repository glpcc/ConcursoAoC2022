f = open('input.txt')
lines = f.readlines()

current_cals = 0
max_cals = 0
for line in lines:
    if line != '\n':
        current_cals += int(line)
    else:
        if current_cals > max_cals:
            max_cals = current_cals
        current_cals = 0

print(max_cals)