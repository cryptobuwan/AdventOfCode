#!/usr/bin/env python3


# created a function to compare the list with itself and count the increases
def challenge1(dep):
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


def challenge2(dep):
    # counter
    increase = 0
    # first window which iterates list creating windows and summing them up
    window1 = [sum(dep[i:i+3]) for i in range(len(dep)) if len(dep[i:i+3]) == 3]
    # second window which iterates list creating windows and summing them up
    window2 = [sum(dep[i+1:i+4]) for i in range(len(dep) - 2) if len(dep[i:i+3]) == 3]
    # compares first and second window and counts the increases
    for i in range(len(window1)):
        increase += window1[i] < window2[i]
    # returns value
    return increase

# opens the file and stores it in temp var as f
with open("input") as f:
    # converts f into a list stores it in depth as int
    depth = [int(i) for i in f.readlines()]

# print results, function that runs the stored list depth
print("Challenge 1: ", challenge1(depth))
print("Challenge 2: ", challenge2(depth))
