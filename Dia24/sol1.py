f = open("input.txt")
lines = [i.strip() for i in f.readlines()]

starting_pos = (1,0)
ending_pos = (150,21)
# starting_pos = (1,0)
# ending_pos = (6,5)

open_positions = {starting_pos}
walls: set[tuple[int,int]] = {(1,-1)}
up_storms: set[tuple[int,int]] = set()
down_storms: set[tuple[int,int]] = set()
left_storms: set[tuple[int,int]] = set()
right_storms: set[tuple[int,int]] = set()
for i,line in enumerate(lines):
    for j,ch in enumerate(line):
        if ch == '#':
            walls.add((j,i))
        elif ch == '^':
            up_storms.add((j,i))
        elif ch == '>':
            right_storms.add((j,i))
        elif ch == 'v':
            down_storms.add((j,i))
        elif ch == '<':
            left_storms.add((j,i))

blocked_pos = walls.union(up_storms).union(down_storms).union(left_storms).union(right_storms)

dirs = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]
mins = 0

def update_storms(ls:set[tuple[int,int]],rs: set[tuple[int,int]],ds: set[tuple[int,int]],us: set[tuple[int,int]]):
    new_ls = set()
    for i in ls:
        if i[0] -1 < 1:
            new_ls.add((150,i[1]))
        else:
            new_ls.add((i[0]-1,i[1]))
    new_rs = set()
    for i in rs:
        if i[0] + 1 > 150:
            new_rs.add((1,i[1]))
        else:
            new_rs.add((i[0]+1,i[1]))
    new_us = set()
    for i in us:
        if i[1] - 1 < 1:
            new_us.add((i[0],20))
        else:
            new_us.add((i[0],i[1]-1))
    new_ds = set()
    for i in ds:
        if i[1] + 1 > 20:
            new_ds.add((i[0],1))
        else:
            new_ds.add((i[0],i[1]+1))
    return new_ls,new_rs,new_ds,new_us

def draw_storms(ls:set[tuple[int,int]],rs: set[tuple[int,int]],ds: set[tuple[int,int]],us: set[tuple[int,int]],walls: set[tuple[int,int]]):
    for i in range(6):
        for j in range(8):
            if (j,i) in ls:
                print('<',end='')
            elif (j,i) in rs:
                print('>',end='')
            elif (j,i) in us:
                print('^',end='')
            elif (j,i) in ds:
                print('v',end='')
            elif (j,i) in walls:
                print('#',end='')
            else:
                print('.',end='')
        print()


done = False
while not done and len(open_positions) > 0:
    print(mins)
    new_open_positions = set()
    left_storms,right_storms,down_storms,up_storms = update_storms(left_storms,right_storms,down_storms,up_storms)
    blocked_pos = walls.union(up_storms).union(down_storms).union(left_storms).union(right_storms)
    for i in open_positions:
        for d in dirs:
            new_pos = (i[0]+d[0],i[1]+d[1])
            if new_pos == ending_pos:
                done = True
                break
            elif new_pos not in blocked_pos:
                new_open_positions.add(new_pos)
        if i not in blocked_pos:
            new_open_positions.add(i)
    # print(new_open_positions)
    # draw_storms(left_storms,right_storms,down_storms,up_storms,walls)
    open_positions = new_open_positions
    mins += 1

print(mins,done)