#!/usr/bin/env python3


with open("d4_input") as f:
    bingo_nums = [int(x) for x in f.readline().strip('\n').split(',')]
    bingo_cards = []
    while f.readlines():
        bingo_cards = []
        for i in range(5):
            bingo_cards.append([int(x) for x in f.readline().strip('\n').split(' ')])

            print(bingo_cards)
