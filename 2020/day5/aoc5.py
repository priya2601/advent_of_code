# boarding pass
import re


def get_input(filename):
    passes = []
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            passes.append(line.strip())
    return passes


def convert(board):
    binstr = ''
    for chr in board:
        if chr == 'F' or chr == 'L':
            binstr += '0'
        else:
            binstr += '1'
    return(int(binstr,2))


def max_seat_id(passes):
    max = 0
    for board in passes:
        seat = convert(board)
        if seat > max:
            max = seat
    return max


def min_seat_id(passes):
    min = 891
    for board in passes:
        seat = convert(board)
        if seat < min:
            min = seat
    return min


def missing_seat(passes):
    ids = [x for x in range(85,890)]
    all_ids = []
    for board in passes:
        all_ids.append(convert(board))
    all_ids.sort()
    print(all_ids)
    for i in range(len(ids)):
        if all_ids[i] != ids[i]:
            return ids[i]


passes = get_input('aoc5_input.txt')
print(max_seat_id(passes))
print(missing_seat(passes))

