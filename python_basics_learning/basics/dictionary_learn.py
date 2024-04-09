"""
dic1 = dict()

dict2 = dict((iterable pairs))

dict3 = dict(zip(iterable, iterable))

dict4 = dict(enumerate(iterable))

dict5 = {}

dict6 = {exp : exp for item in iterable}

dict7 = {(exp, exp) for item in iterable}

dict8 = {(exp, exp) for item in zip(iterable, iterable)}

dict9 = {((exp, exp) for item in enumerate(iterable))}


['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
"""
# list1 = {"A", "B", "C", "D"}
# print(type(list1))
# list2 = ["apple", "banana", "citrus"]
# print(type(list2))
# dict3 = dict(zip(list1, list2))
# print(dict3)

# set1 = {1,3,5}
# set2 = "ABC"
# dict3 = dict(zip(set1, set2))
# print(dict3)
# Extra values will be ignored
# dict3 = dict(zip([1,2,3], (11,22,33,44,55)))
# print(dict3)

print(dir(__builtins__))

#=================================
# It can be a pair of any iterable
# dict2 = dict(((1,"Akai") , (2, "Aoki"), (3, "Midori")))
# dict2 = dict(([1,1,45], [2,20], [3,56])) #ValueError: dictionary update sequence element #0 has length 3; 2 is required
# dict2 = dict(('ab', 'cd', 'ef'))
# list1 = [(1,2), (3,4), (5,6)]
# dict2 = dict(list1)
# print(dict2)
#=======================================
dict5 = {}
for x in range(1,6):
    dict5[x] = 2*x

# print(dict5)
#============================
# dict1 = dict()
# print(type(dict1))
# dict1["apple"] = "red"
# dict1["mango"] = "yellow"
# dict1["grape"] = "purple"

# for x in range(1,6):
#     dict1[x]= x**2
# print(dict1)

#=================================
# dic2 = {
#     101: "Takana",
#     102 : "Yamada",
#     103 : "Sakura"
# }

# # a = dic2[0] # KeyError
# # print(a)
# dic2[104] = "Kentaro"
# # del dic2[4]
# for i in dic2:
#     print(i, dic2[i])


# dicionary
# https://www.youtube.com/watch?v=XYkyKhV5Ifk&list=PLH6mU1kedUy9ScsTt2MCE9k9ung8dy5Yp
# searching O(1)
# pair, entry, item
# Any data type for 
morse_code = {
    "A" : ". -",
    "B" : "- . . .",
    "C" : "- . - .",
    "D" : "- . .",
    "E" : ".",
    "F" : ". . - .",
    "G" : "- - ."
}
print(morse_code)

morse_code3 = {}

morse_code3["A"] = ". -"
morse_code3["B"] = "- . . ."
morse_code3["C"] = "- . - ."
morse_code3["D"] = "- . ."
morse_code3["E"] = "."
morse_code3["F"] = ". . - ."
morse_code3["G"] = "- - ."

print(morse_code3)




# print(morse_code)

x= {"- . - ."} # set
# print(type(x))

morse_code1 = {
    "C" : "- . - .",
    "D" : "- . ."
}
morse_code1["A"] = ". -"
morse_code1["B"] = "- . . ."
# print(morse_code1)


morse_code2 = {
    "A" : ". -",
    "B" : "- . . ."
}
# print(morse_code2)