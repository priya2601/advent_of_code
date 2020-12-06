def read_input():
    wires = []
    file = open('input_aoc3.txt', 'r')
    for line in file:
        wires.append(line)
    wire1 = wires[0].split()[0].split(',')
    wire2 = wires[1].split()[0].split(',')
    return wire1,wire2


def calc_points(wire):
    init_pos = (0,0)
    points_covered = []
    sign = []
    for path in wire:
        dir = path[0]
        dist = int(path[1:])
        if dir == 'U':
            sign = (0,1)
        elif dir == 'R':
            sign = (1,0)
        elif dir == 'L':
            sign = (-1,0)
        elif dir == 'D':
            sign = (0,-1)
        else:
            print("unknown direction")
        for i in range(1, dist + 1):
            points_covered.append((init_pos[0] + i*sign[0], init_pos[1] + i*sign[1]))
        init_pos = points_covered[-1]
    return points_covered

def find_closest(wire1,wire2):
    intersection = list(set(calc_points(wire1)) & set(calc_points(wire2)))
    dist_min = 10000000
    for tup in intersection:
        dist = abs(tup[0])+abs(tup[1])
        if dist < dist_min:
            dist_min = dist
    return dist_min

def find_min_delay(wire1,wire2):
    points1 = calc_points(wire1)
    points2 = calc_points(wire2)
    intersection = list(set(points1) & set(points2))
    step_min = 10000000
    for tup in intersection:
        steps = points1.index(tup) + points2.index(tup) + 2
        if steps < step_min:
            step_min = steps
    return step_min


# print(find_closest(['R8','U5','L5','D3'],['U7','R6','D4','L4']))
# print(find_min_delay(['R8','U5','L5','D3'],['U7','R6','D4','L4']))

# print(find_closest(['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']))
print(find_min_delay(['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']))

print(find_closest(*read_input()))
print(find_min_delay(*read_input()))

