difference = """
    The main difference between the various programming paradigms os the handling of state.
    [State : The value of a program's variable while it is running.]
    [Global State : The  value of the program's global variable while it is running.]

    Functional programming is a programming paradigm that addresses the problems that 
    arise in procedual programming by *ELIMINATING GLOBAL STATE*.

    Functional programmers DO NOT use GLOBAL VARIABLES!
    Instead they keep track of data by passing it as a parameter fromm one function to another.

    KEY CONCEPT: In functional programming, you write programs that 
    -> do not rely on or change any global state

"""

procedual = """
    Here is an example:
    [Procedual Programming]
    a = 0

    def increment():
        global a
        a += 1

    A functional programmer would not like this function because:
    -. it relies on data OUTSIDE ofITSELF and,
    -> it CHANGES DATA OUTSIDE of the current function by INCREMENTING a GLOBAL VARIABLE.
"""

functional = """
    {Functional Programming}
    Here is a function a functional programmer would like because 
     DOES NOT RELY ON OR CHANGE ANY DATA OUTSIDE of ITSELF!
    i.e. f{x} - > {x}
     def increment(a):
         return a + 1
"""

advantage = """
    One advantage of Functional programming is that it:
    -> eliminattes an entire category of errors caused by GLOBAL STATE. 
"""

disadvantage = """
    Disadvantage of functional programming is certain problems are:
    -> easier to conceptualize with state.

    i.e. 
    it is easier to think about designing a user interface using global state.
    on = True /// off = False

    
"""

print(difference)
print(procedual)
print(functional)
print(advantage)
print(disadvantage)