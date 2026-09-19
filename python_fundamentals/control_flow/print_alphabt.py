#!/usr/bin/env python3

alphabet = ""

for number in range(97, 123):
    letter = chr(number)
    if letter != "e" and letter != "q":
        alphabet += letter

print("{}".format(alphabet), end="")
