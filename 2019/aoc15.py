" Oxygen tank repair droid min steps"

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
    file = open('input_aoc15.txt', 'r')
    lst = []
    for line in file:
        lst.append(line)
    lst = str.split(lst[0], ',')
    intlist = []
    for l in lst:
        intlist.append(int(l))
    return intlist

def count_steps(prog):
    NORTH = (0,1)
    EAST = (1,0)
    WEST  = (-1,0)
    SOUTH = (0,-1)
    direction = [NORTH, SOUTH, WEST, EAST]

    input = []
    output = []
    intcode = Intcode(prog, input, output)
    curr_pos = (0, 0)
    curr_dir = 0
    directions_at_wall = dict()
    room = dict()
    while True:
        input.append(curr_dir+1)
        intcode.exec()
        # print(output)
        next_pos = (curr_pos[0]+direction[curr_dir][0], curr_pos[1]+direction[curr_dir][1])
        if output[0] == 0 or output[0] == 1:
            list = [0,1,2,3]
            random.shuffle(list)
            if next_pos in directions_at_wall:
                if len(directions_at_wall[next_pos]) == 0:
                    raise ValueError("Exhausted directions")
#                    directions_at_wall[next_pos] = list
                curr_dir = directions_at_wall[next_pos].pop(0)
            else:
                directions_at_wall[next_pos] = list
        if output[0] == 0:
            room[next_pos]  = '#'
        elif output[0] == 1:
            room[next_pos] = '.'
            curr_pos = next_pos
        elif output[0] == 2:
            room[next_pos] = 'o'
            curr_pos = next_pos
            print_room(room)
            return(room)
        output.pop(0)
        print_room(room)
    return(room)

def print_room(tiles):
    print("room")
    tiles[(0,0)] = 'D'
    for j in range(min([ x[1] for x in tiles.keys() ]), max([ x[1] for x in tiles.keys() ])+1):
        for i in range(min([ x[0] for x in tiles.keys()]),max([ x[0] for x in tiles.keys()])+1):
            if (i,j) in tiles.keys():
                print(tiles[(i,j)],end="")
            else:
                print(' ',end="")
        print()


print(count_steps(read_input()))