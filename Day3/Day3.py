#!/usr/bin/env python3
from collections import Counter

def challenge1(rate):
    # store Gamma rate
    g = ""
    # store epsilon rate
    e = ""
    # create columns for bits
    for column in range(12):
        # adds up all the 1's in the selected column and compares it to total so see if it's the common bit
        if sum(bit[column] == '1' for bit in rate) < len(rate) // 2:
            # if it's not a common bit this is the result
            e += "1"
            g += "0"
        else:
            # if it's a common bit this is the result
            g += "1"
            e += "0"
    # returns the dec value of epsilon times the gamma rate
    return int(g, 2) * int(e, 2)


def challenge2(bits):
    oxy, co2 = "", ""
    c1, c0 = 0, 0
    # create columns for bits
    for column in range(5):
        c1 = 0
        c0 = 0
        for bit in bits:
            common = Counter(bit[column]).most_common()

    return common


bin_rates = [i for i in open('d3_input')]
demo = [list(map(str.strip, i)) for i in open('sample')]

print("Challenge 1: ", challenge1(bin_rates))
print("Challenge 2: ", challenge2(demo))
