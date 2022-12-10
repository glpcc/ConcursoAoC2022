f = open('input.txt')

lines = [i.strip() for i in f.readlines()]

cycle = 1
register = 1
signal_strength_sum = 0
for line in lines:
    if line == 'noop':
        cycle += 1
        if cycle%40 == 20: 
            signal_strength_sum += register*cycle
    else:
        _, value = line.split(' ')
        value = int(value)
        if cycle%40 == 19:
            signal_strength_sum += register*(cycle+1)
        elif cycle%40 == 18:
            signal_strength_sum += (register+value)*(cycle+2)
        cycle += 2
        register += value

print(signal_strength_sum)