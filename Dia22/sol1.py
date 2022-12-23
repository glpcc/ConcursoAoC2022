import re
f = open("input.txt")
lines = [i for i in f.readlines()]
instrucctions = lines[201].strip()
instrucctions = list(re.findall('R|L|\d+',instrucctions))
m = lines[:200]
walls: set[tuple[int,int]] = set()
horizontal_delimitions: list[tuple[int,int]] = []
for i,line in enumerate(m):
    x = 0
    y = i
    delimition = [0,0]
    started_counting = False
    for j in line:
        if j != ' ' and not started_counting:
            delimition[0] = x
            started_counting = True
        if j == '#':
            walls.add((x,y))
        if j == '\n':
            delimition[1] = x-1
        x += 1
    horizontal_delimitions.append(tuple(delimition))

vertical_delimitions: list[tuple[int,int]] = []
for i in range(len(m[0])):
    x = i
    y = 0
    delimition = [0,0]
    started_counting = False
    while y < len(m) and i < len(m[y])-1:
        elem = m[y][i]
        if elem != ' ' and not started_counting:
            delimition[0] = y
            started_counting = True
        y += 1
    delimition[1] = y-1
    vertical_delimitions.append(tuple(delimition))

vertical_delimitions = vertical_delimitions[:-1]

current_pos = (50,0)
current_dir = 0
directions = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]
print(len(horizontal_delimitions))
def calculate_following_pos(curent_pos,dir):
    # print(current_pos,current_dir)
    new_pos = [curent_pos[0]+directions[dir][0],curent_pos[1]+directions[dir][1]]
    # print(new_pos,vertical_delimitions[curent_pos[0]])
    if new_pos[0] > horizontal_delimitions[curent_pos[1]][1]:
        new_pos[0] = horizontal_delimitions[curent_pos[1]][0]
    elif new_pos[0] < horizontal_delimitions[curent_pos[1]][0]:
        new_pos[0] = horizontal_delimitions[curent_pos[1]][1]
    elif new_pos[1] > vertical_delimitions[curent_pos[0]][1]:
        new_pos[1] = vertical_delimitions[curent_pos[0]][0]
    elif new_pos[1] < vertical_delimitions[curent_pos[0]][0]:
        new_pos[1] = vertical_delimitions[curent_pos[0]][1]
    return tuple(new_pos)


for i in instrucctions:
    if i == 'R':
        current_dir = (current_dir+1)%4
    elif i == 'L':
        current_dir = (current_dir-1)%4
    else:
        num = int(i)
        for i in range(num):
            new_pos = calculate_following_pos(current_pos,current_dir)
            if new_pos in walls:
                break
            else:
                current_pos = new_pos
                # print(current_pos)

print(current_pos,current_dir)
print(current_pos[1]*1000 + current_pos[0]*4 + current_dir)
