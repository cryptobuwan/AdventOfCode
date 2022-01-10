#!/usr/bin/env python3

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


def counter(bits, pos):
    # set up counters
    c1, c0 = 0, 0
    # create loop to parsing data to count 1's and 0's
    for bit in bits:
        if bit[pos] == '1':
            c1 += 1
        else:
            c0 += 1
    return c1, c0


def parser(c1, c0, lis, b):
    common = []
    for bit in lis:
        if c1 >= c0 and bit[b] == '1':
            common.append(bit)
        elif c0 > c1 and bit[b] == '0':
            common.append(bit)
    return common


def co2(c1, c0, lis, b):
    common = []
    for bit in lis:
        if c1 < c0 and bit[b] == '1':
            common.append(bit)
        elif c0 <= c1 and bit[b] == '0':
            common.append(bit)
    return common


def oxygen(listed):
    for i in range(12):
        count = counter(listed, i)
        new_list = parser(count[0], count[1], listed, i)
        listed = new_list
    return listed[0]


def co2reading(listed):
    # create columns of the binaries
    for i in range(12):
        #
        count = counter(listed, i)
        new_list = co2(count[0], count[1], listed, i)
        listed = new_list
        if len(listed) == 1:
            return listed[0]


def challenge2(list):
    return int(oxygen(list), 2) * int(co2reading(list), 2)


with open('d3_input') as f:
    bin_rates = f.read().splitlines()


print("Challenge 1: ", challenge1(bin_rates))
print("Challenge 2: ", challenge2(bin_rates))
