" Space card shuffle"


def cut(deck,num):
    return deck[num:]+deck[:num]


def deal_increment(deck,increment):
    new_deck = [0] * len(deck)
    for i in range(len(deck)):
        new_deck[(increment*i) % len(deck)] = deck[i]
    return new_deck

def new_stack(deck):
    return deck[::-1]

def read_input():
    file = open('input_aoc22.txt', 'r')
    instr = []
    for line in file:
        instr.append(line)
    return instr

def shuffle(instr):
    deck = [i for i in range(119315717514047)]
    for tech in instr:
        command = ' '.join(tech.split(' ')[:-1])
        print(command)
        if command == 'deal with increment':
            num = int(tech.split(' ')[-1])
            deck = deal_increment(deck, num)
        elif command == 'deal into new':
            deck = new_stack(deck)
        elif command == 'cut':
            num = int(tech.split(' ')[-1])
            deck = cut(deck,num)
        else:
            raise ValueError('unknown command')
    print(deck[2020])
    return deck

# print(shuffle(['deal into new stack','cut -2',
# 'deal with increment 7',
# 'cut 8',
# 'cut -4',
# 'deal with increment 7',
# 'cut 3',
# 'deal with increment 9',
# 'deal with increment 3',
# 'cut -1']))

print(shuffle(read_input()))

