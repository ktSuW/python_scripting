t = ([1,2],[3,4,5])
print(type(t))

# t3 = (2,)
# t3 = (2)
# t3 = tuple(3,6)
# print(type(t3)) # int class or tuple

# t = ()
# print(type(t))
# t1 = tuple()
# print(type(t1))

# t = ("osaka", "nagoya", "tokyo", "kyoto", "niigata")
# print(type(t))
# t[0] = 'nara' # does not support item assignment, immutable,can be heterogenous in nature

# languages =['java', 'python', 'javascript']
# versions = [14, 3, 6]

# # zip takes iterables and aggregates them into a tuple and returns it
# # iterables can be - list, string, dict 
# result = zip(languages, versions)
# print(list(result))


# numbersList = [1, 2, 3]
# str_list = ['one', 'two']
# numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')
# result = zip(numbers_tuple, numbersList)
# print(set(result))

# coordinate = ['x', 'y', 'z']
# value = [3,4,5]

# result = zip(coordinate, value)
# result_list = list(result)
# print(result_list)

#unpacking operator 
"""
c, v = zip(*result_list):
Here, zip(*result_list) uses the unpacking operator * to unpack the list of tuples back into separate lists. The zip function then takes these unpacked tuples as separate arguments. Each tuple argument provides items at a particular index: all first items in one list, all second items in another, and so on.

Specifically, *result_list unpacks result_list into its individual elements, which are tuples. So, *result_list is essentially ('x', 3), ('y', 4), ('z', 5). These are passed to zip as three separate arguments:

('x', 3)
('y', 4)
('z', 5)
zip then pairs the first elements of these tuples together, and the second elements together, effectively reconstructing the original lists:

c will contain all the first elements of the tuples: ('x', 'y', 'z')
v will contain all the second elements of the tuples: (3, 4, 5)
Printing c and v:

print('c=', c) outputs: c= ('x', 'y', 'z')
print('v=', v) outputs: v= (3, 4, 5)
This technique of using zip(*iterable) is commonly employed to unzip or transpose the iterable.

"""
# c,v = zip(*result_list)
# print('c=', c)
# print('v=', v)