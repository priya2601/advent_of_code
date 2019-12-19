" Tractor beam count pounds "

from itertools import permutations
import random


class Intcode:
    def __init__(self, prog, input, output):
        self.prog = prog.copy()
        self.prog.extend([0]*100000)
        self.input = input
        self.output = output
        self.i = 0
        self.base = 0

    def get_param(self,mode,index):
        if mode == 0:
            return self.prog[self.prog[index]]
        elif mode == 1:
            return self.prog[index]
        else:
            return self.prog[self.prog[index] + self.base]


    def exec(self):
        """Returns true if the self.program has halted, continues running
        the self.program till it finds a load and no input and returns false"""
        while self.i < len(self.prog):
            opcode = self.prog[self.i] % 100
            if opcode == 99:
                return True
            mode_first = (self.prog[self.i] // 100) % 10
            mode_second = (self.prog[self.i] // 1000) % 10
            mode_third = (self.prog[self.i] // 10000) % 10
            param1 = self.get_param(mode_first,self.i+1)
            if opcode in [7,8,1,2]:
                if mode_third == 0:
                    index_third = self.prog[self.i + 3]
                elif mode_third == 2:
                    index_third = self.prog[self.i + 3] + self.base
            if opcode != 3 and opcode != 4 and opcode != 9:
                param2 = self.get_param(mode_second,self.i+2)
            if opcode == 1:
                self.prog[index_third] = param1 + param2
                self.i += 4
            elif opcode == 2:
                self.prog[index_third] = param1 * param2
                self.i += 4
            elif opcode == 3:
                if len(self.input) == 0:
                    return False
                if mode_first == 0:
                    self.prog[self.prog[self.i + 1]] = self.input.pop(0)
                elif mode_first == 2:
                    self.prog[self.prog[self.i + 1] + self.base] = self.input.pop(0)
                self.i += 2
            elif opcode == 4:
                # print(param1)
                self.i += 2
                self.output.append(param1)
            elif opcode == 5:
                if param1 != 0:
                    self.i = param2
                else:
                    self.i += 3
            elif opcode == 6:
                if param1 == 0:
                    self.i = param2
                else:
                    self.i += 3
            elif opcode == 7:
                if param1 < param2:
                    self.prog[index_third] = 1
                else:
                    self.prog[index_third] = 0
                self.i += 4
            elif opcode == 8:
                if param1 == param2:
                    self.prog[index_third] = 1
                else:
                    self.prog[index_third] = 0
                self.i += 4
            elif opcode == 9:
                self.base += param1
                self.i += 2
            else:
                print("unknown opcode", opcode)
        # print(self.prog)
        print("Error: reached end of program without halt instruction")
        return True

def read_input():
    file = open('input_aoc19.txt','r')
    lst = []
    for line in file:
        lst.append(line)
    lst = str.split(lst[0], ',')
    intlist = []
    for l in lst:
        intlist.append(int(l))
    return intlist

def fill(prog, i, j, grid):
    input = []
    output = []
    intcode = Intcode(prog, input, output)
    input.append(i)
    input.append(j)

    intcode.exec()
    if output.pop() == 0:
        grid[i][j] = '.'
        return False
    else:
        grid[i][j] = '#'
        return True

def dense_points(prog, x, y, size):
    n = 50
    grid = {}
    for i in range(x, x+size):
        grid[i] = {}
        for j in range(y, y+size):
            fill(prog, i, j, grid)
    return grid

def sparse_points(prog):
    n = 5000
    grid = {}
    points = 0
    left_pound = 8
    right_pound = 8
    for i in range(8,n):
        grid[i] = {}
        if fill(prog, i, left_pound, grid):
            pass
        elif fill(prog, i, left_pound+1, grid):
            left_pound += 1
        elif fill(prog, i, left_pound + 2, grid):
            left_pound += 2
        else:
            print("Could not find left pound")

        right_pound = max(left_pound, right_pound)
        while fill(prog, i, right_pound, grid):
            right_pound += 1
        for k in range(left_pound, right_pound):
            grid[i][k] = '#'

    L = 100
    for i in range(8, n):
        for j in range(n):
            if check(grid, i, j) and check(grid, i+L, j) and check(grid, i, j+L) and check(grid, i+L, j+L):
                print("Found: ", i, j)
                return

    return grid

def check(grid, i, j):
    if not i in grid.keys() or not j in grid[i].keys():
        return False
    return grid[i][j] == '#'

def print_grid(grid, x, y, size):
    for i in range(x, x+size):
        for j in range(y, y+size):
            if j in grid[i].keys():
                print(grid[i][j], end="")
            else:
                print(' ', end="")
        print()

sparse_points(read_input())
#print_grid(dense_points(read_input(), 1843, 2001, 100), 1843, 2001, 100)


