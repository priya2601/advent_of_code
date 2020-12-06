# min and max


def get_input(filename):
    arr = []
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            min = line.split('-')[0]
            max, letter, pwd = line.split('-')[1].split()
            letter = letter.split(':')[0]
            arr.append([min, max, letter, pwd])
    return arr

def check_pwd(arr):
    valid = 0
    for line in arr:
        min, max, letter, pwd = line
        count = 0
        for charac in pwd:
            if charac == letter:
                count += 1
        if int(min) <= count <= int(max):
            valid += 1
    return valid


def check_pwd_2(arr):
    valid = 0
    for line in arr:
        min, max, letter, pwd = line
        if (pwd[int(min)-1] == letter) ^ (pwd[int(max)-1] == letter):
            valid += 1
    return valid

arr = get_input('aoc2_input.txt')
print(check_pwd(arr))
print(check_pwd_2(arr))
