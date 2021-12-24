#!/usr/bin/env python3

def challenge1(rate):
    for i in range(12):
        g = ""
        e = ""
        if sum(bit[i] == '1' for bit in rate) > len(rate) // 2:
            g += "1"
            e += "0"
        else:
            e += "1"
            g += "0"
        print(g)
        return int(''.join(g), 2) * int(''.join(e), 2)


bin_rates = [i for i in open('d3_input')]

print("Challenge 1: ", challenge1(bin_rates))
