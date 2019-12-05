" two more opcodes. position mode and immediate mode."

def exec(prog):
    i = 0
    input = 5
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
            prog[prog[i+1]] = input
            i += 2
        elif opcode == 4:
            print(param1)
            i += 2
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
    return

def read_input():
    file = open('input_aoc5.txt','r')
    lst = []
    for line in file:
        lst.append(line)
    lst = str.split(lst[0], ',')
    intlist = []
    for l in lst:
        intlist.append(int(l))
    return intlist


# print(exec([1002,4,3,4,33]))
#
# print(exec([1101,100,-1,4,0]))

print(exec(read_input()))

# print(exec([3,9,8,9,10,9,4,9,99,-1,8]))

# print(exec([3,3,1108,-1,8,3,4,3,99]))

# print(exec([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]))

# print(exec([3,3,1105,-1,9,1101,0,0,12,4,12,99,1]))

# print(exec([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]))