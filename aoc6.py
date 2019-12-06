""" Orbits.. Directed Acyclic Graphs"""

def read_input(filename):
    file = open(filename,'r')
    inputs =[]
    for line in file:
        inputs.append(line.split('\n')[0])
    return inputs

def make_adj_list(inputs):
    graph = dict()
    for input in inputs:
        key = input.split(')')[0]
        val = input.split(')')[1]
        if key not in graph.keys():
            graph[key] = [val]
        else:
            graph[key].append(val)
        if val not in graph.keys():
            graph[val] = [key]
        else:
            graph[val].append(key)
    return graph


def dfs(graph,node,node_depth,depth):
    if node in depth.keys():
        return
    depth[node] = node_depth
    for neighbor in graph[node]:
        dfs(graph,neighbor,node_depth+1,depth)

def calc_total_orbits(filename):
    depth = dict()
    dfs(make_adj_list(read_input(filename)), 'COM', 0, depth)
    return sum(depth.values())

def calc_orbital_transfers(filename):
    depth = dict()
    dfs(make_adj_list(read_input(filename)), 'YOU', 0, depth)
    return depth['SAN']-2




# print(calc_total_orbits('input_aoc6.txt'))

print(calc_orbital_transfers('input_aoc6.txt'))

