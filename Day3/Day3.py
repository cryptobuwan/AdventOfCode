#!/usr/bin/env python3

def challenge1(rate):
    g = ""
    e = ""
    for i in range(12):

        if sum(bit[i] == '1' for bit in rate) < len(rate) // 2:
            e += "1"
            g += "0"
        else:
            g += "1"
            e += "0"
        print(g)
    return (int(g, 2) * int(e, 2))


bin_rates = [i for i in open('d3_input')]

print("Challenge 1: ", challenge1(bin_rates))
