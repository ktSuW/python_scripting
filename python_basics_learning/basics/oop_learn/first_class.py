#CapWords notation
class MyFirstClass:
    pass

# python -i first_class.py # -i argument tells Python to run the code and then drop to the interactive interpreter
# Create a new object - type a class name with (). Objects will have different memory address they live at 
# a = MyFirstClass()
# b = MyFirstClass()
# print(a)
# print(b)

#-----------------------------------
# # Set artitrary attributes on an instantiated object using dot notation
# class Point:
#     pass 
# # This create an empty Point class with no data/behaviours 
# p1 = Point()
# p2 = Point()
# # Assign these instances 
# # object.attribute = value => dot notation
# p1.x = 5
# p1.y = 4

# p2.x = 3
# p2.y = 6


# print(p1.x, p1.y)
# print(p2.x, p2.y)
#----------------------------------------------
# self argument to a method is a reference to the object that the method is being invoked on.
# constructor, a special method that creates and initializes the object when it is created. Python ia slightly different. It has a constructor and an initializer
# Python initialization method - __init__
import math 

class Point:
    def __init__(self,x,y):
        self.move(x,y)
        
    def move(self, x, y):
        self.x = x
        self.y = y
    def reset(self):
        self.move(0, 0)
    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
        )
 # how to use it:
point1 = Point()
point2 = Point()
point1.reset()
point2.move(5, 0)
print(point2.calculate_distance(point1))
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)
point1.move(3, 4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))

# In python, a method is formatted identically to a function
# The difference between methods and normal functions is that all methods have one required argument. conventionally, it is self.
# print(p.x, p.y)
