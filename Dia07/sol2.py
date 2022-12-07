from __future__ import annotations

f = open('input.txt')
lines = [i.strip() for i in f.readlines()]

class Directory():
    def __init__(self,name: str, parent_node: Directory | None) -> None:
        self.name = name
        self.child_nodes: dict[str,File | Directory] = dict()
        self.parent_node: Directory = parent_node

class File():
    def __init__(self,name: str, parent_node: Directory, size: int) -> None:
        self.size: int = size
        self.name = name
        self.parent_node = parent_node
    
tree_root = Directory('/',None)

def procces_comand_line(line_indx,current_node: Directory):
    line = lines[line_indx]
    if line[0] == '$':
        command = line[2:4]
        if command == 'cd':
            dir_name = line[5:]
            if dir_name == '/':
                procces_comand_line(line_indx+1,tree_root)
            elif dir_name == '..':
                procces_comand_line(line_indx+1,current_node.parent_node)
            else:
                if not dir_name in current_node.child_nodes:
                    current_node.child_nodes[dir_name] = Directory(dir_name,current_node)
                procces_comand_line(line_indx+1,current_node.child_nodes[dir_name])
        if command == 'ls':
            i = line_indx + 1
            while i < len(lines) and lines[i][0] != '$':
                line = lines[i]
                if line[0:3] == 'dir':
                    dir_name = line[4:]
                    if not dir_name in current_node.child_nodes:
                        current_node.child_nodes[dir_name] = Directory(dir_name,current_node)
                else:
                    file_size, file_name = line.split(' ')
                    current_node.child_nodes[file_name] = File(file_name,current_node,int(file_size))
                i += 1
            if i < len(lines):
                procces_comand_line(i,current_node)
    else:
        print(line_indx)
        print('Hey')

procces_comand_line(0,tree_root)

total_size = 0
dir_sizes = []
def calculate_size(direc: Directory):
    dir_size = 0
    for i in direc.child_nodes:
        if type(direc.child_nodes[i]) == Directory:
            dir_size += calculate_size(direc.child_nodes[i])
        else:
            dir_size += direc.child_nodes[i].size
    print(direc.name,dir_size)
    dir_sizes.append(dir_size)
    return dir_size

calculate_size(tree_root)
sorted_sizes = sorted(dir_sizes)
print(sorted_sizes)
needed_space = 30000000 - (70000000 - sorted_sizes[-1])
for i in sorted_sizes:
    if i >= needed_space:
        print(i)
        break




