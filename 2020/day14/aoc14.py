# bitmask
import itertools


def get_program(file):
    with open(file) as fil:
        lines = fil.readlines()
        return lines


def execute_prog(prog):
    mem = {}
    for line in prog:
        if line.startswith('mask'):
            msk = line.split('= ')[1].strip()
            msk_bin_or = ['0' if t == 'X' else t for t in msk]
            msk_bin_and = ['1' if t == 'X' else t for t in msk]
            msk_bin_or = int(''.join(msk_bin_or), 2)
            msk_bin_and = int(''.join(msk_bin_and), 2)
        else:
            locc = int(line.split('[')[1].split(']')[0])
            val = int(line.split('= ')[1])
            result = msk_bin_and & val
            result = result | msk_bin_or
            print(msk_bin_or, msk_bin_and, val, mem)
            mem[locc] = result
    return sum(mem.values())


def execute_prog2(prog):
    mem = {}
    for line in prog:
        if line.startswith('mask'):
            msk = line.split('= ')[1].strip()
            msk_bin_or = int(''.join(['0' if t == 'X' else t for t in msk]), 2)
            num_x = 0
            for t in msk:
                if t == 'X':
                    num_x += 1
        else:
            locc = int(line.split('[')[1].split(']')[0])
            val = int(line.split('= ')[1])
            result = msk_bin_or | locc
            result = bin(result)[2:].zfill(36)
            x_lst = [pos for pos, char in enumerate(msk) if char == 'X']   # find x positions
            result_x = ''
            for k, chr in enumerate(result):
                if k in x_lst:
                    result_x += 'X'
                else:
                    result_x += chr
            lst = list(map(list, itertools.product([0, 1], repeat=num_x)))
            for i in range(len(lst)):
                add = result_x
                for j in range(len(lst[0])):
                    add = add.replace('X', str(lst[i][j]), 1)
                mem[int(add, 2)] = val
    return sum(mem.values())


prog = get_program('aoc14_input.txt')
print(execute_prog2(prog))