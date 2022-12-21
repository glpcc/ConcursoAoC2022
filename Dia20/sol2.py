from __future__ import annotations
f = open('input.txt')

l = [int(i.strip())*811589153 for i in f.readlines()]
# print(len(l),len(set(l)))
class LinkedListNode():
    def __init__(self,num) -> None:
        self.num = num
        self.prev_node: LinkedListNode | None = None
        self.next_node: LinkedListNode | None = None

nodes: dict[int,LinkedListNode]= dict()
for i in range(len(l)):
    nodes[i] = LinkedListNode(l[i])

for i in range(len(l)):
    if i != 0:
        nodes[i].prev_node = nodes[i-1]
    if i != len(l)-1:
        nodes[i].next_node = nodes[i+1]

list_first_node = nodes[0]
list_last_node = nodes[len(l)-1]

def find_node(pos_to_move: int,node: LinkedListNode)-> LinkedListNode:
    if pos_to_move >= 0 :
        next_node = node
        for i in range(pos_to_move):
            if next_node.next_node is not None:
                next_node = next_node.next_node
            else:
                next_node = list_first_node
        return next_node
    else:
        next_node = node
        for i in range(-pos_to_move):
            if next_node.prev_node is not None:
                next_node = next_node.prev_node
            else:
                next_node = list_last_node
        return next_node

def print_list(first_node: LinkedListNode):
    next_node = first_node
    while next_node.next_node != None:
        print(f'{next_node.num}', end=' ')
        next_node = next_node.next_node
        
    print(next_node.num, end=' ')
    print()

# print_list(list_first_node)
for _ in range(10):
    for i in range(len(l)):
        node = nodes[i]
        if node.num == 0:
            continue
        if node.num < 0:
            node_to_move = find_node(-1 * (abs(node.num)%(len(l)-1)),node)
        else:
            node_to_move = find_node(node.num%(len(l)-1),node)
        if node == node_to_move:
            continue
        # print(node.num, node_to_move.num)
        # print(list_first_node.num,list_last_node.num)
        if node.prev_node is not None:
            if node.next_node is not None:
                node.prev_node.next_node = node.next_node
                node.next_node.prev_node = node.prev_node
            else:
                list_last_node = node.prev_node
                node.prev_node.next_node = None
        else:
            list_first_node = node.next_node
            node.next_node.prev_node = None

        if node.num > 0:
            if node_to_move.next_node is not None:
                node.next_node = node_to_move.next_node
                node_to_move.next_node.prev_node = node
                node.prev_node = node_to_move
                node_to_move.next_node = node
            else:
                list_first_node.prev_node = node
                node.prev_node = None
                node.next_node = list_first_node
                list_first_node = node
        else:
            if node_to_move.prev_node is not None:
                node.next_node = node_to_move
                node.prev_node = node_to_move.prev_node
                node_to_move.prev_node.next_node = node
                node_to_move.prev_node = node
            else:
                # print_list(list_first_node)
                list_last_node.next_node = node
                node.next_node = None
                node.prev_node = list_last_node
                list_last_node = node
                # print_list(list_first_node)
        # print_list(list_first_node)
    # print_list(list_first_node)
print("Finished_part1")
next_node = list_first_node
while next_node.num != 0:
    next_node = next_node.next_node
print(next_node.num)
print(find_node(6,next_node).num)
print(find_node(1000,next_node).num+find_node(2000,next_node).num+find_node(3000,next_node).num )




