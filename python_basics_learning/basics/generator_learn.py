# # by putting yield inside the function, it becomes a generator object. It wraps in generator object.
# def func1():
#     print("Start")
#     yield 55 #stateful, keeps the function running in memory - return destory function calls
#     print('End')
#     yield 77
# # Purpose is like iterator
# # f1 will return None
# x = func1()
# # print(type(x))
# # function does not run unless you use next. Continues from where it left off and find it from the memory and runs until the next yield
# # v = next(x) # runs till next yield statement 
# # print(v)
# # z = next(x)
# # print(z)

# # Generator function
# def range1():
#     i = -1
#     while True:
#         i += 1
#         yield i
# # set up generator
# r = range1()
# # call generator using next()
# r_value = next(r)
# # print(r_value)
# print('-----------------')
# # Generally, next() is not used in prod grade code.
# for i in range(10):
#     a = next(r)
#     print(a)
    
# # Generator expression - list comprehensions
# lst1 = [1,2,3,4,5]
# # list comprehension - generator expression in []
# # lst2 = [n*2 for n in lst1]
# ###=========== generator expression on its own, returns generator object
# lst2 = (n*2 for n in lst1)

# # print(type(lst2))
# # Generator object reference
# # print(lst2)
# # Iterate over the generator and gives thel ist 
# # print(list(lst2))

#=========================================
# iterator class 
class MyIter:
    
    def __init__(self):
        self.i = 0
    
    def __next__(self):
        while self.i < 9:
            self.i += 1
            return self.i 
        else:
            raise StopIteration
        
    def __iter__(self):
        return self

# Create a class
g = MyIter()
# x = next(g)
# print(x)

print('=================')
for i in range(20):
    x = next(g)
    print(x)

# iterator expression, function, class 