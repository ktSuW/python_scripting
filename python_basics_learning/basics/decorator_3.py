
def divide_check(func):
    def inner_check(a,b):
        if b == 0:
            print('This will raise ZeroDivisionError.')
        else:
            # This will call divide,func is divide
            func(a,b)
    return inner_check

# link decorator 
@divide_check # python VM will check if there is any decorator configured
def divide(a,b):
    print(a/b) # float value

divide(10,2)
divide(10,0) # Zero division error

"""
Summary
============
1. Decorator function should be defined first and then use
2. While defining decorator, the number of arguments must be matched.

"""