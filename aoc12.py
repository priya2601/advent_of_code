" get energy of Jupiter moons"
import copy

def read_input():
    file = open('input_aoc12.txt','r')
    lst = []
    for line in file:
        lst.append([int(t) for t in line.split(',')])
    return lst

# print(read_input())

def calc_energy(positions):
    velocity =[[0]*3,[0]*3,[0]*3,[0]*3]
    gravity = [[0]*3,[0]*3,[0]*3,[0]*3]

    for time in range(1000):
        energy = 0
        for moon in range(4):
            for axis in range(3):
                gravity[moon][axis] = sum([positions[other_moon][axis] > positions[moon][axis] for other_moon in range(4)]) \
                    - sum([ positions[other_moon][axis] < positions[moon][axis] for other_moon in range(4)])
                velocity[moon][axis] += gravity[moon][axis]
        for moon in range(4):
            pot_energy = 0
            kin_energy = 0
            for axis in range(3):
                positions[moon][axis] += velocity[moon][axis]
                pot_energy += abs(positions[moon][axis])
                kin_energy += abs(velocity[moon][axis])
            energy += pot_energy * kin_energy
        # print(time)
        # print(positions)
        # print(velocity)
    return energy


# print(calc_energy([[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]]))

# print(calc_energy([[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]]))

def calc_time_axis(positions):
    velocity =[0,0,0,0]
    gravity = [0,0,0,0]
    original_velocity = copy.deepcopy(velocity)
    original_positions = copy.deepcopy(positions)
    time = 0

    while True:
        for moon in range(4):
            gravity[moon] = sum([positions[other_moon] > positions[moon] for other_moon in range(4)]) \
                    - sum([ positions[other_moon] < positions[moon] for other_moon in range(4)])
            velocity[moon] += gravity[moon]

        for moon in range(4):
            positions[moon] += velocity[moon]
        time += 1
#        if time % 1000 == 0:
#            print(time)
        if positions == original_positions and velocity == original_velocity:
            return time

def calc_time(positions):
    for axis in range(3):
        position_axis = [positions[moon][axis] for moon in range(4)]
        print(calc_time_axis(position_axis))

# print(calc_energy(read_input()))


#print(calc_time([[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]]))

#print(calc_time([[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]]))
# 4686774924
print(calc_time(read_input()))







