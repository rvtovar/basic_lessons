# # # print("She said \"Holy crap batman\"")
# # # print('She said "Holy Crap Batman"')

# # # print('I\'m doing well')

# # # print("Hello there!\n\tHow are you?\nI\'m doing fine.")

# # # name = "Rose"

# # # print(f'''
# # #     I'm very tired and sleepy
# # #     HOly Crap Batman
# # #         Bacon is amazing
# # #         {name}
# # #     People are aslee
# # # ''')

# # # Comments

# # """
# #     This is a multiline comment
# #     i can add as much as i want
# #     to this
# # """


# # spam = "Hello, World!"

# # print(spam[5])

# # print(spam[-1])
# # print(spam[0: 5])
# # print(spam[:5])

# # print(spam[7:])

# # fizz = spam[7:]
# # print(fizz)


# # print("Helo" not in spam)

# # print('Hello'.upper())
# # print("World".lower())

# # print("HELLO".isupper())

# # print('hello'.islower())


# # # isAlpha
# # print("3".isalpha())


# # # isalnum
# # print("hello23".isalnum())


# # # isdecimal
# # print("123.23".isdecimal())

# # isspace
# # print("     ".isspace())
# # print(" Hello".isspace())

# # # is title
# # print("Hello Cruel World 123".istitle())
# # print("Hello there".istitle())


# # while True:
# #     print("Enter your age")
# #     age = input()
# #     if age.isdecimal():
# #         break
# #     print("Please Enter your age")


# # while True:
# #     print("Select a new password (Letters and numbers only.) ")
# #     pwd = input()
# #     if pwd.isalnum():
# #         break
# #     print("Passwords can only have letters and numbers")


# # Startswith

# # print("Hello there".startswith("Helo"))

# # # Endswith
# # print("Hello There".endswith("e"))


# # # Join and Splitting a string

# # splits = "My name is Rose".split("y")
# # print(splits)

# # lists = "MyABCnameABCisABCRose".split("ABC")
# # print(lists)


# # string = ":".join(lists)
# # print(string)


# # spam = '''Dear Alice,
# # How have you been? I am fine.
# # There is a container in the fridge
# # that is labeled "Milk Experiment"

# # Please do not drink it.
# # Sincerly,
# # Bob'''

# # lists = spam.split("\n")

# # print(lists)


# # print("\n".join(lists))

# # string = ""

# # Partition Method

# # print("Hello World".partition('W'))

# # # rjust ljust and center

# # print('hello'.rjust(10, "*"))
# # print("Hello World".ljust(10, "-"))

# # print('Hello'.center(10, "_"))


# # R strip, L Strip, and Strip

# spam = '           Hello World                   '

# print(spam)
# print(spam.strip())

# print(spam.rstrip())
# print(spam.lstrip())


# # Numeric values of characters

# print(ord("C"))

# num = ord("D")
# print(chr(num + 1))


# What are escape characters?
"""
\n \t \\ \' \"
"""

string = "Howl's Moving Castle"


multline = '''This is a multiline
string
YAY'''


# print("Hello, World"[1])
# print('Hello, World'[0:5])
# print("Hello, World"[:5])
# print('Hello, World'[3:])

# print("hello".upper())
# print("Hello".upper().isupper())
# print("hello".upper().lower())

print("Remember, remember, the fifth of November".split())

print('-'.join('There can be only one'.split()))
