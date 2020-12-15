# memory game
import copy
from collections import defaultdict


def find_2020(input):
    arr = defaultdict(list)
    lst = copy.deepcopy(input)
    for i,num in enumerate(input):
        arr[num].append(i+1)
    cur = input[-1]
    idx = len(lst)
    while len(lst) <= 2020:
        if cur in arr.keys():
            if len(arr[cur]) == 1:
                next = 0
            else:
                next = arr[cur][-1] - arr[cur][-2]
        else:
            next = 0
        lst.append(next)
        idx += 1
        arr[next].append(idx)
        cur = next
    return lst[2019]


def find_3m(input):
    prev = defaultdict(int)
    prev_prev = defaultdict(int)
    for i, num in enumerate(input):
        prev[num] = i + 1
    cur = input[-1]
    idx = len(input)
    while idx < 30000000:
        if cur in prev:
            if cur not in prev_prev or prev_prev[cur] == 0:
                next = 0
            else:
                next = prev[cur] - prev_prev[cur]
        else:
            next = 0
        idx += 1
        prev_prev[next] = prev[next]
        prev[next] = idx
        cur = next
    return cur


# print(find_2020([0,3,6]))
# print(find_2020([1,3,2]))
# print(find_2020([3,1,2]))
# print(find_2020([0,3,1,6,7,5]))

# print(find_3m([0,3,6]))
print(find_3m([0,3,1,6,7,5]))

