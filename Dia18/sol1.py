f = open("input.txt")

positions = {tuple([int(i) for i in x.strip().split(',')]) for x in f.readlines()}

surface_area = 0
posible_sides = [[0,0,0] for i in range(6)]
for i in range(6):
    posible_sides[i][i//2] = 1 if i%2 == 0 else -1

def sum_lists(a,b):
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

for i in positions:
    for j in posible_sides:
        if sum_lists(i,j) not in positions:
            surface_area += 1

print(surface_area)