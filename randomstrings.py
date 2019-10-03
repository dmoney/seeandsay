#!/usr/bin/env python3

"""
Usage: ./randomstrings.py N M

Produces N lines of up to M random decimal digits.
E.g.:

    ./randomstrings 10 5

produces 10 lines of up to 5 digits each.  A line may
have fewer digits because leading zeroes are not displayed.

This is used to feed ./seeandsay.py, which counts occurrences
of each digit, per line.

You are probably looking for lookandsay.py, which does something else.
See the README for what this is all about.
"""

import sys, random

def main(num_ints, num_digits):
    for _ in range(num_ints):
        i = 0
        for d in range(num_digits):
            i += random.randint(0, 9) * (10 ** d)
        print(i)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
