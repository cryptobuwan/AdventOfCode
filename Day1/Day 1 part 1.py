#!/usr/bin/env python3

# Christopher Carlson
# COSN 206 Final Exam B Q4
import numpy
# created a function to compare the list with itself and count the increases
def compare(dep):
    # the counter for the increases
    increase = 0
    # iterate through the list to compare values in the list starting at the beginning 0 on the end of list
    for d in range(len(dep) - 1):
        # compares first vaule if it is less than the second value
        if int(dep[d]) < int(dep[d + 1]):
            # if its true then adds to the counter
            increase += 1
    # returns the total count
    return increase


def comp(dep):
    increase = 0

    windows = [dep[i:i + 3]]
    print(windows)
            # increase += 1
    # return increase

# opens the file and stores it in temp var as f
with open("input") as f:
    # converts f into a list and removes newlines and stores it in depth
    depth = f.read().splitlines()

# print results, function that runs the stored list depth
print("Answer:", comp(depth))
