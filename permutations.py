# from math import factorial
from sys import argv

if len(argv) == 2:
    n = int(argv[1])
else:
    n = input("Enter number: ")

#def num_of_perms(n):
#    return factorial(n)

def num_of_perms(n):
    f = (lambda x: x * f(x-1) if x != 0 else 1)
    return f(n)
print(num_of_perms(n))
