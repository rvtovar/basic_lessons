# Ask the user for a grade and then you will print a letter grade based on the number.
# if number is too big or small tell them not valid


grade = int(input("Enter a Grade: "))

if grade > 110 or grade < 0:
    print("Invalid Grade")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print("F")
