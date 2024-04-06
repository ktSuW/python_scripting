# array (list)
"""
list is an ordered collection
list is heterogenous object.
Each item is an object in the memory
Variable can hold any type of data
List is mutable, can be modified

integer, float, string -- immutable data types
list concatenate -> create a new object in the memory
list extend -> add it to the same object, no new object is created in the memory
in, not in boolean operators 
0   1   2   3   4   
"a"     "b"     "c"     "d"     "e"
"""
# Tuple Datatype - same as list, but it is immutable, cannot add or remove 
# tuple1 = (1,2,3,4,5)
# python built-in modules list
"""
tup1 = ()
os - provides a unified interface to a number of os functions
string - for string processing
re = regex 
math 
datetime
gc - builtin garbage collector
asyncio - asynchronous processing
Collections - advanced containter datatypes
socket - low level networking interface
sqlite3 -
statistics
typing 
venv - creation of virtual environments
json - encode and decode JSON format
unittest - unit testing framework for python
random - generate pseudo random numbers
"""
# only a number, string or tuple can be used as a key. All of them are immutable. Values can be any type
japan_cities1 = {
    "Tokyo": "Tokyo",
    "Osaka": "Osaka",
    "Kyoto": "Kyoto",
    "Hiroshima": "Hiroshima",
    "Sapporo": "Hokkaido",
    "Nagoya": "Aichi",
    "Fukuoka": "Fukuoka",
    "Kobe": "Hyogo",
    "Yokohama": "Kanagawa",
    "Sendai": "Miyagi",
    "Nara": "Nara",
    "Kanazawa": "Ishikawa",
    "Nagasaki": "Nagasaki",
    "Kumamoto": "Kumamoto",
    "Hakodate": "Hokkaido"
}
japan_cities2 = {
    "Nara": "Nara",
    "Kanazawa": "Ishikawa",
    "Nagasaki": "Nagasaki",
    "Kumamoto": "Kumamoto",
    "Hakodate": "Hokkaido"
}

japan_cities_values = japan_cities1.get("ara") # returns the value mapped to the given key
print(japan_cities_values)

# s1 = {1,2,3,4,6,4,3,2}
# print(s1)
# python membership operators in, not in
# identity operators - is, is not 
# operator evalutes to True if both the operand objects share the same memory location.
# memory location -> id() True
# bitwise AND, OR, XOR, NOT left shift, right shift

# s1 = {1, 2, 3, 7, 9}
# # set is not a sequence data type
# # cannot be accessed individually as they do not have a positional index, can only traverse the set items using a for loop
# # s1.add(23)
# # for num in s1:
# #     print(num)
# s2 = {"Hello", "world", 7, 9}#union
# s3 = s1.union(s2)
# # s1.update(s2)
# # s1.remove(10) #KeyError - use discard instead
# s1.pop() # remove random item from s1
# s1.clear()
# print(s1)
# print(s1) # TypeError: unhashable type: 'list'
# hasing generates a unique number for an immutable item that enables quick search
# python built in function hash() is not supported by list or dictionary
# t1 = (1, 1, 2, 3, 4, 4, 2, 6, 7, 9, 8, 7,7)
# t2 = ()
# for i in t1:
#     if i not in t2:
#         t2 +=(i,)
        
# print("Original tuple t1 : ", t1)
# print("Unique numbers tuple t2 : ", t2)

# import random

# t1 = ()
# for i in range(10):
#     x = random.randint(0,10)
#     if x not in t1:
#         t1 +=(x,) 
# print(t1)

# cities = ("Osaka", "Nagoya", "Kagoshima", "Yokohama")
# a,b,c,d = cities
# print("a: ",a, "b: ", b)
# tup1 = (12, 3, 45, 64, 23, 80)
# indices = range(len(tup1))
# for i in indices:
#     print(f"tup1[{i}] : ", tup1[i])

# + concatenate
# a.extend(b)
# tuple count() , index()

# print(tup1[2])
# tup1[2] = ("Hida no Sato")
# del cities
# print(cities[2])
# machi = ("Amori", "Saitama", "Kochi")
# print(cities+machi) # concatenation

