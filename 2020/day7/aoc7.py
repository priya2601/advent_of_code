# luggage rules
from collections import defaultdict


def get_input(filename):
    rules = {}
    rev_rules = defaultdict(list)
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            key = line.split(' bags contain ')[0]
            contains = line.split(' bags contain ')[1].split(',')
            contain_list = []
            for ele in contains:
                ele = ele.strip()
                if any(char.isdigit() for char in ele):
                    contain_list.append((ele[0], ele[2:].split(' bag')[0]))
                    rev_rules[ele[2:].split(' bag')[0]].append(key)
            rules[key] = contain_list
    return rules, rev_rules


def dfs(bag, rev_rules, visited):
    if bag in visited:
        return
    visited.add(bag)
    for node in rev_rules[bag]:
        dfs(node, rev_rules, visited)


def count_container_bags(rev_rules):
    visited = set()
    dfs('shiny gold', rev_rules, visited)
    print(visited)
    return len(visited)-1


def dfs_2(bag, rules):
    total = 1
    if bag not in rules:
        return 1
    for ele in rules[bag]:
        total = total + (int(ele[0]) * dfs_2(ele[1], rules))
        print(ele[0], ele[1])
    return total


def count_bags_inside(rules):
    return dfs_2('shiny gold', rules)-1



# rules, rev_rules = get_input('aoc7_sample.txt')
# rules, rev_rules = get_input('aoc7_sample2.txt')
rules, rev_rules = get_input('aoc7_input.txt')

# print(rules, rev_rules)
# print(count_container_bags(rev_rules))
print(count_bags_inside(rules))