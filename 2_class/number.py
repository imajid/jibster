#!/usr/bin/env python3

class Number():
    def __init__(self, n):
        self.val = int(n)

    def is_positive(self):
        pass

    def is_negative(self):
        pass

    def is_even(self):
        pass

    def is_odd(self):
        pass

    def is_prime(self):
        pass

    def is_not_prime(self):
        pass

x = input("Give me a number: ")
n = Number(x)

if n.is_positive():  print("{} is positive.".format(n.val))
if n.is_negative():  print("{} is negative.".format(n.val))
if n.is_even():      print("{} is even.".format(n.val))
if n.is_odd():       print("{} is even.".format(n.val))
if n.is_prime():     print("{} is prime.".format(n.val))
if n.is_not_prime(): print("{} is not prime.".format(n.val))
