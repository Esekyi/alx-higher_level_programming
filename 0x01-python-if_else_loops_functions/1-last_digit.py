#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# converting the object int into string and slicing to get last element
last_digit_str = repr(number)[-1]
last_digit = int(last_digit_str)  # converting string to integer

if last_digit < 6 and last_digit != 0:
    if number < 0 and last_digit != 0:
        print("Last digit of {} is -{} and is less "
              "than 6 and not 0".format(number, last_digit))
    else:
        print("Last digit of {} is {} and is "
              "less than 6 and not 0".format(number, last_digit))
elif last_digit > 5:
    if number > 0 and last_digit != 0:
        print("Last digit of {} is {} and is greater "
              "than 5".format(number, last_digit))
    else:
        print("Last digit of {} is -{} and is less than "
              "6 and not 0".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
