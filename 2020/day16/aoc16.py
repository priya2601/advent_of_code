# invalid tickets
import copy
from collections import defaultdict


def get_input(file):
    tkt = []
    others = []
    rules = defaultdict(list)
    with open(file) as fil:
        lines = fil.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if line.startswith('your ticket:'):
                tkt.extend([int(t) for t in lines[i+1].split(',')])
            elif line.startswith('nearby tickets:'):
                j = copy.deepcopy(i)
                while j < len(lines)-1:
                    others.append([int(t) for t in lines[j+1].split(',')])
                    j += 1
            elif 'or' in line:
                name = line.split(':')[0]
                range1 = line.split(': ')[1].split(' or ')[0]
                range11 = int(range1.split('-')[0])
                range12 = int(range1.split('-')[1])
                range2 = line.split(': ')[1].split(' or ')[1]
                range21 = int(range2.split('-')[0])
                range22 = int(range2.split('-')[1])
                vall = []
                vall.extend([i for i in range(range11, range12+1)])
                vall.extend([i for i in range(range21, range22+1)])
                rules[name].append(vall)
    return tkt, others, rules


def get_invalids(others, rules):
    total = 0
    for num in others:
        if num not in rules:
            total += num
    return total


# print(get_input('aoc16_sample.txt'))
tkt, rules, valid = get_input('aoc16_input.txt')
print(get_invalids(others, rules))

