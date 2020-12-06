" built hull painting robot"

from itertools import permutations


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
                print(param1)
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
    file = open('input_aoc11.txt', 'r')
    lst = []
    for line in file:
        lst.append(line)
    lst = str.split(lst[0], ',')
    intlist = []
    for l in lst:
        intlist.append(int(l))
    return intlist

UP = (0,1)
DOWN = (0,-1)
LEFT = (-1,0)
RIGHT = (1,0)
directions = [UP,LEFT,DOWN,RIGHT]

def count_panels(prog):
    input = [1]
    output = []
    intcode = Intcode(prog, input, output)
    hull = dict()
    x = 0
    y = 0
    direction = UP
    while not intcode.exec():
        if len(output) != 2:
            raise ValueError("output not 2")
        hull[(x,y)] = output[0]
        if output[1] == 0:
            direction = directions[(directions.index(direction)+1) % 4]
        else:
            direction = directions[(directions.index(direction) - 1) % 4]
        x += direction[0]
        y += direction[1]
        input.append(hull.get((x,y),0))
        output[:] = []
    min_x = min([x[0] for x in hull.keys()])
    max_x = max([x[0] for x in hull.keys()])
    min_y = min([x[1] for x in hull.keys()])
    max_y = max([x[1] for x in hull.keys()])

    for j in range(min_y, max_y + 1):
        for i in range(min_x,max_x+1):
            print(hull.get((i,j),0),' ',end="")
        print()
    return len(hull)

print(count_panels(read_input()))


