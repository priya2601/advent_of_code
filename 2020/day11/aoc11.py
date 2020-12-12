# occupied seats
from collections import defaultdict
import copy


def get_input(filename):
    grid = []
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            ll = []
            for chr in line.strip():
                ll.append(chr)
            grid.append(ll)
    return grid


def count_total_seats(layout):
    seats = 0
    for i in range(len(layout)):
        for j in range(len(layout[0])):
            if layout[i][j] == '#':
                seats += 1
    return seats


# def count_seats(layout, x, y):
#     seats = 0
#     for i in range(x - 1, x + 2):
#         for j in range(y - 1, y + 2):
#             if 0 <= i < len(layout) and 0 <= j < len(layout[0]):
#                 if not (i == x and j == y):
#                     if layout[i][j] == '#':
#                         seats += 1
#     return seats
#
#
# def seat_simulation(grid):
#     layout = copy.deepcopy(grid)
#     next = copy.deepcopy(grid)
#     seat_change = True
#     while seat_change:
#         for i in range(len(layout)):
#             for j in range(len(layout[0])):
#                 if layout[i][j] == '.':
#                     next[i][j] = '.'
#                 if layout[i][j] == 'L':
#                     if count_seats(layout, i, j) == 0:
#                         next[i][j] = '#'
#                 if layout[i][j] == '#':
#                     if count_seats(layout, i, j) >= 4:
#                         next[i][j] = 'L'
#         change = 0
#         for i in range(len(layout)):
#             for j in range(len(layout[0])):
#                 if layout[i][j] == next[i][j]:
#                     change += 1
#         if change == len(layout[0])*len(layout):
#             seat_change = False
#         else:
#             layout = copy.deepcopy(next)
#     return count_total_seats(layout)


def count_seats2(layout, x, y):
    seats = 0
    for id, jd in [(1,0),(-1,0),(0,-1),(0,1),(1,-1),(-1,1),(1,1),(-1,-1)]:
        i = x
        j = y
        for steps in range(max(len(layout[0]), len(layout))):
            i += id
            j += jd
            if not (0 <= i < len(layout) and 0 <= j < len(layout[0])):
                break
            if layout[i][j] == 'L':
                break
            if layout[i][j] == '#':
                seats += 1
                break
    return seats


def seat_simulation2(grid):
    layout = copy.deepcopy(grid)
    next = copy.deepcopy(grid)
    seat_change = True
    while seat_change:
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == '.':
                    next[i][j] = '.'
                if layout[i][j] == 'L':
                    if count_seats2(layout, i, j) == 0:
                        next[i][j] = '#'
                if layout[i][j] == '#':
                    if count_seats2(layout, i, j) >= 5:
                        next[i][j] = 'L'
        # for i in range(len(layout)):
        #     print(''.join(layout[i]))
        # print()
        change = 0
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == next[i][j]:
                    change += 1
        if change == len(layout[0]) * len(layout):
            seat_change = False
        else:
            layout = copy.deepcopy(next)
    return count_total_seats(layout)


# grid = get_input('aoc11_sample.txt')
grid = get_input('aoc11_input.txt')
print(seat_simulation2(grid))