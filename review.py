names = ['Rose', "Skye", "Nick", "Celty"]


def itemSwap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp
    return list


newList = itemSwap(names, 0, 3)

print(newList)


def min(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2


print(min(10, 20))


def reverse(list):
    return list[::-1]


print(reverse(names))


# Finding Biggest Number in a list

nums = [20, 30, 10, 31, 78, 3]


def biggest(list):
    largest = -9999999999
    for num in list:
        if num > largest:
            largest = num
    return largest


print(biggest(nums))


def printEven(list):
    for num in list:
        if num % 2 == 0:
            print(num)


printEven(nums)
