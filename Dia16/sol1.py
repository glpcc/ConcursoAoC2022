from __future__ import annotations
import re
from functools import cache
f = open("input2.txt")

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
new_graph: dict[str,GraphNode] = {}
for i in temp_nodes:
    if temp_nodes[i].drain_value > 0 or i == 'AA':
        calculate_distances(temp_nodes[i])
        temp_nodes[i].connected_nodes = {j:temp_nodes[i].connected_nodes[j] for j in temp_nodes[i].connected_nodes if j.drain_value>0 or j.name=='AA'}
        new_graph[temp_nodes[i].name] = temp_nodes[i]

print([new_graph[i].connected_nodes for i in new_graph])
@cache
def calculate_most_flowrate(mins_left: int,opened_nodes: frozenset[GraphNode],current_node: GraphNode):
    if mins_left <= 1:
        return 0
    # elif mins_left == 2:
    #     return current_node.drain_value
    # print(mins_left,opened_nodes,current_node)
    max_flowrate: int = -1
    for i in current_node.connected_nodes:
        # Supose to open the node and then go to that node
        if current_node.name != 'AA' and current_node not in opened_nodes:
            flow_amount1 = current_node.drain_value*(mins_left-1) + calculate_most_flowrate(mins_left-1-current_node.connected_nodes[i],opened_nodes.union({current_node}),i)
        else:
            flow_amount1 = -1
        # Supose you leave
        flow_amount2 = calculate_most_flowrate(mins_left-current_node.connected_nodes[i],opened_nodes,i)
        max_flowrate = max(max_flowrate,flow_amount1,flow_amount2)
    if mins_left == 30:
        print(opened_nodes)
    return max_flowrate

print(calculate_most_flowrate(30,frozenset(),temp_nodes['AA']))
