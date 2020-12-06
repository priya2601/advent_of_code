# twosum and threesum
tgt = 2020


def get_input(filename):
    arr = []
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            arr.append(int(line))
    return arr


def twosum(arr, tgt):
    for i in range(len(arr)):
        val = arr[i]
        if tgt-val in arr[i:]:
            return val*(tgt-val)


arr = get_input("aoc1_input.txt")
print(twosum(arr, tgt))


def threesum(arr, tgt):
    for i in range(len(arr)):
        val1 = arr[i]
        for j in range(len(arr[i:])):
            val2 = arr[j]
            if tgt-val1-val2 in arr[j:]:
                return val1*val2*(tgt-val1-val2)


print(threesum(arr, tgt))
