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

list4.extend([7,8,9])
list5 = list5 + [10,11,12]
list5 = list5*2
# print(list5)
if 4 in list5:
    print("Found")
else:
    print("Not Found")