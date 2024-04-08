#!/usr/bin/env python3

d = dict()

while True:
    x = input("Enter a number between 0-10, q to quit: ")
    if x == 'q' or x == 'Q':
        break
    x = int(x)
    if x not in d:
        d[x] = 1
    else:
        d[x] = d[x] + 1

for x in d:
    print("You gave me {} {} times.".format(x, d[x]))


