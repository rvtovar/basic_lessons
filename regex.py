# # Regular Expressions
from atexit import register
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

# phoneRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")

# mo = phoneRegex.search('My numbers are 901-901-0000 and 800-777-8989')


# print(mo.group())


# numbers = phoneRegex.findall('My numbers are 901-901-0000 and 800-777-8989')

# print(numbers[0])


"""
\d any numeric digit
\D any non numeric character
\w Any letter, numeric character, or underscore
\W any character not a letter, digit, or underscore
\s any space tab, or new line
\S Any character not a space tab or new line

"""

# xmasRegex = re.compile(r"\d+\s\w+")

# print(xmasRegex.findall('12 drummers, 11 pipers, 1 partridge'))


# vowelRegex = re.compile(r"[^aeiouAEIOU]")

# print(vowelRegex.findall('Robocop eats babyfood. BABY FOOD'))


# re.compile(r"[^a-zA-Z0-9]")

# Carrot Symbol and Dollar Sign

# ro = re.compile(r"^Hello")

# print(ro.search("Hello World").group())


# ends = re.compile(r"\d$")

# print(ends.search('42').group())


# whole = re.compile(r"^\d+$")

# print(whole.search('90d2'))


# The Wild Card Method

# atRegex = re.compile(r".at")

# print(atRegex.findall('Cat Bat bat cat mat sat hat'))


# nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")

# mo = nameRegex.search("First Name: John Last Name: Smith")

# print(mo.groups())


# non = re.compile(r"<.*?>")

# mo = non.search('<Help im> But im >')

# print(mo.group())

# greedy = re.compile(r"<.*>")

# mo = greedy.search('<Help im> But im >')

# print(mo.group())


# newline = re.compile('.*', re.DOTALL)

# print(newline.search('Serve the public\nProtect the innocent'))


# Case sensitivity

robocop = re.compile(r'robocop', re.I)

print(robocop.search('RoboCop'))

nameRegex = re.compile(r"Agent (\w)\w*")

print(nameRegex.sub('CENSORED',
      'Agent Alice told Agent Carol that Agent Eve knows Agent Bob was a double agent'))


print(nameRegex.sub(r'\1****',
      'Agent Alice told Agent Carol that Agent Eve knows Agent Bob was a double agent'))


phoneRegex = re.compile(r'''(
    \d{3}|\(\d{3}\))?
    (\s|-|\.)
    \d{3}
    (\s|-|\.)
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})?
''', re.VERBOSE)
