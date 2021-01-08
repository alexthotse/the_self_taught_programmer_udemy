
object = """
    Obeject Oriented Paradigm also ELIMINATES global state.
    Instead of storing state in functions, you store STATE IN OBJECTS!!!
    Everything in Python is an object from:
    "Strings" to 123 (integer)

    You create an object using something called a CLASS.

    [Class : A blueprint for creating objects in Python.]
    [Every object is an INSTANCE of a CLASS which means:
    the OBJECT DATA TYPE is the CLASS that created it.]

    i.e. str() 
    A string in Python has the data type string because behind the scences Python creates it,
    with the String Class.

    You can use a class to creatte instances of your own objects.  
    i.e. You want to model Oranges in Python; you can use a class to create the blueprint of an 
    Orange. And then use that blueprint to create different instances of orange objects.
"""

example = """
    class Orange:                   
        #Class called Orange and class names should always start with an UPPERCASE LETTER
        #And always use CamelCase; which means if a class name has more than one word,
        #  you should always Capitailize the first letter of every word i.e. class LikeThis
        
        #Defining a method
        def __init__(self):     
            print("Created!)

        [Methods : are like functions that you call on objects.]
        [You define a method inside of a class.]
        [Then when you use a class to create an object, you call the method you defined on it.]
        [Methods names like Function names shoould be lowercase with words separated by underscores.]
        [Once you've defined a class, you can use it to create an object by writing a class's name
        followed by parentheses, creating a new object is called instantiating a class.]

        i.e.
>>> class Orange():
...     def __init__(self):
...             print("Created with Love!")
... 
>>> orange = Orange()
Created with Love!
>>> 
___END___
This happens because the code that prints "Created withLove!" 
is defined inside of a method called __init__.

[__init__ : defining a special method]

Python calls everytime you create a new object using that class. 
[Any method surrounded by double underscorces is called a magic method.]
[A method Python uses for special purposes like creating an object.]
[When you define a method it must always accept at least ONE PARAMETER except for special cases.]
[The convention in Python is always to name this parameter *self*.]
[he reason methods have to accept at least one parameter is because when you call a method,
Python passes the object the method was called on back it as a parameter.]
i.e.

>>> class Orange:
...     def __init__(self):
...             print(self)
... 
>>> orange = Orange()
<__main__.Orange object at 0x7f41012a13c8>
>>> print(orange)
<__main__.Orange object at 0x7f41012a13c8>
>>> 
___END___
{When you create a new orange object and print it; Python tells you it is an orange object.}
{When you print the parameter self, Python prints the same thing because 
Python passes in the orange object as the parameter self}
{When you create a new object you don't have to pass in *SELF* because Python does it Automatically}









"""

instance = """
[You can use self to define an insstance variable, a variable that belongs to an object like this]
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created")
[You should always define instance variables inside __init__ except in special cases]
[If you create multiple objects, they can all have different instance variable values]

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c

orange_one = Orange(2, "orange")
orange_two = Orange(9, "light orange")
orange_three = Orange(7, "dark orange")

print(orange_one)
print(orange_one.weight)
print(orange_one.color)
print("\n")

print(orange_two)
print(orange_two.weight)
print(orange_two.color)
print("\n")

print(orange_three)
print(orange_three.weight)
print(orange_three.color)
print("\n")

[Once you've created an object you can get the value of it's instance variables like this.]
[You can print orange ones weight and height like this]


class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created")
[You should always define instance variables inside __init__ except in special cases]
[If you create multiple objects, they can all have different instance variable values]

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c

or1 = Orange(10, "dark orange")
print(or1.weight)
print(or1.color)
print("\n")

or1.weight = 100
or1.color = "light orange"
print(or1.weight)
print(or1.color)
print("\n")


[You can change the value of an instance variable like this.]
[ in case your orange objects weight started at 10 but you changed it to 100]
[It's color started as dark orange but you changed it to light orange]
[Theree's more to an orange than it's physical properties like color and weight.]
[Oranges also do things like rot that you can model with methods.]

[Here's how you can give an orange the ability to rot]


class Fruit:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0

    def rot(self, days, temp):
        self.mold = days * temp

fruit = Fruit(6, "orange")
print(fruit.mold)
fruit.rot = (10,98)
print(fruit.mold)

[Here's you can give an Orange the ability to rot, rot accepts two parameters.]
[Number of days since someone picked the orange and the average temperature during that time.]
[When you call it, this method uses a made up formula to increment mold which works to increment mold,
which works because you can change the value of an instance variable inside of any method.]
"""
multiple = """
    [You can define multiple methods in a class.] 
    class Rectangle():
        def __init__(self, w,l):
            self.width = w
            self.len = l

        def area(self):
            return self.width * self.len

        def change_size(self, w, l):
            self.width = w
            self.len = l

    [Here is an exaample of modeling a rectangle with a method to calculate it's area and another method to change it's size.]
    [In this example Rectangle objects have two instance variables LEN and WIDTH.]
    The area method returns the area of the rectangle object by multiplying the instance variables together 
    [The change_size method changes them by assigning them to the numbers the caller passes in
    as parameters]

"""

composition="""
    Object Orientated Programming allows you to model a "has a" 
    relationship by storing an object as a variable in another object.
    The formal name is Composition.

    i.e.
    class Dog():
        def __init__(self, name, breed, owner):
            self.name = name
            self.breed = breed
            self.owner = owner
    class Person():
        def __init__(self, name):
            self.name

    mick = Person("Mick Jagger")
    stan = Dog("Stanley", "Bulldog",mick)
    print(stan,owner,name)

    [you can use composition to represent the RELATIONSHIP between a DOG and it's OWNER 
    by MODELLING that a dog has an owner.]
    [1st you define classes to represent dogs and people then when you create a dog object,
     you pass in a person object as the owner parameter.]
     [Now the dog object named Stanley has an owner: a person object named Mick Jagger]

"""

detailed = """

More detailed example:
>>> class Orange:
...     def __init__(self, create):
...             self.create = create
...     def create(self):
...             return f"{self.create}"
... 
>>> fruit = Orange("Banana")
>>> print(fruit)
<__main__.Orange object at 0x7f41012a1160>
>>> print(fruit.create)
Banana
>>> 
___END___
"""

advantages="""
OOP has several advantages:
-> it encourages code reuse
-> thus decreases the amount of time spent in developing and maintaining code.
-> Encourages breaking problems up into multiple pieces 
-> which results in code that is easy to maintain
"""

disadvantage="""
A disadvantage of OOP is that:
-> Creating programs takes extra effort 
-> Because a great deal of planning is involved in designing them.


"""


