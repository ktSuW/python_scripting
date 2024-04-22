"""Notes
- https://book.pythontips.com/en/latest/map_filter.html
- https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce
- 
"""
# def is_even(n):
#     return n % 2 == 0
# nums = [3,2,6,8,4,6,2,9]

# evens_1 = list(filter(is_even, nums))
# print(evens_1)
# evens_2 = list(filter(lambda n: n%2 == 0, nums))
# print(evens_2)

# map -------------------------------------------
# nums = [3,2,6,8,4,6,2,9]
# def update(n):
#     return n*2

# doubles_1 = list(map(update, nums))
# doubles_2 = list(map(lambda n : n*2, nums))
# print(doubles_2)

#----reduce ------------
nums = [3,2,6,8,4,6,2,9]
from functools import reduce 

def add_all(a,b):
    return a+b
reduce_1 = reduce(add_all, nums)
reduce_2 = reduce(lambda a,b: a+b, nums)
print(reduce_1)
print(reduce_2)
