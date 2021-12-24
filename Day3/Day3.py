#!/usr/bin/env python3

def challenge1(rate):
    for i in range(12):
        g = [i[bit] for bit in rate if i[bit] == 1]
        print(g)

bin_rates = [i for i in open('d3_input')]

print("Challenge 1: ", challenge1(bin_rates))