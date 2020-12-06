# program 4 positions

def exec(prog):
    i = 0
    while i < len(prog):
        opcode = prog[i]
        if opcode == 1:
            prog[prog[i+3]] = prog[prog[i+1]] + prog[prog[i+2]]
        elif opcode == 2:
            prog[prog[i + 3]] = prog[prog[i + 1]] * prog[prog[i + 2]]
        elif opcode == 99:
            break
        else:
            print("unknown opcode",opcode)
        i += 4
    return prog[0]

def read_input():
    file = open('input_aoc2.txt', 'r')

    lst = []
    for line in file:
        lst.append(line)
    lst = str.split(lst[0], ',')
    intlist = []
    for l in lst:
        intlist.append(int(l))
    return intlist

# print(read_input())
#
# print(exec([1,0,0,0,99]))
#
# print(exec([2,3,0,3,99]))
#
# print(exec([1,1,1,4,99,5,6,0,99]))

# print(exec(read_input()))

def find_params():
    for noun in range(100):
        for verb in range(100):
            prog = read_input()
            prog[1] = noun
            prog[2] = verb
            result = exec(prog)
            if result == 19690720:
                return 100*noun + verb
    return -1

print(find_params())