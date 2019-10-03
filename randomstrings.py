#!/usr/bin/env python3

import sys, random

def main(num_ints, num_digits):
    for _ in range(num_ints):
        i = 0
        for d in range(num_digits):
            i += random.randint(0, 9) * (10 ** d)
        print(i)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
