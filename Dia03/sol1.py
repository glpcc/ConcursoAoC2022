
f = open('input.txt')

lines = f.readlines()
total_val = 0
for line in lines:
    set1 = set(line[0:len(line)//2])
    set2 = set(line[len(line)//2:])
    inter = list(set1.intersection(set2))[0]
    if ord(inter) < 97:
        total_val += ord(inter) - 64 + 26
    else:
        total_val += ord(inter) - 96

print(total_val)