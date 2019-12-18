" FFT phases"
import math
import numpy as np

def read_input():
    file = open('input_aoc16.txt','r')
    lst = []
    for line in file:
        lst.append(line)
    return lst[0]

def calc_fft(signalstr):
    signals = [int(signal) for signal in signalstr]
    patt = [0,1,0,-1]
    pattern = []
    for dig in range(1,len(signals)+1):
        lstt = [[t]*dig for t in patt]
        l = lstt * (math.ceil(len(signals)/len(patt))+1)
        pattern.append([item for sublist in l for item in sublist][1:len(signals)+1])
    # print(pattern)
    # print(signals)
    for phase in range(100):
        output = []
        for digit in range(len(signals)):
            output.append(abs(np.dot(signals,pattern[digit])) % 10)
            # print(np.dot(signals,pattern[digit]))
        signals = output
        # print(output)
    return signals

def calc_fft2(signalstr):
    signals = [int(signal) for signal in signalstr] * 10000
    offset = int(signalstr[0:7])
    for phase in range(100):
        output = signals.copy()
        partial_sum = sum([signal for signal in signals[offset:]])
        print(partial_sum)
        for i in range(len(signals[offset:])):
            output[offset+i] = abs(partial_sum)%10
            partial_sum -= signals[offset+i]
        signals = output
        # print(output)
    return signals[offset:offset+8]

# print(calc_fft2('03081770884921959731165446850517'))



print(calc_fft2(read_input()))