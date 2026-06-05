x = 5
name = "Tonny"
print(x)
print(name)

# check Rules for variable names
# 1. Variable names can only contain letters, numbers, and underscores
# 2. Variable names cannot start with a number
# 3. Variable names are case-sensitive, meaning that "name" and "Name" are considered different variables
# 4. Keywords such as if, else and for cannot be used as variable names.
"""
    The list of keywords are: 
        ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    """

Name = "Alice"
print(Name)

# Basic assignment
x = 10
y = 20
z = 'Hello, World!'
print(x, y, z)

# Dynamic typing
x = 3
print(x)
x = "Now I'm a string"
print(x)

# Assigning same value to multiple variables
a = b = c = 100
print(a, b, c)

# Assigning values to multiple variables in one line
x, y, z = 1, 2, "Python"
print(x, y, z)

# Object reference

x = 5
y = x  # y now references the same object as x
print(x, y)  # Output: 5 5

y = 10  # y now references a new object, x still references the original object
print(x, y)  # Output: 5 10

x = "Hello"  # x now references a new object, y still references the original object
print(x, y)  # Output: Hello 10 , 5 is garbage collected

# deleting variables
a = 27
print(a)  # Output: 27
del a  # deletes the variable a
# print(a)  # This will raise a NameError since a has been deleted

# Swapping two variables
a, b = 5, 10
print("Before swapping: a =", a, "b =", b)  # Output: Before
a, b = b, a
print("After swapping: a =", a, "b =", b)  # Output: After

# Counting Characters in a String
word = "Hello, My name is Tonny"
# char_count = len(word)
# print('The number of characters in the string is:', len(word))
print(f"The number of characters in the string is: {len(word)}")
# f is used for string formatting
