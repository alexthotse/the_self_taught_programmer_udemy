dude="""
    [You will learn more important concepts in OOP:]
    [-> Class variables
    -> Instance variables
    -> Magic methods
    -> the keyword "is"]


    [Class Variables vs Instance Variables]
    [Everything in Python is an object]
    i.e. 

    class Square:
        pass

    print(Square)
    >>> <class '__main__.Square'>

    [Classes have to kinds of variables:
    1-> Class variables: Belongs to the object and the objects class.
    2-> Instance variables : Belongs to the object]

    [Class variables are useful because you can use them to share the data
    between all instances of a class without relying on global variables.]

    i.e.
    [In this example, width and len are instance variables.]
    [You can define a class variable by creating a variable inside of a class without using self like this(self.recs)]
    [RECS is a class variable you defined outside of the init method because init only gets called when you create an object.]
    [Now whenever Python creates a new Rectangle object, it calls the init function which has code 
    that appends a tuPLE containing the object's length and width to RECS]
    [This allows you to print a list of data about every object.]
    class Rectangle():
        recs = []
        def __init__(self, w, l):
            self.width = w
            self.len = l
            self.recs.append((self.width, self.len))
        def print_size(self):
            print("""{} by {}""".format(self.width,self.len))


[This design enables you to share data between the different objects created by this class, 
without having to use a global variable]
>>> class Rectangle:
...     recs = []
...     def __init__(self, w, l):
...             self.width = w
...             self.len = l
...             self.recs.append((self.width, self.len))
...     def print_size(self):
...             print("""{} by {}""".format(self.width, self.len))
... 
>>> rect_one = Rec
Rectangle(       RecursionError(  
>>> rect_one = Rectangle(3,4) # Each time you create a new Rectangle, Python appends it to your RECS list
>>> rect_two = Rectangle(9,9) # Each time you create a new Rectangle, Python appends it to your RECS list
>>> rect = Rectangle
>>> print(rect)
<class '__main__.Rectangle'>
>>> print(rect.recs) # You can use a Rectangle class object to print the list.
[(3, 4), (9, 9)]
>>> print(rect.recs[0])
(3, 4)
>>> print(rect.recs[0][1])
4
>>> print(Rectangle.recs)
[(3, 4), (9, 9)]
>>> rect_three = Rectangle(65,44)
>>> print(Rectangle.recs)
[(3, 4), (9, 9), (65, 44)]


[]
"""


lion = """
    [Every class in Oython inherits from a parent class called object.]
    [Python uses the methods it inherits from Objects in different situations,
    like when you print an object]
    [When you print an object Python calls a magic method called REPR inherited from object 
    and prints whatever the method returns]
    [By default it prints information about the object like it's type and location in memory.]
    [You can override this method to change what prints]
    i.e.

    class Lion:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name
             
    lion = Lion("Dilbert")
    print(lion)         # <class '__main__.Lion object at 0x7f926ac90550'>
    print(lion.name)    # Dilbert


>>> class Lion:
...     def __init__(self, name):
...             self.name = name
... 
>>> lion = Lion("Alex")
>>> print(lion)
<__main__.Lion object at 0x7f926ac90550>
>>> 
>>> 
>>> print(lion)
<__main__.Lion object at 0x7f926ac90550>
>>> print(lion.name)
Alex
>>> class Lion:
...     def __init__(self, name):
...             self.name = name
...     def __repr__(self):
...             return self.name
... 
>>> print(Lion)
<class '__main__.Lion'>
>>> lion = Lion("Alex")
>>> lion
Alex
>>> 


"""

unique="""
    [Python reiles on magic methods when it evaluates expressions.]
    i.e.
    [This expression, each integer object has a magic method named ADD that Python calls when it evaluates the expression.]
    2 + 2
    [If you override this method you can create objects that perform additions however you want.]

    class AlwaysPositive:
        def __init__(self, number):
            self.n = number

        def __add__(self, other):
            return abs(self.n + other.n)

    x = AlwaysPositive(-90)
    y = AlwaysPositive(10)

    print(x + y)
    print(f"Difference between x and y is {x+y}")
    Difference between x and y is 80
    
"""

is_keyword = """
    [The keyword is returns True if the operands on either side pf it are the same object and 
    false if not.]

    i.e. 

    class Person:
        def __init__(self):
            self.name = 'bob'
    bob = Person()
    same_bob = bob
    print(bob is same_bob)
    [When you use the keyword is in an expression with the objects Bob and same_Bob as operators,
    the expression evaluates to true because both variables points to the same person object.]
    [When you create a new person object and compare it to the original bob, 
    the expression evaluates to false because the variables point to different person objects.f]

    another_bob = Person()
    print(bob is another_bob)


>>> class Person:
...     def __init__(self):
...             self.name = 'bob'
... 
>>> bob = Person()
>>> same_bob = bob
>>> print(bob is same_bob)
True
>>> another_bob = Person()
>>> print(bob is aanother_bob)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'aanother_bob' is not defined
>>> print(bob is another_bob)
False

"""