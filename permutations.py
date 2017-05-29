#!/usr/bin/env python

from math import factorial
from sys import argv

if len(argv) == 2:
    n = int(argv[1])
else:
    n = input("Enter number: ")

def num_of_perms(n):
   return factorial(n)

print(num_of_perms(n))
