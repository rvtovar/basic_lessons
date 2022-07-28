# total = 20


# def printer():
#     total = 30
#     print(f"Inside {total}")


# printer()

# print(f"Outside {total}")


# def max_of_two(x, y):
#     if x > y:
#         return x
#     return y


# def max_of_three(x, y, z):
#     return max_of_two(x, max_of_two(y, z))


# print(max_of_three(3, 6, -5))


from math import prod


def sumOfList(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


total = sumOfList([1, 2, 3])

print(total)


def multOfList(nums):
    product = 1
    for num in nums:
        product *= num
    return product


print(multOfList([1, 2, 3]))

# Create Mult of List


# a is the start of the range and b is the end of the range

def givenRange(num, a, b):
    if num > a and num < b:
        return True
    return False


print(givenRange(10, 8, 15))
