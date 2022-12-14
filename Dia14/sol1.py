f = open('input.txt')

lines = [[[int(k) for k in j.split(',')] for j in i.strip().split('->')] for i in f.readlines()]

# max_x = 544
# max_y = 164
# min_x = 483
# min_y = 16
# Map delimitors 480-550 x and 0-164 y

# Create the map 0 if air, 1 if blocked
mapp = [[0 for j in range(70)] for i in range(165)]

for line in lines:
    prev_point = line[0]
    for point in line[1:]:
        if prev_point[0] == point[0]:
            directon = 1 if prev_point[1] < point[1] else -1
            for i in range(0,point[1]-prev_point[1],directon):
                mapp[prev_point[1] + i][prev_point[0]-480] = 1
        elif prev_point[1] == point[1]:
            directon = 1 if prev_point[0] < point[0] else -1
            for i in range(0,point[0]-prev_point[0],directon):
                mapp[prev_point[1]][prev_point[0]-480+i] = 1
        prev_point = point
    mapp[line[-1][1]][line[-1][0]-480] = 1

done = False
sand_num = 0
while not done:
    on_rest = False
    sand_pos = (500,0)
    while not on_rest:
        if sand_pos[1]+1 == len(mapp):
            on_rest = True
            done = True
        elif mapp[sand_pos[1]+1][sand_pos[0]-480] == 0:
            sand_pos = (sand_pos[0],sand_pos[1]+1)
        elif mapp[sand_pos[1]+1][sand_pos[0]-1-480] == 0:
            sand_pos = (sand_pos[0]-1,sand_pos[1]+1)
        elif mapp[sand_pos[1]+1][sand_pos[0]+1-480] == 0:
            sand_pos = (sand_pos[0]+1,sand_pos[1]+1)
        else:
            on_rest = True
            mapp[sand_pos[1]][sand_pos[0]-480] = 2
            sand_num += 1

on_rest = False
sand_pos = (500,0)
while not on_rest:
    if sand_pos[1]+1 == len(mapp):
        on_rest = True
        done = True
    elif mapp[sand_pos[1]+1][sand_pos[0]-480] == 0:
        mapp[sand_pos[1]+1][sand_pos[0]-480] = 4
        sand_pos = (sand_pos[0],sand_pos[1]+1)
    elif mapp[sand_pos[1]+1][sand_pos[0]-1-480] == 0:
        mapp[sand_pos[1]+1][sand_pos[0]-480-1] = 4
        sand_pos = (sand_pos[0]-1,sand_pos[1]+1)
    elif mapp[sand_pos[1]+1][sand_pos[0]+1-480] == 0:
        mapp[sand_pos[1]+1][sand_pos[0]-480+1] = 4
        sand_pos = (sand_pos[0]+1,sand_pos[1]+1)
    else:
        on_rest = True
        mapp[sand_pos[1]][sand_pos[0]-480] = 2
        sand_num += 1
mapp[0][500-480] = 3
for i in mapp:
    for j in i:
        print(j,end='')
    print()
print(sand_num)
