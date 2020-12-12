# adapter arrangement
from collections import defaultdict

def get_input(filename):
    arr = [0]
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            arr.append(int(line.strip()))
        arr.append(max(arr)+3)

    return arr


def get_diff(arr):
    adaps = sorted(arr)
    diff = defaultdict(int)
    for j in range(1, len(adaps)):
        key = adaps[j] - adaps[j-1]
        if key <= 3:
            diff[key] += 1
    print(diff)
    return diff[1]*diff[3]


def get_arrangements(arr):
    adaps = sorted(arr)
    print(adaps)
    ways = defaultdict(int)
    ways[0] = 1
    ways[1] = 1 if 1 in adaps else 0
    ways[2] = (ways[1] + ways[0]) if 2 in adaps else 0
    for i in range(1, max(adaps)+1):
        ways[i] = 0 if i not in adaps else (ways[i-3]+ways[i-2]+ways[i-1])
    print(ways)
    return ways[max(adaps)]


arr = get_input('aoc10_input.txt')
# print(get_diff(arr))
print(get_arrangements(arr))