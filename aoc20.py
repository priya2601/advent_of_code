" Pluto maze. find shortest path through warps"

def read_input():
    file = open('input_aoc20.txt','r')
    lst = []
    for line in file:
        lst.append(line.strip('\n'))
    return lst

def write_dict(dict,key,value):
    if key in dict.keys():
        dict[key].append(value)
    else:
        dict[key] = [value]


def find_path(maze):
    " start with queue"
    portals = dict()
    rows = len(maze)
    for i in range(rows):
        cols = len(maze[i])
        for j in range(cols):
            if maze[i][j].isalpha():
                if j+1 < cols and maze[i][j+1].isalpha():  #right
                    if j+2 < cols and maze[i][j+2] == '.':  #right
                        write_dict(portals,maze[i][j]+maze[i][j+1],(i,j+2))
                    elif j-1 > 0 and maze[i][j-1] == '.':  #left
                        write_dict(portals,maze[i][j] + maze[i][j+1], (i, j-1))
                elif i+1 < rows and maze[i+1][j].isalpha():  #bottom
                    if i+2 < rows and maze[i+2][j] == '.':  #bottom
                        write_dict(portals, maze[i][j]+maze[i+1][j], (i+2,j))
                    elif i-1 > 0 and maze[i-1][j] == '.':  #above
                        write_dict(portals, maze[i][j] + maze[i+1][j], (i-1, j))
    portal_transfer = dict()
    for value in portals.values():
        if len(value) > 1:
            portal_transfer[value[0]] = value[1]
            portal_transfer[value[1]] = value[0]
    print(portal_transfer)

    queue = [portals['AA'][0]]
    dist = dict()
    dist[portals['AA'][0]] = 0
    visited = set()
    while queue:
        curr = queue.pop(0)
        if curr in visited:
            continue
        else:
            visited.add(curr)
        for delta in [(0,1),(-1,0),(0,-1),(1,0)]:
            neighbor = (curr[0]+delta[0],curr[1]+delta[1])
            if maze[neighbor[0]][neighbor[1]] == '.':
                dist[neighbor] = dist[curr] + 1
                queue.append(neighbor)
        if curr in portal_transfer:
            dist[portal_transfer[curr]] = dist[curr] + 1
            queue.append(portal_transfer[curr])
    print(dist[portals['ZZ'][0]])
    return


find_path(read_input())




