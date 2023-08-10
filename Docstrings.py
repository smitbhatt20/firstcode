#Docstrings:A Python docstring is a string used to document a Python module, class, function or method,

def square(n):
    ''' Takes a number n, returns # it is not comment ist is docstring (IMP for Interview)
    the square of n'''
    print(n**2)

square(5)
print(square.__doc__) #this command is used to print the docstring
#Docstring is only written in the first part of the body


#PEP 8
#This document gives coding conventions for the Python code comprising the standard library in the main Python distribution.


#Exceptions:An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions

try:
    #some lines of code
except <ERROR1>:
    #handler <ERROR1>
except <ERROR2>:
    #handler <ERROR2>
else:
    #if there is not error type else:
