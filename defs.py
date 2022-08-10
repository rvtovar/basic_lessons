# 2. Python function that accepts two numbers as arguments and returns the sum
def sum(a, b):
    return a + b

# Python function that accepts different values as parameters and returns a list


def listMaker(a, b, c, d):
    return [a, b, c, d]

#  Python function that accepts a list as a parameter and prints out each item


def listPrinter(items=[1, 2, 3]):
    for item in items:
        print(item)


# 12. Passing an arbitrary number of arguments to a Python function and prints them
def printArgs(*args):
    for arg in args:
        print(arg)
