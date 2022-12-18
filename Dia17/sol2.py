f = open("input  .txt")

wind_dirs = f.readline().strip()
piezes = [
    [(0,0),(1,0),(2,0),(3,0)],
    [(0,1),(1,0),(2,1),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(2,1),(2,2)],
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(0,1),(1,1)],
]



def calculate_height(h) -> int:
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
    top_piece_y = 0
    k = 0
    stoped_positions = []
    for i in range(h):
        current_pieze = piezes[i%len(piezes)]
        pieze_pos = (2,top_piece_y+3)
        stoped = False
        repeating = False
        repeating_index = 0
        test_index = 0
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
                stoped_positions.append((pieze_pos[0],i%len(piezes)))
                # print("Stoped:",pieze_pos,i%len(piezes),top_piece_y,blocked_positions)
            else:
                pieze_pos = (pieze_pos[0],pieze_pos[1]-1)
            k = (k+1)%len(wind_dirs)

    # Find patterns in stoped positions
    # for m in range(len(stoped_positions)):
    #     pattern_width = 35
    #     pattern_repetitions = [n for n in range(len(stoped_positions)-pattern_width) if n!=m and stoped_positions[m:m+pattern_width] == stoped_positions[n:n+pattern_width]]
    #     if len(pattern_repetitions) > 0:
    #         print(m,pattern_repetitions)
    # Pretty print the output
    # for m in range(top_piece_y,0,-1):
    #     temp_str = '|'
    #     for n in range(7):
    #         if (n,m) in blocked_positions:
    #             temp_str += "#"
    #         else:
    #             temp_str += '.'
    #     print(temp_str+"|")
    return top_piece_y

a = 1000000000000
b = 1745
num_cycles = (a-55)//b
print(num_cycles)
print((a-55)-(num_cycles*1745))
d = calculate_height(955+55)-calculate_height(55)
print(d)
distance_height = 2778*num_cycles + 80 + d
print(distance_height)

