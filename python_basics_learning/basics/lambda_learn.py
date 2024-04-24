lst1 = [1,2,3,4,5]

def twice(n):
    return n*2

# pass the reference to the function, therefore, no ()
# higher level function - since it calls other function and the way it calls is pass the reference of the other function, with each item in the list is an argument, is a kind of foreach loop
lst1_map = map(twice, lst1)
# python v3 - about 10 years now, map returns an iterator, not a list, an object that will generate a list for you if you ask
# python v2 - map returns a list, iterable , concrete list
# e.g. 10 millions numbers -> only need one memory location
# print(list(lst1_map)) 
print("----------------------------")
# for i in lst1_map:
#     print(i)
# iterator has state
x = next(lst1_map)
print(x)
y = next(lst1_map)
print(y)
print("----------------------------")
for i in lst1_map:
    print(i)
print("----------------------------")   
# map, filter, reversed, range => return object which are iterators
# x = range(5) # returns iterator, not a list 
# print(type(x))
# for i in x:
#     print(i)    
    
    
    
    
# Iterator    





# # function reference and trasfer it to a variable, x
# # print is a variable that holds a reference to the function code in the memory
# x = print #function name without () acts as a reference to the function
# x("Hello World")

# # print(id(x))
# # print(id(print))
# 10('Hello World')
# print = 10 

# print("Hello World")
