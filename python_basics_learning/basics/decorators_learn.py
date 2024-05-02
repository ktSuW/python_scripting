# Decorator functions - Basic concepts
"""
In python, everything is an object
Function aliasing - for existing function, gives another reference variable
Even if you delete one variable, you can still use the other variable
"""

def f1():
    print('Hello world')
    
# print(type(f1)) # f1 is a reference variable to function object
# print(id(f1)) # address of f1

def greet(name):
    print(f'Good morning {name}')
# print(greet)
おはよう = greet # おはよう points to the same object
# print(おはよう)
# greet('Saga')
# おはよう('Taka')
del greet
# おはよう('Sakura')

"""
Nested Functions - function declared inside another function
"""

def outer():
    print('Outer function execution started.')
    
    def inner():
        print('Inner function execution')
    # Call inner function
    inner()
    print('Outer function execution completed.')

outer()
# Calling inner function from outside is not possible since it is local to outer() function

