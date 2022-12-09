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
tail_pos = (0,0)
visited_pos = {tail_pos}

for dir,amount in movements:
    for i in range(amount):
        head_pos = sum_pos(head_pos,dirrections[dir])
        distance = calculate_distance(head_pos,tail_pos)
        if distance == 2:
            tail_pos = sum_pos(tail_pos,dirrections[dir])
            visited_pos.add(tail_pos)
        elif distance == 3:
            # Check the direction to move diagonally if the diference of coordinates is 2 means the longer distance is in that coordinate
            vertical_dist = tail_pos[1] - head_pos[1]
            horizontal_dist = tail_pos[0] - head_pos[0]
            # Head is down
            if vertical_dist == 2:
                tail_pos = sum_pos(tail_pos,(-horizontal_dist,-1))
            # Head is up
            elif vertical_dist == -2:
                tail_pos = sum_pos(tail_pos,(-horizontal_dist,1))
            # Head is left
            elif horizontal_dist == 2:
                tail_pos = sum_pos(tail_pos,(-1,-vertical_dist))
            # Head is right
            elif horizontal_dist == -2:
                tail_pos = sum_pos(tail_pos,(1,-vertical_dist))
            visited_pos.add(tail_pos)
print(len(visited_pos))



