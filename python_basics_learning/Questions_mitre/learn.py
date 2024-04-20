"""
BeautifulSoup
requests
lambda, https://realpython.com/python-lambda/
Python lambdas are little, annoymous functions, give concise syntax than regular python functions
- lambda calculus 
- it does not keep any state
- state based module of computation
- map(), filter(), reduce()
- The title() method returns a string where the first character in every word is upper case. Like a header, or a title. If the word contains a number or a symbol, the first letter after that will be converted to upper case.
- anonymous /lambda functions/lambda expression/ lambda abstractions/lambda form/function literals
"""

# def identity(id):
#     return id

# # lambda(keyword) x(bound variable - argument to a lambda function) : x(body)
# test1 = (lambda x: x+1)(2) 

# # def test2(x):
# #     return x + 1
# test2 = (lambda x: x +1)
# print(test1)
# print(test2(5))
# full_name = lambda first, last : f'Full name : {first.title()} {last.title()}'

# print(full_name('Tanaka', 'Handa'))
higher_order_function = lambda x, func: x + func(x)
print(higher_order_function(2, lambda x : x * x))


