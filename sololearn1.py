from itertools import permutations, repeat

x = int(input("Enter a number: "))

def numbers(x):
    for i in range(1, x + 1):
        yield i
    #[l[i:i + n] for i in range(0, len(l), n)]

numbers_chunks = (numbers(x:x+100) for x in range(0, len(numbers), 100))

# def decor(func):
#     def wrap():
#         print("============")
#         func()
#         print("============")
#     return wrap

num_list = list(numbers(x))
num_list_len = len(list(numbers(x)))
num_list_perm = len(list(permutations(numbers(x))))
print(num_list)
print(numbers_chunks)
#print(list(permutations(numbers(x))))
print("For " + str(num_list_len) + " elements, number of permutations equals: " + str(num_list_perm))
