#!/usr/bin/env python

from math import factorial
from sys import argv

if len(argv) == 2:
    n = int(argv[1])
else:
    n = input("Number of elements: ")

print("Number of permutations for the " + str(n) + "-elements set eguals: " + str(factorial(n)) + ".")
