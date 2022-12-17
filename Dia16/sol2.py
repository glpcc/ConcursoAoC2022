from __future__ import annotations
import re

f = open("input.txt")

lines = [re.findall("(?:Valve )(.*?)(?: has flow rate=)(\d*?)(?:; tunnels? leads? to valves? )(.*)",i)[0] for i in f.readlines()]

class GraphNode():
    def __init__(self,name: str,drain_value: int) -> None:
        self.name = name
        self.drain_value = drain_value
        self.connected_nodes: dict[GraphNode,int] = dict()

    def __hash__(self) -> int:
        return hash(self.name)  
    
    def __repr__(self) -> str:
        return f"GraphNode with name:{self.name} and drain_value:{self.drain_value} "
# Create all the nodes
temp_nodes: dict[str,GraphNode] = {}
for i in lines:
    temp_nodes[i[0]] = GraphNode(i[0],int(i[1]))

# Connect the nodes
for i in lines:
    for j in i[2].split(","):
        tmp = j.strip()
        temp_nodes[i[0]].connected_nodes[temp_nodes[tmp]] = 1
    
def calculate_distances(node1: GraphNode):
    """Calculate the distance from a node to all the non 0 drainage nodes that are connected by 0 drainage nodes"""
    # Dict with Node: distance to it
    open_nodes: list[tuple[GraphNode,int]] = [(node1,0)]
    visited_nodes: set[GraphNode] = set()
    distance = 0
    new_connections: list[tuple[GraphNode,int]] = []
    while len(open_nodes) > 0:
        selected_tuple = open_nodes[0]
        selected_node = selected_tuple[0]
        for next_node in selected_node.connected_nodes:
            if next_node not in visited_nodes:
                if next_node.drain_value > 0 or next_node.name == "AA":
                    distance = selected_tuple[1] + selected_node.connected_nodes[next_node]
                    new_connections.append((next_node,distance))
                    visited_nodes.add(next_node)
                else:
                    open_nodes.append((next_node,selected_tuple[1] + 1))
        visited_nodes.add(selected_node)
        open_nodes = open_nodes[1:]
    for i in new_connections:
        node1.connected_nodes[i[0]] = i[1]

# Leave only nodes with drainage > 0
new_graph: dict[int,dict[int,int]] = {}
for i in temp_nodes:
    if temp_nodes[i].drain_value > 0 or i == 'AA':
        calculate_distances(temp_nodes[i])
        temp_nodes[i].connected_nodes = {j:temp_nodes[i].connected_nodes[j] for j in temp_nodes[i].connected_nodes if j.drain_value>0 or j.name=='AA'}
        new_graph[temp_nodes[i].drain_value] = {j.drain_value:temp_nodes[i].connected_nodes[j] for j in temp_nodes[i].connected_nodes}

print(new_graph)

def distance(node1: int, node2:int):
    open_nodes:  dict[int,int] = {node1:0}
    visited_nodes: set[int] = set()
    distance = -1
    while len(open_nodes) > 0:
        selected_node = min(open_nodes,key= lambda k: open_nodes[k])
        if selected_node == node2:
            return open_nodes[node2]
        for next_node in new_graph[selected_node]:
            if next_node not in visited_nodes:
                if next_node in open_nodes:
                    if open_nodes[selected_node] + new_graph[selected_node][next_node] < open_nodes[next_node]:
                        open_nodes[next_node] = open_nodes[selected_node] + new_graph[selected_node][next_node]
                else:
                    open_nodes[next_node] = open_nodes[selected_node] + new_graph[selected_node][next_node]

        visited_nodes.add(selected_node)
        open_nodes.pop(selected_node)
    return distance


# Precalculate distances
distances = {}
for i in new_graph:
    distances[i] = {}
    for j in new_graph:
        if i != j:
            distances[i][j] = distance(i,j)


def calculate_flow(you_list: list[int],elephant_list: list[int]):
    flow = 0
    minute = 26
    current_pos = 0
    for i in you_list:
        minute = minute-distances[current_pos][i]-1
        if minute == 0:
            break
        flow += minute*i
        current_pos = i

    minute = 26
    current_pos = 0
    for i in elephant_list:
        minute = minute-distances[current_pos][i]-1
        if minute == 0:
            break
        flow += minute*i
        current_pos = i
    
    return flow
    
def calculate_time(l: list[int]):
    minutes = 0
    current_pos = 0
    for i in l:
        minutes += distances[current_pos][i] + 1
        current_pos = i
    return minutes

x = [0]
func_cache = {}
def calculate_max_flow(valves_left: set[int],you_list: list[int],elephant_list: list[int]):
    func_hash = frozenset({tuple(you_list),tuple(elephant_list)})
    if func_hash in func_cache:
        return func_cache[func_hash]
    # x[0] = x[0] + 1
    max_flow = -1
    if len(valves_left) == 0:
        return calculate_flow(you_list,elephant_list)
    you_list_time = calculate_time(you_list)
    elephant_list_time = calculate_time(elephant_list)
    if abs(26-you_list_time) <= 2 and abs(26-elephant_list_time) <= 2:
        return calculate_flow(you_list,elephant_list)

    for i in valves_left:
        if len(valves_left) >= len(new_graph)-2:
            print(len(valves_left))
        new_set = valves_left.difference({i})
        max1 = -1
        if len(you_list)==0 or you_list_time + distances[you_list[-1]][i] + 1 <= 26:
            max1 = calculate_max_flow(new_set,you_list+[i],elephant_list)
        max2 = -1
        if len(elephant_list)==0 or elephant_list_time + distances[elephant_list[-1]][i] + 1 <= 26:
            max2 = calculate_max_flow(new_set,you_list,elephant_list+[i])
        max_flow = max(max_flow,max1,max2)
    func_cache[func_hash] = max_flow
    return max_flow

valves = {i for i in new_graph if i != 0}
valves_to_test = {19, 5, 20, 3, 17, 25, 18, 12}
print(valves)
max_flow = -1
for i in valves_to_test:
    func_cache.clear()
    new_set = valves.difference({i})
    max1 = calculate_max_flow(new_set,[i],[])
    max_flow = max(max_flow,max1)
    print(max_flow)


# Calculated sols
# {15, 22, 23, 24, 9, 6, 10, 19, 5, 20, 3, 17, 25, 18, 12}
# starting 15 2070
# starting 22 2155
# starting 23 2155
# starting 24 2709
# starting 9 2735
# starting 6 2736
# starting 10 2838 # solutiooooooooooooooooon
# starting 19 1964
# starting 9 2735
# starting 6 2736
