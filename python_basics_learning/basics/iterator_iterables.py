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

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end 
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    
nums = MyRange(1,5)
print(next(nums))
print(next(nums))
print(next(nums))
#15 mins 

# for num in nums:
#     print(nums)
        

# https://www.youtube.com/watch?v=jTYiNjvnHZY