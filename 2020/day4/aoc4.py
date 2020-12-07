# passport check fields
import re


def get_input(filename):
    data = []
    passport = {}
    passport_str = []
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            if line != '\n':
                passport_str.extend(line.split())
            if line == '\n' and passport_str != []:
                for ele in passport_str:
                    passport[ele.split(':')[0]] = ele.split(':')[1]
                data.append(passport)
                passport = {}
                passport_str = []
    return data


def check_passport(passport):
    required = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    required.sort()
    valid = 0
    available = []
    for field in passport:
        available.append(field.split(':')[0])
    available.sort()
    try:
        i = available.index("cid")
        del available[i]
    except ValueError:
        pass
    return available == required


def check_passport_2(passport):
    valid1 = (1920 <= int(passport['byr']) <= 2002) and (2010 <= int(passport['iyr']) <= 2020) \
             and (2020 <= int(passport['eyr']) <= 2030) and (
            re.match(r"^#[0-9a-f]{6}$",passport['hcl'] )) and (
        re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$",passport['ecl'])) and (
        re.match(r"^\d{9}$",passport['pid']))

    hgt1_valid = False
    hgt2_valid = False
    hgt1 = re.match(r"^(?P<cm>\d+)cm$", passport['hgt'])
    if hgt1:
        cm = int(hgt1.group('cm'))
        hgt1_valid = 150 <= cm <= 193
    hgt2 = re.match(r"^(?P<inc>\d+)in$", passport['hgt'])
    if hgt2:
        inc = int(hgt2.group('inc'))
        hgt2_valid = 59 <= inc <= 76
    valid2 = hgt1_valid or hgt2_valid
    print(valid1,hgt1_valid,hgt2_valid)
    return valid1 and valid2


def check_passport_final(data):
    valid = 0
    for passport in data:
        if check_passport(passport):
            if check_passport_2(passport):
                valid += 1
    return valid


data = get_input('aoc4_input.txt')
print(check_passport_final(data))