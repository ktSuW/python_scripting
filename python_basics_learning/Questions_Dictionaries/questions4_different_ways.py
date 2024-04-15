"""
Below are two lists, one for keys and one for values
Create a dictionary from the two lists.

	keys = [ 'key1', 'key2', 'key3', 'key4' ]
	values = [ 11, 22, 33, 44 ]

Example Output:
	{'key1': 11, 'key2': 22, 'key3': 33, 'key4': 44}

BONUS - how many different ways can you achieve the same result.
"""

def method1(keys, values):
    result = {}
    length = min(len(keys), len(values))  
    for i in range(length):
        result[keys[i]] = values[i]  
    
    return result

# zip method - https://www.programiz.com/python-programming/methods/built-in/zip
# zip() function takes iterables 
def method2(keys, values):
    zipped = zip(keys, values)
    result = {}
    for x, y in  zipped:
        result[x]= y
    # result = {k:v for k,v in zip(keys,values)}
    return result 

def main():
    keys = ['key1', 'key2', 'key3', 'key4']
    values = [11, 22, 33, 44]
    result = method1(keys, values)
    print(result)  

if __name__ == "__main__":
    main()
