#!/usr/bin/python3

results = "".join(chr(i) if i % 2 == 0 else chr(i).upper()
                  for i in range(ord('z'), ord('a') - 1, -1))

print("{:s}".format(results), end="")
