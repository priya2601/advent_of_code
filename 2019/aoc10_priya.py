" asteroids. find asteroid with path (line of sight) to max asteroids"

def read_input(filename):
    file = open(filename,'r')
    lst = []
    for line in file:
        lst.append(line.strip('\n'))
    return lst

# print(read_input())

def calc_slopes(lst):
    max_asteroids = -float('inf')
    asteroids = []
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '#':
                asteroids.append((j,i))
    for a1 in asteroids:
        slopes = set()
        for a2 in asteroids:
            if a1 != a2:
                if (a2[0] - a1[0]) == 0:
                    slopes.add(10000000)
                else:
                    slopes.add((a2[1]-a1[1]) / (a2[0] - a1[0]))
        if len(slopes) > max_asteroids:
            max_asteroids = len(slopes)
    return max_asteroids

print(calc_slopes(read_input('input_aoc10a.txt')))
