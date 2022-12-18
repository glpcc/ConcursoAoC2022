f = open("input.txt")

wind_dirs = f.readline().strip()
piezes = [
    [(0,0),(1,0),(2,0),(3,0)],
    [(0,1),(1,0),(2,1),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(2,1),(2,2)],
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(0,1),(1,1)],
]

blocked_positions: set[tuple[int,int]] = set()
def calculate_intersection(pos: tuple[int,int],piece: list[tuple[int,int]])-> bool:
    intersect = False
    for x,y in piece:
        new_pos = (pos[0]+x,pos[1]+y)
        if new_pos in blocked_positions:
            intersect = True
            break
        elif new_pos[0] < 0 or new_pos[0] > 6 or new_pos[1] < 0:
            intersect = True
            break
            
    return intersect


def calculate_height(h) -> int:
    top_piece_y = 0
    k = 0
    stoped_positions = []
    for i in range(h):
        current_pieze = piezes[i%len(piezes)]
        pieze_pos = (2,top_piece_y+3)
        stoped = False
        while not stoped:
            # print(pieze_pos,i%len(piezes),k)
            if wind_dirs[k] == '>':
                intersects = calculate_intersection((pieze_pos[0]+1,pieze_pos[1]),current_pieze)
                if not intersects:
                    pieze_pos = (pieze_pos[0]+1,pieze_pos[1])
            elif wind_dirs[k] == '<':
                intersects = calculate_intersection((pieze_pos[0]-1,pieze_pos[1]),current_pieze)
                if not intersects:
                    pieze_pos = (pieze_pos[0]-1,pieze_pos[1])
            if calculate_intersection((pieze_pos[0],pieze_pos[1]-1),current_pieze):
                stoped = True
                for j in current_pieze:
                    if pieze_pos[1]+j[1]+1 > top_piece_y:
                        top_piece_y = pieze_pos[1]+j[1]+1
                    blocked_positions.add((pieze_pos[0]+j[0],pieze_pos[1]+j[1]))
                stoped_positions.append(pieze_pos[0])
                # print("Stoped:",pieze_pos,i%len(piezes),top_piece_y,blocked_positions)
            else:
                pieze_pos = (pieze_pos[0],pieze_pos[1]-1)
            k = (k+1)%len(wind_dirs)

    return top_piece_y

print(calculate_height(2022))