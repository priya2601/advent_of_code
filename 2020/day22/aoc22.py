# Space cards


def get_cardseq(file):
    p1 = []
    p2 = []
    with open(file) as fil:
        lines = fil.readlines()
        k = 0
        for i in range(1, (len(lines)-1)/2):
            p1.append(int(lines[i].strip()))
        for i in range((len(lines)-1)/2 + 2, len(lines)):
            p2.append(int(lines[i].strip()))
    return p1, p2


# def get_winner(p1,p2):
p1, p2 = get_cardseq('aoc22_sample.txt')

