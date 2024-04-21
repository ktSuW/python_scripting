"""
BeautifulSoup
requests
lambda, https://realpython.com/python-lambda/
Python lambdas are little, annoymous functions, give concise syntax than regular python functions
- lambda calculus 
- it does not keep any state
- state based module of computation
- map(), filter(), reduce()
- The title() method returns a string where the first character in every word is upper case. Like a header, or a title. If the word contains a number or a symbol, the first letter after that will be converted to upper case.
- anonymous /lambda functions/lambda expression/ lambda abstractions/lambda form/function literals
"""
# Higher order function
# In python, a function can be assigned to a variable. This assignment does not call the function, instead a reference to that function is created
# def shout(text):
#     return text.upper()

# print(shout('Hello'))

# #Assign function to a variable 
# yell = shout
# print(yell('Hello')) 
# # functions are like objects in python, therefore, they can be passed as argument to other functions. 

# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.upper()

# def greet(func):
#     greeting = func('Hi, I am created by a function.')
#     print(greeting)
    
# greet(shout)
# greet(whisper)
#==============================================
# def create_adder(x):
#     def adder(y):
#         return x + y
    
#     return adder 

# add_15 = create_adder(15)
# print(add_15(10))
#================================================
# Decorators
# Decorators are the most common use of higher-order functions in python. It allows programmers to modify the behaviour of function or class. Decorators allow us to wrap another function in order to extend the behaviour of wrapped function, without permanently modifying it. 

# def hello_decorator(func):
#     #inner 1 is a Wrapper function in which the argument is called
#     def inner1():
#         print("Hello, this is before function execution")
#         # calling the actual function now 
#         # inside the wrapper function function
#         func()
#         print("This is after function execution")
#     return inner1 


# def function_to_be_used():
#     print("This is inside the function!")
    
# function_to_be_used = hello_decorator(function_to_be_used)

# function_to_be_used()
#===============================================
# """
# dis

# """
# import dis 

# add = lambda x,y : x + y
# print(type(add))
# print(dis.dis(add))
# print(add)
#================================================
# def some_decorator(f):
#     def wraps(*args):
#         print(f'Calling function "{f.__name__}"')
#         return f(args)
#     return wraps 

# @some_decorator
# def decorated_function(x):
#     print(f'With argument "{x}"')
    
# decorated_function("Travelling")
#================================================
# # Define decorator
# def trace(f):
#     def wrap(*args, **kwargs):
#         print(f'[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}')
#         return f(*args, **kwargs)
#     return wrap

# #Applying a decorator to a function
# @trace
# def add_two(x):
#     return x + 2 

# # Calling a decorated function
# add_two(3)

# # Applying a decorator to lambda
# # print((trace(lambda x: x**2))(3))
# #================================================
# list(map(trace(lambda x: x*2), range(6)))
#================================================
# closure 
# a closure is a function where every  free variales, everything except parameters, used in that function is bound to a specific value defined in the enclosing scope of that function
#================================================
# def outer_func(x):
#     y = 4
#     def inner_func(z):
#         print(f'x={x}, y ={y}, z= {z}')
#         return x+y+z
#     return inner_func

# for i in range(4):
#     closure = outer_func(i)
#     print(f'closure({i+5} = {closure(i+5)})')
#================================================
# nums = 'one', 'two','three'
# # print(type(nums))
# funcs = []
# for n in nums:
#     funcs.append(lambda n=n:print(n))

# for f in funcs:
#     f()
#================================================
# class Car:
#     """Car with methods as lambda functions"""
#     def __init__(self,  brand, year):
#         self.brand = brand
#         self.year = year 
        
#     brand = property(lambda self: getattr(self, '_brand'), lambda self, value: setattr(self, '_brand', value))
    
#     year = property(lambda self: getattr(self, '__year', lambda self, value: setattr(self, '__year')))

# __str__ = lambda self: f'{self.brand} {self.year}'
# honk = lambda self: print('Honk!')

#================================================
# def identity(id):
#     return id

# # lambda(keyword) x(bound variable - argument to a lambda function) : x(body)
# test1 = (lambda x: x+1)(2) 

# # def test2(x):
# #     return x + 1
# test2 = (lambda x: x +1)
# print(test1)
# print(test2(5))
# full_name = lambda first, last : f'Full name : {first.title()} {last.title()}'

# print(full_name('Tanaka', 'Handa'))
# higher_order_function = lambda x, func: x + func(x)
# print(higher_order_function(2, lambda x : x * x))


