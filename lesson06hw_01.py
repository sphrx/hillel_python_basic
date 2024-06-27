"""
This program takes two letters separated by a dash as input
and returns all the characters between them (inclusive).
"""

import string as s

a, b = input("Enter two letters separated by a dash: ").split("-")
print("".join(s.ascii_letters[s.ascii_letters.index(a):s.ascii_letters.index(b) + 1]))