#==================
# l1 = [None]*10
# print(l1)
#==================
# a = [[1,2,3], [4,5,6], [7,8,9]]
# b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

# c = []

# for i in range(len(a)):
#     s = []
#     for j in range(len(a[0])):
#         s.append(a[i][j] + b[i][j])
#     c.append(s)

# print(c)

#==================
# list = [1,2, ["a", "b", ["c", "d"]], 4,5]

#==================
# index, count, reverse, sort(*, key=None, reverse=False)
#l1 = [expression for item in iterable]
# iterable - str, range, str, tuple, list 
# l1 = [x for x in range(10)]
# l2 = [x**2 for x in range(1,6)]
# l3 = [x for x in (10,5,7,8,12,3) if x%2==0]
# print(l3)
# l4 = [x.lower() for x in "Python"]
# l5 = [x for x in 'ab123dsdf&4$hi2' if x.isalpha()]
# print(l5)

# data = input("Enter names: ").split()
# print(data)

#==================
# a2 = ["yy", "jj", "mm", "BB", "aa", "ZZ"]
# # a2.sort(key=str.lower)
# sorted(a2) # Do not modify the original list
# print(a2)
#==================
# a1 = [4,5,6, 8,9,2,3,1,10,6,7]
# print(a1.count(6))
# a1.reverse()
# a1.sort()
# print(a1)
# print(a1.index(9,4,8))

# index(x[,start[,end]]), count(x), reverse(), sort(*, key=None, reverse=False)

#============
# list methods for list class - append, extend, insert, copy
# append is only for one element, extend is for adding collections of elements, iterable
# a1.append(21)
# a1[6:6] = [23]
# a1[len(a1):] = [14]
# print(a1)

# a1.extend((10,11,12)) # parameters must be iterable. list, tuple, string
# a1.extend("apple") # string is iterable.
# a1[len(a1):] = ["orange"]
# print(a1)
#======================
# print(id(a1))
# a1.insert(1,50) # it is a costly operateion if inserting at the beginning of the list 
# print(a1)
# print(id(a1)) # Same list is modified, therefore new object is not created.
#======================
# copy - create a shallow copy, clone of original list is created
# a2 = a1.copy()
# print(id(a1[0]))
# print(id(a2[0]))
#======================
# print(a1)
# a1.pop(2)
# del a1[2]
# print(a1)
#======================
# a1.remove(5)  # need to specify the element you want to delete, # if there is duplicates, will delete the first one
# # a1.remove("apple") # gives ValueError
#======================


# i = 0
# while i < len(a1):
#     print(a1[i])
#     i +=1
# for i in range(len(a1)-1,-1,-1):
#     print(a1[i])

# for i in range(1,len(a1)):
#     print(a1[i])
    
# for x in a1:
#     print(x)
    
    
    
# lucky_numbers_list = [3,7,9,17,23]

# for i in lucky_numbers_list:
#     print(i)
# print(lucky_numbers_list[1])

# list1 = list(1,2,3,4,5)
# list1 = list((1,2,3,4,5))
# for index, num in enumerate(list1):
#     print(index, num)

# list2 = ["Sato", "Hida", 2026, True, 23.45]
# list2[0] = "Hida no Sato"
# list2.append("haru") # Append is costly because it creates a new object

# Operators on list - [], [:], +, * , in, not in 
# [] index operator 
# slice operator [:], start, end, step
# list3 = [10,20,30,40,50,60]
# can replace with less items, eqal or more items
# print(list3[::2])
# print(list3[::-2])
# list3[0:3] = [70,80]
# list3[0:3] = ["a", "b", "c", "d"]
# print(list3)

list4 = [1,2,3]
list5 = [4,5,6]
item = 4
# Can only concatenante list to list ONLY, not int
# new_list = list4 + list5 + item
# print(new_list)

# list4.extend([7,8,9])
# list5 = list5 + [10,11,12]
# list5 = list5*2
# # print(list5)
# if 4 in list5:
#     print("Found")
# else:
#     print("Not Found")