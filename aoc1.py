def read_fuel():
    f = []
    fil = open('input_aoc1.txt','r')
    for line in fil:
        f.append(int(line))
    return f

def calc(f):
    total = 0
    for mass in f:
        total += int(mass//3.0 - 2)
    return total

# print(calc_fuel())
#
# print(calc([12]))
#
# print(calc([1969]))
#
# print(calc([100756]))

def calc1(lst):
    grand_total = 0

    for num in lst:
        fuel_for_fuel = int(num // 3.0 - 2)
        while fuel_for_fuel > 0:
            grand_total += fuel_for_fuel
            fuel_for_fuel = int(fuel_for_fuel//3.0 - 2)
    return grand_total



# print(calc1([12]))
#
# print(calc1([14]))
#
# print(calc1([1969]))
#
# print(calc1([100756]))

print(calc1(read_fuel()))




