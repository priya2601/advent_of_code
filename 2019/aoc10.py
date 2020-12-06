" asteroids. find asteroid with path (line of sight) to max asteroids"
import math

def read_input(filename):
    file = open(filename,'r')
    lst = []
    for line in file:
        lst.append(line.strip('\n'))
    return lst

# print(read_input())

def get_direction(x, y):
    if x[0] <= y[0] and x[1] > y[1]:
        return 0
    elif x[0] <= y[0] and x[1] <= y[1]:
        return 1
    elif x[0] > y[0] and x[1] <= y[1]:
        return 2
    else:
        return 3

def calc_slopes(lst):
    max_asteroids = -float('inf')
    best_asteroid = None
    asteroids = []
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '#':
                asteroids.append((j,i))

    a1 = (14, 17)

    slopes = [set(), set(), set(), set()]
    slope_to_point = [dict(),dict(),dict(),dict()]
    for a2 in asteroids:
        direction = 0 #get_direction(a1, a2)
        if a1 != a2:
            slope = math.atan2(a2[1]-a1[1],  (a2[0] - a1[0]))
            slopes[direction].add(slope)
            if slope in slope_to_point:
                slope_to_point[direction][slope].append(a2)
            else:
                slope_to_point[direction][slope] = [a2]

    for slope in slopes:
        print(len(slope))

    print(slope_to_point[0][list(slopes[0])[60]])
    return max_asteroids

def calc_200th(lst):
    asteroids = []
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '#':
                asteroids.append((j,i))


    max_asteroids = -float('inf')
    a1 = (14, 17)

    for a2 in asteroids:
        direction = get_direction(a1, a2)
        if a1 != a2:
            if (a2[0] - a1[0]) == 0:
                slopes[direction].add(10000000)
            else:
                slopes[direction].add((a2[1] - a1[1]) / (a2[0] - a1[0]))

print(calc_slopes(read_input('input_aoc10.txt')))
