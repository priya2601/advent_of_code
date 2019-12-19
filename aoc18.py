
def read_input():
    file = open('input_aoc18.txt','r')
    lst = []
    for line in file:
        ln = line.strip()
        lst.append(ln)
    return lst

def bfs(gridStr):
    grid = {}
    dist = {}
    rows = len(gridStr)
    cols = len(gridStr[0])
    for i in range(rows):
        for j in range(cols):
            grid[(i,j)] = gridStr[i][j]
            dist[(i,j)] = -1
            if grid[(i,j)] == '@':
                x = i
                y = j

    queue = [(x,y)]
    dist[(x,y)] = 0
    while queue:
        curr = queue.pop(0)
        if grid[curr] == '#':
            continue
        for delta in [(-1,0), (1,0), (0,1), (0, -1)]:
            new_point = (curr[0] + delta[0], curr[1] + delta[1])
            if new_point[0] >= rows or new_point[0] < 0 or new_point[1] >= cols or new_point[1] < 0 or dist[new_point] > 0:
                continue
            print(new_point)
            if grid[new_point] == '.' or str.islower(grid[new_point]):
                dist[new_point] = dist[curr] + 1
                print(dist[new_point])
                queue.append(new_point)

            for i in range(rows):
                for j in range(cols):
                    print(dist[(i,j)], end=" ")
                print()


bfs(["#########", "#b.A.@.a#", "#########"])

#print(read_input())