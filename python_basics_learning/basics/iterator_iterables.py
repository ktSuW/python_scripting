# l1 = [1,2,3,4] #string, list, tuple, dict
# l1 = (1,2,3,4) # tuple
# l1 = {1,2,3,4} # set
# l1 = {
#     1: 'a',
#     2 : 'b',
#     3 : 'c',
#     4 : 'd'
# }
# l1_itr = iter(l1)
# print(next(l1_itr))
# print(next(l1_itr))
# print(next(l1_itr))
# print(next(l1_itr))
#StopIteration error - end of sequence

## Generators - works like iterator - Inner
def Days():
    days = ['sun', 'mon', 'tue', 'wed', 'thurs', 'fri', 'sat']
    i = 0
    while True:
        day = days[i]
        i = (i+1) % 7 #cyclic indices
        yield day # generator function continues from the same point, generator function maintains the state
# yield keyword is used to create a generator function. A type of function that is memory efficient and can be used like an iterator object.
# Take iterator upon this function
d = Days()
print(d) # becomes iterator
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))


        

# # Iterables - something that can be looped over, e.g. list, tuples, dic, string, file
# # __iter__() - 
# nums = [1,2,3,4]
# # i_nums = nums.__iter__()
# i_nums = iter(nums)
# # for i in nums:
# #     print(i)
# # for loop in the background calls __iter__ on the object
# # get next value, dunternext method is not available
# # print(i_nums)
# # print(dir(nums))

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break 
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

# class MyRange:
#     def __init__(self, start, end):
#         self.value = start
#         self.end = end 
    
#     def __iter__(self):
#         return self 
    
#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value += 1
#         return current
    
# nums = MyRange(1,5)
# print(next(nums))
# print(next(nums))
# print(next(nums))
#15 mins 

# for num in nums:
#     print(nums)
        

# https://www.youtube.com/watch?v=jTYiNjvnHZY