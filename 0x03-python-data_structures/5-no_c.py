#!/usr/bin/python3

def no_c(my_string):
    new_string = [
        character for character in my_string if character not in "Cc"]
    return ("".join(new_string))
