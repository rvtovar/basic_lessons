# dict = {
#     "Rose": "Jan 25th",
#     "Skye": "Nov 14th",
#     "Nick": "Aug 28th"
# }


# # for value in dict.values():
# #     print(value)

# for item in dict.items():
#     print(item)


# print("Celty" not in dict)


# print(dict.get('Celty', 'Jan 1st'))

# dict.setdefault("Celty", "Apr 5th")

# print(dict)


dict2 = {
    "names": ['Rose', "Skye", "Nick", "Celty"],
    "hobbies": {
        'Rose': ['Monster Hunter', "Destiny 2", "Data Science", "Reading"],
        'Skye': ['Monster Hunter', "Monster Hunter", "Monster Hunter"],
        "Nick": ["Sleeping", "Monster Hunter", "Destiny 2"]
    }
}

print(dict2['hobbies']['Rose'][2])


nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(nums[0][0])


ppl = [
    {
        'Name': "Rose",
        'Age': 31,
        "Color": "Purple"
    }, {
        'Name': "Skye",
        'Age': 32,
        "Color": "Pink"
    }, {
        'Name': "Nick",
        'Age': 24,
        "Color": "Blue"
    }
]

print(ppl[1]["Age"])

emptydict = {
    "foo": 42
}

print(emptydict['bar'])
