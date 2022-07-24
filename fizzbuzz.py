# FizzBuzz

# Ask the user for a number

# if the number is divisible by 5 print buzz
# if the number is divisible by 3 print fizz
# if the number is divisble by both 5 and 3 we will print fizzbuzz


num = int(input("Enter a whole number: "))

if num % 5 == 0 and num % 3 == 0:
    print(f'{num} - FizzBuzz')
elif num % 3 == 0:
    print(f'{num} - Fizz')
elif num % 5 == 0:
    print(f"{num} - Buzz")
else:
    print(num)
