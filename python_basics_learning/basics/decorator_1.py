# decorator demo 1 - simple

def decorator_cake(input_func):
    def inner_cake():
        print('Send the basic cake to special cake decorator shop')
        print('Display the cake after decorating')
    return inner_cake

# Python vm will check if there any decorator configured for that particular function
# display is an input function
# original function display is not taking argument. The number of arguments in orignial function and inner function must match
@decorator_cake
def display():
    print('Displaying a cake as it is')
    
display()