# dict = {
#     "name": "Rose",
#     "age": 31,
#     "job": "Instructor"
# }


# # print(dict["age"])

# # for key in dict:
# #     print(dict[key])

# # for value in dict.values():
# #     print(value)


# # dict['name'] = "Skye"
# # print(dict)


# # Create a Dictinary representing a dog, include a name, breed, and legs
# dog = {
#     "name": "Fito",
#     "breed": "German Shepard",
#     "legs": 4
# }

# # Create a dictinary representing States, Keys are Initials, values are state name 5 states

# states = {
#     "TN": "Tennessee",
#     "GA": "Georgia",
#     "AZ": "Arizona",
#     "NY": "New York",
#     "NM": "New Mexico"
# }

# # Birthday App

# birthdays = {
#     'Rose': "Jan 25th",
#     "Skye": "Nov 14th",
#     "Nick": "Aug 28th"
# }

# print(birthdays)

# while True:
#     name = input("Enter a name (blank to quit): ")
#     if name == "":
#         break

#     if name in birthdays:
#         print(f"{birthdays[name]} is the birthday of {name}")
#     else:
#         print(f"We do have have the information for {name}")
#         bday = input("Supply Birthday: ")
#         birthdays[name] = bday
#         print("birthday database updated")


# print(birthdays)

# Create a Fantasy Inventory Program.
# Ask the user for a item and tell them how much they have
# if its not in the dictionary you will add the item and ask how many they have


inventory = {}

while True:
    item = input("What item are you looking for? (blank to move on) ")
    if item == "":
        break

    if item in inventory:
        print(f"You have {inventory[item]} of {item}")
    else:
        print(f"{item} is not in inventory, how much are we adding ")
        amount = int(input())
        inventory[item] = amount
        print("Inventory updated")


print(inventory)
