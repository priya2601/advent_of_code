# grid. count trees


def get_input(filename):
    grid = []
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            grid.append(line.strip())
    return grid


def count_trees(grid, right, down):
    trees = 0
    i = 0
    j = 0
    gridlen = len(grid[0])
    while j < len(grid):
        if grid[j][i % gridlen] == '#':
            trees += 1
        i += right
        j += down

    return trees


def count_trees_2(grid, slopes):
    output = 1
    for right, down in slopes:
        output *= count_trees(grid, right, down)
    return output


grid = get_input('aoc3_input.txt')
print(count_trees(grid, 3, 1))
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(count_trees_2(grid, slopes))
