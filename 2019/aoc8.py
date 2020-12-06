" Images as series of digits25x6xlayers"

import numpy as np

np.set_printoptions(linewidth=200)

def read_input():
    file = open('input_aoc8.txt', 'r')
    lst = []
    for line in file:
        lst.append(line)
    return lst[0]

# print(read_input())

def calc_layers(digitstr,width=25,height=6):
    layers = int(len(digitstr)/(width*height))
    digits = []
    for digit in digitstr:
        digits.append(int(digit))
    digits = np.array(digits)
    image = digits.reshape((layers,height,width))
    min_zero_count = 1000000
    min_zero_layer = None
    for layer in range(layers):
        zero_count = np.sum(image[layer] == 0)
        if zero_count < min_zero_count:
            min_zero_count = zero_count
            min_zero_layer = layer
    return np.sum(image[min_zero_layer] == 1) * np.sum(image[min_zero_layer] == 2)

def calc_image(digitstr,width=25,height=6):
    layers = int(len(digitstr)/(width*height))
    digits = []
    for digit in digitstr:
        digits.append(int(digit))
    digits = np.array(digits)
    image = digits.reshape((layers,height,width))
    result = np.ones((height,width)) * 2
    for layer in range(layers):
        for ht in range(height):
            for wid in range(width):
                if (image[layer][ht][wid] == 0 or image[layer][ht][wid] == 1) and result[ht][wid] == 2:
                    result[ht][wid] = image[layer][ht][wid]
    return(result)

# print(calc_image('0222112222120000',2,2))
print(calc_image(read_input()))


# print(calc_layers('123456789012',3,2))

# print(calc_layers(read_input()))

