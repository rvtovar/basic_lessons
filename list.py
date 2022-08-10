names = ['Rose', 'Celty', 'Skye', 'Nick']

# print(names[0])

# print(names[-1])

# print(names[2:])

# print(names[:3])

# print(names[1:3])

# print(names[1:4:2])

# print(names[::-1])


# names[0] = "Vanica"


# print(names)


# nums = [1, 2, 3]

# numsAgain = [4, 5, 6]

# # This means you can concatenate arrays together to form a bigger array
# print(nums + numsAgain)

# nums = nums + numsAgain
# print(nums)

# # removing elements from an array
# del names[3]

# print(names)

# # Methods

# print(names.index('Rose'))

# names.append('Waffles')
# names.append("Johnny")
# print(names)

# # remove

# names.remove("Waffles")

# print(names)

# names.insert(1, "Lucy")
# print(names)

# # sort

# names.sort()
# print(names)
# names.append('ann')
# names.sort(key=str.lower)
# print(names)

# names.reverse()
# print(names)


for name in names:
    print(name)

print('Waffles' in names)
print("Mo" not in names)

cat = ['fat', 'gray', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

size, color, disposition = cat

print(size)

#spam.insert(2, "hello")

spam = ['a', 'b', 'c', 'd']

print(spam[-1])
print(spam[:2])

bacon = [3.14, 'cat', 11, True]
bacon.index('cat')
bacon.append(99)
bacon.remove('cat')
print(bacon*3)

print(bacon[::-1])
