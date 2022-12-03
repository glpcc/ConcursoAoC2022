
f = open('input.txt')

lines = list(f.readlines())
total_val = 0
print(lines[2].strip())
for i in range(0,len(lines),3):
    set1 = set(lines[i].strip())
    set2 = set(lines[i+1].strip())
    set3 = set(lines[i+2].strip())
    inter = list(set1.intersection(set2).intersection(set3))[0]
    if ord(inter) < 97:
        total_val += ord(inter) - 64 + 26
    else:
        total_val += ord(inter) - 96

f.close()
print(total_val)