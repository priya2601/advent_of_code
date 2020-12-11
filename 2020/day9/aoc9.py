# xmas encryption


def get_input(filename):
    arr = []
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            arr.append(int(line.strip()))
    return arr


def twosum(arr, tgt):
    for i in range(len(arr)):
        val = arr[i]
        if tgt - val in arr[i:]:
            return True


def find_error(arr, pre):
    for i in range(pre, len(arr)):
        if not twosum(arr[i-pre:i], arr[i]):
            return arr[i]


def find_seq(arr, aim):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum(arr[i:j]) == aim:
                return min(arr[i:j])+max(arr[i:j])
    return -1


# arr = get_input('aoc9_sample.txt')
arr = get_input('aoc9_input.txt')
aim = find_error(arr, 25)
print(find_seq(arr, aim))
