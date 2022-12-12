f = open('input.txt')

lines = [i.strip() for i in f.readlines()]

starting_pos = (0,0)
ending_pos = (0,0)
height_map = [[] for _ in range(len(lines))]

for j in range(len(lines)):
    for i in range(len(lines[j])):
        if lines[j][i] == 'S':
            starting_pos = (j,i)
            height_map[j].append(1)
        elif lines[j][i] == 'E':
            ending_pos = (j,i)
            height_map[j].append(26)
        else:
            height_map[j].append(ord(lines[j][i])-ord('a')+1)

# Use the A* Algorith to get the shortests path
class pos_helper():
    def __init__(self,x_pos,y_pos,path_value) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.path_value = path_value
        self.heuristic = 0
    
    def calculate_heuristic(self,other_x,other_y) -> int:
        return abs(other_x - self.x_pos)+abs(self.y_pos - other_y)
    

open_pos: dict[tuple[int,int],pos_helper] = {starting_pos:pos_helper(starting_pos[0],starting_pos[1],0)}
DIRS = [(1,0),(-1,0),(0,1),(0,-1)]
print(starting_pos)
print(ending_pos)
visited_pos: set[tuple[int,int]] = set()
found = False
while not found:
    next_pos = min(open_pos,key= lambda k: open_pos[k].heuristic + open_pos[k].path_value)
    # print("Open Pos:")
    # for i in open_pos:
    #     print(i, end=" ")
    # print()
    for dir in DIRS:
        try:
            if next_pos[0]+dir[0] < 0 or next_pos[1]+dir[1] < 0:
                continue
            if height_map[next_pos[0]+dir[0]][next_pos[1]+dir[1]] - height_map[next_pos[0]][next_pos[1]] <= 1:
                new_pos = (next_pos[0]+dir[0],next_pos[1]+dir[1])
                if new_pos in visited_pos:
                    continue
                if new_pos == ending_pos:
                    found = True
                    print(open_pos[next_pos].path_value + 1)
                    break
                elif (new_pos in open_pos) and open_pos[next_pos].path_value + 1 < open_pos[new_pos].path_value:
                    open_pos[new_pos].path_value = open_pos[next_pos].path_value + 1
                else:
                    open_pos[new_pos] = pos_helper(new_pos[0],new_pos[1],open_pos[next_pos].path_value + 1)
                    open_pos[new_pos].heuristic = open_pos[new_pos].calculate_heuristic(ending_pos[0],ending_pos[1])
        except IndexError:
            continue
    visited_pos.add(next_pos)
    open_pos.pop(next_pos)
    if len(open_pos) == 0:
        found = True
