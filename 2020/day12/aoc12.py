# ship navigation
import copy


def get_input(filename):
    nav = []
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            dir = line[0]
            amp = int(line[1:].strip())
            nav.append((dir, amp))
    return nav


def find_pos(nav):
    dirs = {'E':(1,0),'W':(-1,0),'N':(0,1),'S':(0,-1)}
    rot = ['E', 'S', 'W', 'N']
    x = 0
    y = 0
    wx = 10
    wy = 1
    for dir, amp in nav:
        if dir == 'L':
            for step in range(amp/90):
                wx, wy = -wy, wx
        if dir == 'R':
            for step in range(amp/90):
                wx, wy = wy, -wx
        if dir == 'F':
            x += wx * amp
            y += wy * amp
        if dir in rot:
            dx, dy = dirs[dir]
            wx += dx * amp
            wy += dy * amp
    return abs(x)+abs(y)


# nav = get_input('aoc12_sample.txt')
nav = get_input('aoc12_input.txt')
print(find_pos(nav))