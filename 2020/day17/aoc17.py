# Conway cubes


def get_grid(file):
    grid = []
    with open(file) as fil:
        lines = fil.readlines()
        for line in lines:
            grid.append(line.strip())
    return grid


def simulate(grid):
    cube = defaultdict()
    return


