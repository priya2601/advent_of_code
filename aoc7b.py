" Amplifier Circuit. position mode and immediate mode. Guest author "
from itertools import permutations

class Amplifier:
    def __init__(self, prog, input, output):
        self.prog = prog.copy()
        self.input = input
        self.output = output
        self.i = 0
    
    def exec(self):
        """Returns true if the self.program has halted, continues running 
        the self.program till it finds a load and no input and returns false"""
        while self.i < len(self.prog):
            opcode = self.prog[self.i]%100
            if opcode == 99:
                return True
            mode_first = (self.prog[self.i]//100)%10
            mode_second = (self.prog[self.i]//1000)%10
            param1 = self.prog[self.prog[self.i + 1]] if mode_first == 0 else self.prog[self.i + 1]
            if opcode != 3 and opcode != 4:
                param2 = self.prog[self.prog[self.i + 2]] if mode_second == 0 else self.prog[self.i + 2]
            if opcode == 1:
                self.prog[self.prog[self.i+3]] = param1 + param2
                self.i += 4
            elif opcode == 2:
                self.prog[self.prog[self.i + 3]] = param1 * param2
                self.i += 4
            elif opcode == 3:
                if len(self.input) == 0:
                    return False
                self.prog[self.prog[self.i+1]] = self.input.pop(0)
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
                    self.prog[self.prog[self.i+3]] = 1
                else:
                    self.prog[self.prog[self.i + 3]] = 0
                self.i += 4
            elif opcode == 8:
                if param1 == param2:
                    self.prog[self.prog[self.i + 3]] = 1
                else:
                    self.prog[self.prog[self.i + 3]] = 0
                self.i += 4
            else:
                print("unknown opcode",opcode)
        # print(self.prog)
        print("Error: reached end of program without halt instruction")
        return True

def read_input():
    file = open('input_aoc7.txt','r')
    lst = []
    for line in file:
        lst.append(line)
    lst = str.split(lst[0], ',')
    intlist = []
    for l in lst:
        intlist.append(int(l))
    return intlist

def calc_feedback(prog, phase):
    amps = []
    channels = []
    channels.append([phase[0], 0])
    for i in range(5):
        if i < 4:
            channels.append([phase[i+1]])
        amps.append(Amplifier(prog, channels[i], channels[(i+1) % 5]))
    print(channels)

    all_halted = False
    while not all_halted:
        all_halted = True
        for amp in amps:
            halted = amp.exec()
            if not halted:
                all_halted = False

    return channels[0][0]

def calc_max_feedback(prog):
    phases = permutations(range(5, 10))
    max_signal = -3500000
    for phase in phases:
        signal = calc_feedback(prog, phase)
        if signal > max_signal:
            max_signal = signal
    return max_signal


# print(calc_max_feedback([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
# 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]))

# print(calc_max_feedback([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]))

print(calc_max_feedback(read_input()))
