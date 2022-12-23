import re
f = open("input.txt")
lines = [i for i in f.readlines()]
instrucctions = lines[201].strip()
instrucctions = list(re.findall('R|L|\d+',instrucctions))
m = lines[:200]
walls: set[tuple[int,int]] = set()
cube_sides_conecctions:dict[int,list[int]] = {
    1:[2,3,5,6],
    2:[4,3,1,6],
    3:[2,4,5,1],
    4:[2,6,5,3],
    5:[4,6,1,3],
    6:[4,2,1,5]
} 
cube_sides_limits: dict[int,list[int]] = {
    1:[50,0,100,50],
    2:[100,0,150,50],
    3:[50,50,100,100],
    4:[50,100,100,150],
    5:[0,100,50,150],
    6:[0,150,50,200]
}
for i in cube_sides_limits:
    cube_sides_limits[i][2] -= 1
    cube_sides_limits[i][3] -= 1
print(cube_sides_limits)
for i,line in enumerate(m):
    x = 0
    y = i
    for j in line:
        if j == '#':
            walls.add((x,y))
        x += 1


current_pos = (50,0)
current_dir = 0
current_side = 1
directions = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]

def calculate_apearing_pos(current_pos,current_dir,appearing_dir,next_side,current_side):
    if current_dir == 0:
        y_diff = (current_pos[1]-cube_sides_limits[current_side][1])
        if appearing_dir == 2:
            new_pos = (cube_sides_limits[next_side][0],cube_sides_limits[next_side][1] + y_diff)
        elif appearing_dir == 0:
            new_pos = (cube_sides_limits[next_side][2],cube_sides_limits[next_side][3] - y_diff)
        elif appearing_dir == 1:
            new_pos = (cube_sides_limits[next_side][0] + y_diff,cube_sides_limits[next_side][3])
        elif appearing_dir == 3:
            new_pos = (cube_sides_limits[next_side][2] - y_diff,cube_sides_limits[next_side][1])
    elif current_dir == 2:
        y_diff = (current_pos[1]-cube_sides_limits[current_side][1])
        if appearing_dir == 2:
            new_pos = (cube_sides_limits[next_side][0],cube_sides_limits[next_side][3] - y_diff)
        elif appearing_dir == 0:
            new_pos = (cube_sides_limits[next_side][2],cube_sides_limits[next_side][1] + y_diff)
        elif appearing_dir == 1:
            new_pos = (cube_sides_limits[next_side][2] - y_diff,cube_sides_limits[next_side][3])
        elif appearing_dir == 3:
            new_pos = (cube_sides_limits[next_side][0] + y_diff,cube_sides_limits[next_side][1])
    elif current_dir == 1:
        x_diff = (current_pos[0]-cube_sides_limits[current_side][0])
        if appearing_dir == 0:
            new_pos = (cube_sides_limits[next_side][2],cube_sides_limits[next_side][1] + x_diff)
        elif appearing_dir == 3:
            new_pos = (cube_sides_limits[next_side][0]+x_diff,cube_sides_limits[next_side][1])
        else:
            print("Error")
    elif current_dir == 3:
        x_diff = (current_pos[0]-cube_sides_limits[current_side][0])
        if appearing_dir == 2:
            new_pos = (cube_sides_limits[next_side][0],cube_sides_limits[next_side][1] + x_diff)
        elif appearing_dir == 1:
            new_pos = (cube_sides_limits[next_side][0] + x_diff,cube_sides_limits[next_side][3])

    return new_pos

def calculate_following_pos(current_pos,dir,current_side):
    if dir == 0:
        if current_pos[0] + 1 > cube_sides_limits[current_side][2]:
            new_side = cube_sides_conecctions[current_side][0]
            appearing_direction = cube_sides_conecctions[new_side].index(current_side)
            new_dir = (appearing_direction+2)%4
            new_pos = calculate_apearing_pos(current_pos,dir,appearing_direction,new_side,current_side)
            return new_pos,new_dir,new_side
        else:
            new_pos = (current_pos[0] + 1,current_pos[1])
            return new_pos,dir,current_side
    elif dir == 1:
        if current_pos[1] + 1 > cube_sides_limits[current_side][3]:
            new_side = cube_sides_conecctions[current_side][1]
            appearing_direction = cube_sides_conecctions[new_side].index(current_side)
            new_dir = (appearing_direction+2)%4
            new_pos = calculate_apearing_pos(current_pos,dir,appearing_direction,new_side,current_side)
            return new_pos,new_dir,new_side
        else:
            new_pos = (current_pos[0],current_pos[1]+1)
            return new_pos,dir,current_side
    elif dir == 2:
        if current_pos[0] - 1 < cube_sides_limits[current_side][0]:
            new_side = cube_sides_conecctions[current_side][2]
            appearing_direction = cube_sides_conecctions[new_side].index(current_side)
            new_dir = (appearing_direction+2)%4
            new_pos = calculate_apearing_pos(current_pos,dir,appearing_direction,new_side,current_side)
            return new_pos,new_dir,new_side
        else:
            new_pos = (current_pos[0]-1,current_pos[1])
            return new_pos,dir,current_side
    elif dir == 3:
        if current_pos[1]-1 < cube_sides_limits[current_side][1]:
            new_side = cube_sides_conecctions[current_side][3]
            appearing_direction = cube_sides_conecctions[new_side].index(current_side)
            new_dir = (appearing_direction+2)%4
            new_pos = calculate_apearing_pos(current_pos,dir,appearing_direction,new_side,current_side)
            return new_pos,new_dir,new_side
        else:
            new_pos = (current_pos[0],current_pos[1]-1)
            return new_pos,dir,current_side
    
    
for i in instrucctions:
    if i == 'R':
        current_dir = (current_dir+1)%4
    elif i == 'L':
        current_dir = (current_dir-1)%4
    else:
        num = int(i)
        for i in range(num):
            new_pos,new_dir,new_side = calculate_following_pos(current_pos,current_dir,current_side)
            if new_side != current_side:
                print(current_pos,new_pos,current_dir,current_side,new_side)
            if new_pos in walls:
                break
            else:
                current_pos = new_pos
                current_dir = new_dir
                current_side = new_side
print(current_pos)
print((current_pos[1]+1)*1000 + (current_pos[0]+1)*4 + current_dir)
