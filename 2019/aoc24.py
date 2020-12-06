" Game of life - Eris bugs "

def read_input():
    file = open('input_aoc24.txt', 'r')
    lst = []
    for line in file:
        lst.append([i for i in line.strip('\n')])
    return lst

def get_next(grid,i,j):
    bugs = 0
    if j+1 < len(grid[0]) and grid[i][j+1] == '#':
        bugs += 1
    if i+1 < len(grid) and grid[i+1][j] == '#':
        bugs += 1
    if i-1 >= 0 and grid[i-1][j] == '#':
        bugs += 1
    if j-1 >= 0 and grid[i][j-1] == '#':
        bugs += 1
    if grid[i][j] == '.':
        if (bugs == 1 or bugs == 2):
            return '#'
        else:
            return '.'
    elif grid[i][j] == '#':
        if bugs == 1:
            return '#'
        else:
            return '.'




def update_grid(grid):
    next_grid = [[0]*len(grid[0]) for i in range(len(grid))]
    prev_bio_rating = set()
    while True:
        bio_rating = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                next_grid[i][j] = get_next(grid,i,j)
                print(next_grid[i][j],end = "")
                if next_grid[i][j] == '#':
                    bio_rating += 2**(i*len(grid[0])+j)
            print()
        print(bio_rating)
        if bio_rating in prev_bio_rating:
            return bio_rating
        prev_bio_rating.add(bio_rating)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = next_grid[i][j]
    return None


print(update_grid(read_input()))