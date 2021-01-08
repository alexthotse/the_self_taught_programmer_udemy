procedual = """
    Procedual Programming is 
    a programmiing style where you write a sequence of steps moving towards a solution.

    i.e. 
        Step [1]
            Step [2]
                Step [3]
            Step [2]
        Step [1]

    Every step changes the state. In procedual you write code like this:
    i.e. 
            do("this")
        then
            do("that")

    So far, you have coded in procedual so to code professionally you need to know either
     ->  functional programmming
     ->  Object Orientated programming

     
"""

example = """
    Here is an example of Procedual programming:

    x, y, z = 2, 4, 8
    xyz = x+y+z
    xyz = 14

    Each line of code changes the state of the program.
    first state is x = 2, then y=4, then z=8
"""

dude="""
    When you program procedually, you store data in global variables and manipulate them with functions.
    i.e.
    collect authors function below.

    Procedual programming is fine when you are building small programs.
    Once your programs become larger, you start to run into issues.
    If you program grows larger you need to add more global variables 
    to keep track of your data.
    
    At certain point, it becomes impossible too keep track of all the global variables
    in your program which can lead to unexpected errors.
    
"""
common_problems = """
    if x = 15, you can easily overwrite the value of x along the way 
    with a different piece of data which changes the original purpose of x.

    This approach of programming relies on side effects.
    Side Effects -> Happens when you change the state of a global variable.

    When you program procedually you will often run into unintended side effects,
    such as:
    -> accidentally incrementing a variable twice

    Procedual led to the develop ment of Functional and Object Orientated programming.
"""
authors = []
def collect_authors():
    answer = None
    while answer != "q":
            answer = input("Best?: ")
            authors.append(answer)

print(authors)

collect_authors()

print(authors)
print()
print(procedual)
print(example)
print(dude)
print(common_problems)


# author = []

# def collect_author():
#     answer = None
#     while answer.lower != "q":
#         answer = input("Who is your favourite author?:->  ")
#         author.append(answer)
# #     print(author)

# if __name__ == "__main__":
#     collect_author()



