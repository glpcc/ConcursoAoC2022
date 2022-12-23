f = open("input.txt")

elf_pos: set[tuple[int,int]] = set()
for y,i in enumerate(f.readlines()):
    for x,j in enumerate(i.strip()):
        if j == '#':
            elf_pos.add((x,y))

dirs: dict = {
    'W':(-1,0),
    'E':(1,0),
    'S':(0,1),
    'N':(0,-1),
    'SW':(-1,1),
    'NW':(-1,-1),
    'SE':(1,1),
    'NE':(1,-1)
}

rounds = 0
# print_map(elf_pos)
direction_order = [['N','NE','NW'],['S','SE','SW'],['W','NW','SW'],['E','NE','SE']]
num_moved = 1

while num_moved != 0:
    num_moved = 0
    new_elfs_pos = dict()
    for x,y in elf_pos:
        if any((x+dirs[j][0],y+dirs[j][1]) in elf_pos for j in dirs):
            done = False
            m = 0
            while not done and m < len(direction_order):
                k = direction_order[m]
                if not any((x+dirs[j][0],y+dirs[j][1]) in elf_pos for j in k):
                    new_pos = (x+dirs[k[0]][0],y+dirs[k[0]][1])
                    if new_pos in new_elfs_pos:
                        new_elfs_pos[new_elfs_pos[new_pos]] = new_elfs_pos[new_pos]
                        new_elfs_pos[(x,y)] = (x,y)
                        new_elfs_pos.pop(new_pos)
                    else:
                        new_elfs_pos[new_pos] = (x,y)
                        num_moved += 1
                    done = True
                m += 1
            if not done:
                new_elfs_pos[(x,y)] = (x,y)
        else:
            new_elfs_pos[(x,y)] = (x,y)
    direction_order = direction_order[1:] + [direction_order[0]]
    elf_pos = set(new_elfs_pos.keys())
    # print_map(elf_pos)
    rounds += 1

print(rounds)

max_x = max(elf_pos,key=lambda k: k[0])[0]
min_x = min(elf_pos,key=lambda k: k[0])[0]
max_y = max(elf_pos,key=lambda k: k[1])[1]
min_y = min(elf_pos,key=lambda k: k[1])[1]
print((max_x-min_x+1)*(max_y-min_y+1)-len(elf_pos))
                    
