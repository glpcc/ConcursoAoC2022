f = open("input.txt")
lines = [i.strip() for i in f.readlines() if i != '\n']

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
# Compare the lists 
total_sum = 0
for i in range(0,len(processed_lists),2):
    packet1 = processed_lists[i]
    packet2 = processed_lists[i+1]
    order = is_in_order(packet1,packet2)
    if order == 1:
        total_sum += i/2 + 1
print(total_sum)

                