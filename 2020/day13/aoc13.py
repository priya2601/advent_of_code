# bus to airport


def get_input(filename):
    schedule = []
    with open(filename) as fil:
        lines = fil.readlines()
        timstmp = int(lines[0].strip())
        schedule = lines[1].split(',')
    return timstmp, schedule


def find_earliest(timstmp, schedule):
    n = timstmp
    while True:
        for bus in schedule:
            if bus != 'x':
                rem = n % int(bus)
                if rem == 0:
                    return (n - timstmp)*int(bus)
        n += 1


# timstmp, schedule = get_input('aoc13_sample.txt')
timstmp, schedule = get_input('aoc13_input.txt')
print(find_earliest(timstmp, schedule))