# Basic Introduction to Decorators
"""Decorators
- Decorator is a function which can take a function as argument and extends its functionality and returns modified function with extended functionality
- The main object of decorator functions is we can extend functionality of existing function without modifying that function
- Purpose is decoration : For brithday, cake, some decorations. Person who does all the decorations is decorator.
- Input function(Takes function as argument) --> Decorator Function --> will generate an output function with extended functionality

- Birthday person --> Dressing up, decorating by decorator --> Dressed up, decorated 
"""

def decorator_function(input_func):
    def output_func():
        # add extra 
        pass
    return output_func



"""
Summary
------------
1. We can assign another name to existing function => function aliasing
2. We can define one function inside another function => nested function
3. A function can return another function
4. We can pass a function as argumen to another function 
    Expect another function as argument
    map(), filter(), reduce()
"""
# Decorator functions - Basic concepts

"""
A function can return another function
We can pass a function as an argument to another function
"""
# def outer():
#     def inner():
#         print('Inner function execution.')
#     return inner # returns inner function object , there is no (), must not include ()
#     # return inner() - the difference is this inner function gets executed, then

# # f1 = outer() # inner function aliasing, outer function returns inner function object
# # # Call inner function
# # f1()
# # f2 = outer # f2 points to the same object, function aliasing
# # f2()

# def f1(func):
#     func()

# def f2():
#     print('f2 function')
# # Pass f2 function as argument to f1 function 
# f3 = f1(f2)
# f3
# # Take function and sequence such as list, tuple, etc
# # filter(function, list) # to filter values based on some condition specified inside function
# # map(function, list)
# # reduce(function, list)

# list1 = [1,2,3,4,5,6]
# def is_even(n):
#     return n%2 == 0

# even_nums = filter(is_even, list1)
# print(even_nums) # return filtered object
# list2 = list(even_nums) # return list object
# print(list2)
# list3 = list(filter(is_even, list1))
# print(list3)


# """
# In python, everything is an object
# Pythonではすべてがオブジェクトです
# Function aliasing - for existing function, gives another reference variable
# Even if you delete one variable, you can still use the other variable
# """

# def f1():
#     print('Hello world')
    
# # print(type(f1)) # f1 is a reference variable to function object
# # print(id(f1)) # address of f1

# def greet(name):
#     print(f'Good morning {name}')
# # print(greet)
# おはよう = greet # おはよう points to the same object
# # print(おはよう)
# # greet('Saga')
# # おはよう('Taka')
# del greet
# # おはよう('Sakura')

# """
# Nested Functions - function declared inside another function
# """

# def outer():
#     print('Outer function execution started.')
    
#     def inner():
#         print('Inner function execution')
#     # Call inner function
#     inner()
#     print('Outer function execution completed.')

# # outer()
# # Calling inner function from outside is not possible since it is local to outer() function

