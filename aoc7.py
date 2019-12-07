" Amplifier Circuit. position mode and immediate mode."

from itertools import permutations


def exec(prog,input):
    i = 0
    while i < len(prog):
        opcode = prog[i]%100
        if opcode == 99:
            break
        mode_first = (prog[i]//100)%10
        mode_second = (prog[i]//1000)%10
        param1 = prog[prog[i + 1]] if mode_first == 0 else prog[i + 1]
        if opcode != 3 and opcode != 4:
            param2 = prog[prog[i + 2]] if mode_second == 0 else prog[i + 2]
        if opcode == 1:
            prog[prog[i+3]] = param1 + param2
            i += 4
        elif opcode == 2:
            prog[prog[i + 3]] = param1 * param2
            i += 4
        elif opcode == 3:
            prog[prog[i+1]] = input.pop()
            i += 2
        elif opcode == 4:
            print(param1)
            i += 2
            output = param1
        elif opcode == 5:
            if param1 != 0:
                i = param2
            else:
                i += 3
        elif opcode == 6:
            if param1 == 0:
                i = param2
            else:
                i += 3
        elif opcode == 7:
            if param1 < param2:
                prog[prog[i+3]] = 1
            else:
                prog[prog[i + 3]] = 0
            i += 4
        elif opcode == 8:
            if param1 == param2:
                prog[prog[i + 3]] = 1
            else:
                prog[prog[i + 3]] = 0
            i += 4
        else:
            print("unknown opcode",opcode)
    # print(prog)
    return output

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

def calc_max_signal(prog):
    phases = permutations(range(5))
    max_signal = -3500000
    for phase in phases:
        signal = calc_signal(phase,prog)
        if signal > max_signal:
            max_signal = signal
    return max_signal

def calc_signal(phase,prog):
    input1 = 0
    for amplifier in phase:
        output = exec(prog,[input1, amplifier])
        input1 = output
    return input1


# print(calc_max_signal([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]))

# print(calc_max_signal([3,23,3,24,1002,24,10,24,1002,23,-1,23,
# 101,5,23,23,1,24,23,23,4,23,99,0,0]))

# print(calc_max_signal([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
# 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]))

# print(calc_max_signal(read_input()))

### part two ###

def calc_max_signal2(prog):
    phases = permutations(range(5,10))
    max_signal = -3500000
    for phase in phases:
        signal = calc_signal(phase,prog)
        if signal > max_signal:
            max_signal = signal
    return max_signal

# " function to start a feedback loop"
def calc_signal2(phase,prog):
    """
    :param phase:
    :param prog:
    :return:
    """
    input1 = 0

    for amplifier in phase:
        if i == 5:
            k += 1
        amplifier = phase[i]
        if k == 0:
            output = exec(prog,[input1, amplifier])
        else:
            output = exec(prog, [input1])
        input1 = output
        i += 1
    return input1

