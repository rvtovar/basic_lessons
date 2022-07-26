# FizzBuzz

# Ask the user for a number

# if the number is divisible by 5 print buzz
# if the number is divisible by 3 print fizz
# if the number is divisble by both 5 and 3 we will print fizzbuzz


maxNum = int(input("Enter a whole number: "))

# Loop that goes from 1 to maxNum

# 1
# 2
#3 - Fizz
# 4


for num in range(1, maxNum+1):

    if num % 5 == 0 and num % 3 == 0:
        print(f'{num} - FizzBuzz')
    elif num % 3 == 0:
        print(f'{num} - Fizz')
    elif num % 5 == 0:
        print(f"{num} - Buzz")
    else:
        print(num)
