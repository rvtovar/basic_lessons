from functools import cache
from gettext import find


def printer(name, age):
    print(name)
    print(age)


# printer('rose', 32)


def anyLength(*args):
    print(args)
    for item in args:
        print(item)


# anyLength(10)
# anyLength(10, 20)


def calculation(a, b):
    sum = a + b
    sub = a - b

    return sum, sub


# (sum, sub) = calculation(10, 20)
# print(sum, sub)

def printEmployee(name, salary=9000):
    print(name)
    print(salary)


# printEmployee("Rose", 65000)

# printEmployee('Nick')


def adder(a, b):
    def insideAdder(a, b):
        return a + b

    sum = insideAdder(a, b)
    return sum + 5


# print(adder(10, 20))

def recurAdder(num):
    if num == 0:
        return 0
    else:
        return num + recurAdder(num-1)


print(recurAdder(10))


def display_student(name, age):
    print(name, age)


display_student("Emma", 26)

showStudent = display_student

showStudent('Rose', 31)

print(list(range(4, 30, 4)))


def findlargest(nums):
    largest = -9999999999
    for num in nums:
        if num > largest:
            largest = num

    return largest


x = [4, 6, 8, 24, 12, 2]
print(findlargest(x))
