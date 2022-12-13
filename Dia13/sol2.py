from __future__ import annotations

f = open("input.txt")
lines = [i.strip() for i in f.readlines() if i != '\n']

# Returns 1 if in order 0 to continue and -1 if not in order
def is_in_order(l1: list, l2: list)-> int:
    for i in range(len(l1)):
        if i >= len(l2):
            return -1
        elif type(l1[i]) == list and type(l2[i]) == list:
            order = is_in_order(l1[i],l2[i])
            if order != 0:
                return order
        elif type(l1[i]) == int and type(l2[i]) == int:
            if l1[i] < l2[i]:
                return 1
            elif l1[i] > l2[i]:
                return -1
        elif type(l1[i]) == list and type(l2[i]) == int:
            order = is_in_order(l1[i],[l2[i]])
            if order != 0:
                return order
        elif type(l1[i]) == int and type(l2[i]) == list:
            order = is_in_order([l1[i]],l2[i])
            if order != 0:
                return order
    if len(l1) < len(l2):
        return 1
    return 0


def process_line(bracket_pairs: dict, line: str,starting_i: int) -> list:
    current_list = []
    i = 0
    while i < len(line):
        match line[i]:
            case '[':
                current_list.append(process_line(bracket_pairs,line[i+1:bracket_pairs[starting_i+i]-starting_i],starting_i+i+1))
                i = bracket_pairs[starting_i+i]-starting_i
            case ']':
                raise ValueError('This shouldnt happen')
            case '1':
                if i + 1 < len(line) and line[i+1] == '0':
                    current_list.append(10)
                    i += 1
                else:
                    current_list.append(1)
            case ',':
                ...
            case other:
                current_list.append(int(other))
        i += 1
    return current_list


processed_lists = []
# Get the indices of matching brackets
for line in lines:
    opening_brackets_pos = []
    brackets_pairs = dict()
    for i in range(len(line)):
        if line[i] == '[':
            opening_brackets_pos.append(i)
        elif line[i] == ']':
            brackets_pairs[opening_brackets_pos[-1]] = i
            opening_brackets_pos.pop()
    processed_lists.append(process_line(brackets_pairs,line,0)) 

class CustomList():
    def __init__(self, list:list) -> None:
        self.list = list
    
    def __lt__(self,other: CustomList):
        order = is_in_order(self.list,other.list)
        if order == 1:
            return True
        elif order == -1:
            return False
    
    def __gt__(self,other: CustomList):
        order = is_in_order(self.list,other.list)
        if order == 1:
            return False
        elif order == -1:
            return True
    
    def __eq__(self, other: CustomList) -> bool:
        return self.list == other.list
    
    def __repr__(self) -> str:
        return str(self.list)

processed_lists.append([[2]])
processed_lists.append([[6]])
# Sort the lists 
sorted_list = sorted([CustomList(i) for i in processed_lists])
result = 0
for i in range(len(sorted_list)):
    if sorted_list[i].list == [[2]]:
        result = i+1
    elif sorted_list[i].list == [[6]]:
        result *= i+1

print(result)
                