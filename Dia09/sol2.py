f = open('input.txt')

movements = [i.strip().split(' ') for i in f.readlines()]
movements = [(i[0],int(i[1])) for i in movements]

def sum_pos(a: tuple[int,int], b: tuple[int,int])-> tuple[int,int]:
    return (a[0]+b[0],a[1]+b[1])

def calculate_distance(a: tuple[int,int], b: tuple[int,int]) -> int:
    # Check if is diagonal and then overite distance to 1 to mean it is touching
    if (abs(a[0]-b[0]) == 1 and abs(a[1]-b[1]) == 1):
        return 1
    else:
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
dirrections = {
    'L': (-1,0),
    'R': (1,0),
    'D': (0,-1),
    'U': (0,1)
}


head_pos = (0,0)
knots_pos: list[tuple[int,int]] = [(0,0) for i in range(9)]
visited_pos = {knots_pos[-1]}

for dir,amount in movements:
    for _ in range(amount):
        head_pos = sum_pos(head_pos,dirrections[dir])
        prev_knot = head_pos
        for i in range(9):
            distance = calculate_distance(prev_knot,knots_pos[i])
            if distance == 2 or distance == 4:
                vertical_dist = knots_pos[i][1] - prev_knot[1]
                horizontal_dist = knots_pos[i][0] - prev_knot[0]
                knots_pos[i] = sum_pos(knots_pos[i],(-horizontal_dist//2,-vertical_dist//2))
            elif distance == 3:
                # Check the direction to move diagonally if the diference of coordinates is 2 means the longer distance is in that coordinate
                vertical_dist = knots_pos[i][1] - prev_knot[1]
                horizontal_dist = knots_pos[i][0] - prev_knot[0]
                # Head is down
                if vertical_dist == 2:
                    knots_pos[i] = sum_pos(knots_pos[i],(-horizontal_dist,-1))
                # Head is up
                elif vertical_dist == -2:
                    knots_pos[i] = sum_pos(knots_pos[i],(-horizontal_dist,1))
                # Head is left
                elif horizontal_dist == 2:
                    knots_pos[i] = sum_pos(knots_pos[i],(-1,-vertical_dist))
                # Head is right
                elif horizontal_dist == -2:
                    knots_pos[i] = sum_pos(knots_pos[i],(1,-vertical_dist))

            prev_knot = knots_pos[i]
        visited_pos.add(knots_pos[-1])
#     print(knots_pos)
# print(visited_pos)
print(len(visited_pos))



