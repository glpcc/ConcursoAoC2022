f = open("input.txt")

positions = {tuple([int(i) for i in x.strip().split(',')]) for x in f.readlines()}

surface_area = 0
posible_sides = [[0,0,0] for i in range(6)]
for i in range(6):
    posible_sides[i][i//2] = 1 if i%2 == 0 else -1

def sum_lists(a,b):
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

# Cube dimensions 20x20x20
air_positions = set()
open_positions: list[tuple[int,int,int]] = [(0,0,0)]
while len(open_positions) > 0:
    pos = open_positions[0]
    air_positions.add(pos)
    for i in posible_sides:
        new_pos = sum_lists(pos,i)
        if new_pos in positions:
            surface_area += 1
        else:
            if new_pos not in air_positions and all(-2 <= j <= 20 for j in new_pos) and new_pos not in open_positions:
                open_positions.append(new_pos)
    open_positions = open_positions[1:] 


print(surface_area)