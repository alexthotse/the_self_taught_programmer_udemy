concepts = """
    4 Maain concepts in Object-Orientated Programming:
    -> Encapsulation
    -> Abstraction
    -> Inhertiance
    -> Polymorphism


    [*Encapsulation* refers to two concepts]
    [1. Objects group variables, which hold state, and methods that alter the state, in a single units -- the OBJECT.]
    i.e. 

    class Rectangle():
        def __init__(self, w, l):
            self.width = w
            self.length = l

        def area(self):
            return self.width * self.length
    [2. Encapsulation can also mean hiding the classes internal data to prevent the client from directly accessing it.]
    [The code outside of  class that uses an object the CLIENT.] 
    i.e.

    class Data:
        def __init__(self):
            self.nums = [1,2,3,4,5]

        def change_data(self, index, n):
            self.nums[index] = n
    
    data = Data()
    print(data.nums)

    data.nums[0] = 100
    print(data.nums)

    data.change_data(1,99)
    print(data.nums)

    [Problem is if you change this to a tuple, it breaks all your code for your clients expecting a mutable list.]
    [Many programmers solve this by CREATING PRIVATE VARIABLES adn PRIVATE METHODS]
    [Private variables and private methods: variables and methods that objects can access but clients cannot.]
    [Useful when you have a method or variable that your class uses internally 
    but you plan to change the implementation of your code later or want to preserve the flexibility to do so.]

    [Python doesn't have Private variables,  they all Public!!]
    [A public variable is a variable a client can access]
    [Python addresses the problem private variables solve by using NAMING CONVENTIONS]
    [In Py, if you have a variable or method the caller shouldn't access;
    you proceed it's name with an underscore (def _unsafe_method(self))]

    [PPython programmers know if the name of a method or variable starts with an underscore, 
    they shouldn't use it]
    i.e.

    class PublicPrivateExample:
        def __init__(self):
            self.public = "self"        # Yeah go booboo go
            self._unsafe = "unsafe"     # Enter at own risk

        def public_method(self):
            #clients can use this
            pass
        def _unsafe_method(self):
            # clients shouldn't use this
            pass

"""

Abstraction="""
    [Abstraction is the process of taking away or removing characteristics from something 
    to reduce it to a set of essential characteristics.]
    i.e. 
    [Van vogh painting -> Show a representation of a human but there is no fingers, eyebrows, or eyelids.]
    [It is an abstraction of a person.]
    [The painter reduced this person to a set of essential characteristics.]
    [Similarly you can use abstraction in OOP.]
    [When you model objects using classes and omit unnecessary details]

    i.e. 
    class Person:
        def __init__(self, h,w):
            self.height = height
            self.weight = weight

        [but omit other details like hair and eye color]
"""


Polymorphism="""
    [ Polymorphism is the ability in programming to present the same interface for different data types. ]
    [Interface can be a FUNCTION or METHOD]
    i.e.

    [This program presented the same interface: the PRINT function for 3 different DATA TYPES 
    0-> A String; 1-> An Integer; 2-> A Floating Point Number]
    print("Hello World!")
    print(200)
    print(200.1)
    [You didn't have to call and define three separate functions such as
    -> print_str to print(string) to -> print_int to print(int) to -> print_float to print(floating point numbers)]

    i.e.

    [Another example of polymorphism]
    class Triangle():
        def draw():
            pass
        
    class Square():
        def draw():
            pass

    class Circle():
        def draw():
            pass

    [That way you are presenting a common interface for all your different data types]

"""
examples="""
    [I Python didn't support Polymorphisim and you wanted to write a program that takes shapes from a list and draws them.]
    [You would need to use a the type funtion like this.]
    i.e.

    shapes = [tr1, sq1, cr1]
    for a_shape in shapes:
        if type(a_shape) == "Triangle":
            a_shape.draw_triangle()
        if type(a_shape) == "Square":
            a_shape.draw_square()
        if type(a_shape) == "Circle":
            a_shape.draw_circle()



    [But with the ability to present a common interface, your program is much simpler because
    you can iterate through your list of shapes and call the draw method on each object]

    shapes = [tr1, sq1, cr1]
    for a_shape in shapes:
        a_shape.draw()
"""

Inhertiance="""
    [Inheritance in programming is similar to genetic inheritance.]
    [In genetic inheritance you inherit attributes like eye color from your parents.]

    [Similarly classes can inherit methods and variables from another class.]
    [The class that gets inherited from is called the parent class and 
    the class that inherits is called the child class.]
"""
example_inheritance="""

    [You can create a child class that inheriits from a parent class 
    by passing the name of the parent as a parameter to the child when you create it.]
    [Because of inheritence you can create a square object]

    class Shape():
        def __init__(self, w, l):
            self.width = w
            self.len = l

        def print_size(self):
            print("""{} by {}""".format(self.width, self.len))

    class Square(Shape):
        pass #keyword that tells Python not to do anything.
        [this reduction in code is important because avoiding repeating code 
        makes your program smaller and more manageable]

    
    [When a child class inherits a method from a parent class, you can overwrite it 
    by defining a new method with the same name.]
    [This process is called Method Overwriting]
    [In this case beacuse you defined a method named print size in your child's class,
    The newly defined method overrides the parent method of the same name and prints a new message when you call it.]

    class Shape():
        def __init__(self, w, l):
            self.width = w
            self.len = l

        def print_size(self):
            print("""{} by {}""".format(self.width, self.len))

    class Square(Shape):
        def print_size(self):
            print("override")

    a_square = Square(20, 20)
    a_shape.print_size()


    a_shape = Shape(20, 20)
    a_shape.print_size()

    >>> 'override'
------------------------------------------------------------
>>> class Shape:
...     def __init__(self, w, l):
...             self.width = w
...             self.len = l
... 
>>> class Shape:
...     def __init__(self, w, l):
...             self.width = w
...             self.len = l
...     def print_size(self):
...             print("""{} by {}""".format(self.width, self.len))
... 
>>> class Square(Shape):
...     pass
... 
>>> a_shape = Shape(20, 20)
>>> a_shape.print_size()
20 by 20
>>> 


"""