"""
Python functions types
- built in functions - e.g. print(), int(), len(), sum(), they are loaded into computer's memory as soon as you start Python interpreter
- Standard library also bundles a number of modules. Each module has a group of functions, they are not readily available. 
- Need to import them into the memory from their respective modules

Pass by Reference vs Pass by Value
- Call by value - C/C++
- Call by reference - Python uses pass by reference
- Behaviour also depends on whether the passed object is mutable or immutable. Python numeric object is immmutable.

Order of Python Function Arguments
- def function(a,b,/,c,d, e=v1, f=v2, *arg, g, h, i=v3, **kwarg)
- **kwarg arbitary number of keywords arguments
"""
# Default arguments
# default should be on the right side and is created only once
def add(a,b = 0,c=1):
    return a + b + c

a1 = add(1,2)
a2 = add(3,4,5)
a3 = add(100)
print(a1, a2, a3)

# Positional vs Keyword arguments
# def net_salary(basic, allowance, deduction):
#     net = basic + allowance - deduction
#     return net 
# Positional arguments
# net = net_salary(80,50,20)
# print(net)\
# Keyword arguments
# net = net_salary(30, allowance=45, deduction=10)
# print(net)
# def add_nums(a,b,c):
#     result = a + b + c
#     print(id(a), id(b), id(c))
#     return result
# a,b,c = 3,8,7
# # call by reference
# print(id(a), id(b), id(c))
# result = add_nums(a,b,c)
# print(result)

# def test_call_by_value_reference(arg):
#     print("ID inside the function: " , id(arg))
#     arg = arg + 1 
#     print("new object after increment", arg, id(arg))
    
# greeting = "Hello"
# print("ID before passing :", id(greeting))
# test_call_by_value_reference(greeting)

# Number is NOT mutable
# num = 10
# print("ID before passing :", id(num))
# test_call_by_value_reference(num)
# print("Value after function call: ", num)


# Mutable object - list, dictionary, passed by reference
# def testfunction(arg):
#     print("Inside the function: ", arg)
#     print("ID inside the function: ", id(arg))
#     arg = arg.append(100)

# var = [1, 2, 3, 4,5]
# print("ID before passing: ", id(var))
# testfunction(var)
# print("list after function call: ", var)
# print("ID after passing: ", id(var))


