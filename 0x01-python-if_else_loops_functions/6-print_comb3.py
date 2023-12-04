#!/usr/bin/python3

for outer in range(10):
    for inner in range(outer + 1, 10):
        print("{}{}, ".format(outer, inner), end="")

print()
