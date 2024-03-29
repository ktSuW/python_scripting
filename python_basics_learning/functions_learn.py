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

def test_call_by_value_reference(arg):
    print("ID inside the function: " , id(arg))
    arg = arg + 1 
    print("new object after increment", arg, id(arg))
    
# greeting = "Hello"
# print("ID before passing :", id(greeting))
# test_call_by_value_reference(greeting)

# Number is NOT mutable
# num = 10
# print("ID before passing :", id(num))
# test_call_by_value_reference(num)
# print("Value after function call: ", num)


# Mutable object - list, dictionary, passed by reference
def testfunction(arg):
    print("Inside the function: ", arg)
    print("ID inside the function: ", id(arg))
    arg = arg.append(100)

var = [1, 2, 3, 4,5]
print("ID before passing: ", id(var))
testfunction(var)
print("list after function call: ", var)
print("ID after passing: ", id(var))


