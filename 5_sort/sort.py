#!/usr/bin/env python3

import random

# takes a randomized numbers list and sorts it, we can use python sorted
# function but the idea here is to implement sort and not use sorted.
#
def sort(l):
    return sorted(l)

x = int(input("Enter list size: "))
numbers = [i for i in range(1, x+1)]

random.shuffle(numbers)
print(numbers)

numbers = sort(numbers)
print(numbers)

