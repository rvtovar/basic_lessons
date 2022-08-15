# # Regular Expressions
import re


# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False

#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False

#     if text[7] != '-':
#         return False

#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False

#     return True


# # print(isPhoneNumber("901 283 7198"))


# phoneNumberReg = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# mo = phoneNumberReg.search("My number is 900-900-0000")

# print(mo.groups())

# areacode, mainNumber = mo.groups()

# print(areacode)
# print(mainNumber)


# num = "(900) 900-9999"

# phoneNumberReg = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

# mo = phoneNumberReg.search(num)

# print(mo.groups())


# """
# . ^ $ * + ? ( ) [ ] \ | { }

# \{  \}
# """


# # Pipe Operator

# heroRegex = re.compile(r'Batman|Tina Fey')

# mo1 = heroRegex.search('Batman and Tina Fey')

# mo2 = heroRegex.search('Tina Fey and Batman')

# print(mo1.group())
# print(mo2.group())


# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

# mo = batRegex.search("Batmobile lost a wheel")

# print(mo.group(1))

# Optional matching ?

# batRegex = re.compile(r"Bat(wo)?man")

# mo1 = batRegex.search("The adventures of Batman")

# print(mo1.group())


# mo2 = batRegex.search('The adventures of Batwoman')
# print(mo2.group())


# phoneRegex = re.compile(r"(\d\d\d-)?(\d\d\d-\d\d\d\d)")

# mo1 = phoneRegex.search('800-800-9000')
# print(mo1.group())

# Matching Zero or more characters with *

# batRegex = re.compile(r"Bat(wo)*man")

# mo1 = batRegex.search('Batwowowowowowowowowowoman')
# mo2 = batRegex.search('Batman')

# print(mo1.group())
# print(mo2.group())

# We can also match one or mor etimes and that uses +

# batRegex = re.compile(r"Bat(wo)+man")

# mo1 = batRegex.search('Batman')
# print(mo1 == None)

# mo2 = batRegex.search('Batwoman')
# print(mo2.group())

# mo3 = batRegex.search('Batwowowoman')
# print(mo3.group())


# Matching specific repetitions with braces {}

# haRegex = re.compile(r"(Ha){3,5}?")

# mo1 = haRegex.search('HaHaHa')
# print(mo1.group())

# mo3 = haRegex.search('HaHaHaHa')
# print(mo3.group())

# mo4 = haRegex.search('HaHaHaHaHa')
# print(mo4.group())

# mo2 = haRegex.search('HaHa')
# print(mo2 == None)

# Findall method

phoneRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")

mo = phoneRegex.search('My numbers are 901-901-0000 and 800-777-8989')


print(mo.group())


numbers = phoneRegex.findall('My numbers are 901-901-0000 and 800-777-8989')

print(numbers[0])

tuples = ('hello', 'Hello')
