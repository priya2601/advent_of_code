# game console


def get_input(filename):
    ins = []
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            op = line.split()[0]
            arg = int(line.split()[1])
            ins.append((op, arg))
    return ins


def get_acc_val(ins):
    executed = set()
    accu = 0
    i = 0
    while i < len(ins):
        if i in executed:
            return i, accu
        executed.add(i)
        if ins[i][0] == 'nop':
            i += 1
        elif ins[i][0] == 'acc':
            accu += ins[i][1]
            i += 1
        elif ins[i][0] == 'jmp':
            i += ins[i][1]
        else:
            raise ValueError('undefined')
    return i, accu


def modify_ins(inst):
    for j in range(len(inst)):
        if inst[j][0] == 'jmp': # jmp to nop
            inst[j] = ('nop', inst[j][1])
            i, accu = get_acc_val(inst)
            if i == len(inst):
                return accu
            else:
                inst[j] = ('jmp', inst[j][1])

        elif inst[j][0] == 'nop': # nop to jmp
            inst[j] = ('jmp', inst[j][1])
            i, accu = get_acc_val(inst)
            if i == len(inst):
                return accu
            else:
                inst[j] = ('nop', inst[j][1])


ins = get_input('aoc8_input.txt')
print(get_acc_val(ins))
print(modify_ins(ins))