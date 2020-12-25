# math homework


def get_input(file):
    hw = []
    with open(file) as fil:
        lines = fil.readlines()
        for line in lines:
            hw.append(line.strip())
    return hw


def get_order(hw):
    temp = []
    # ops = ['+','*']
    for i in range(len(hw)):
        if hw[i] == '+':
            if i > 0 and hw[i-1] != ')':
                res = int(temp.pop()) + int(hw[i+1])
        elif hw[i] == '*':
            if i > 0 and hw[i-1] != ')':
                res = int(temp.pop()) * int(hw[i + 1])
        elif hw[i] == '(':
            temp.append(hw[i])





hw = get_input('aoc18_sample.txt')