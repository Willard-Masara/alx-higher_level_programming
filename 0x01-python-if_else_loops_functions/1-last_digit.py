#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10
if last_digit > 5:
    description = "and is greater than 5"
elif last_digit == 0:
    description = "and is 0"
else:
    description = "and is less than 6 and not 0"tas
print(f"Last digit of {number} is {last_digit} {description}")
