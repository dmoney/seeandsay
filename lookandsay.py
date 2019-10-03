"""
Computes the Look And Say sequence.

Usage:  python3 lookandsay.py STARTING_NUMBER NUMBER_OF_STEPS

The Look And Say sequence starts with a given positive integer,
and each subsequent number is constructed from the digits of the
previous one.  For example,

    python3 lookandsay.py 1223334444 5

To describe the number 1223334444, you might say that it has
one 1, two 2's, three 3's, followed by four 4's.

So you could express it as 11223344.  And the next step
is computed from that, and so forth:

    $ python3 lookandsay.py 1223334444 5
    11223344
    21222324
    121132131234
    1112211312111311121314
    3122211311123113311211131114

Fair warning: by about 45, entries have thousands or millions of digits.

This is meant to be used for some benchmarks, which are described
in the README.
"""

import sys, io

def look_and_say_next(i):
    counts = []
    current_digit = int(str(i)[0])
    current_length = 0
    for digit in (int(d) for d in str(i)):
        if digit == current_digit:
            current_length += 1
        else:
            counts.append((current_length, current_digit))
            current_digit = digit
            current_length = 1
        # if counts:
        #     print(counts[-1])
    counts.append((current_length, current_digit))
    outstr = ""
    for c in counts:
        outstr += str(c[0]) + str(c[1])
    return int(outstr)


def look_and_say_seq(i):
    while True:
        i = look_and_say_next(i)
        yield i

def look_and_say_next_str(i):
    #counts = []
    outstr = io.StringIO()

    i.seek(0)
    current_digit = i.read(1)
    # print("current digit: " + current_digit)
    i.seek(0)
    current_length = 0
    while i.readable():
        raw = i.read(1)
        if raw is None or raw == "":
            break
        digit = raw

        # print("digit: " + digit)
        if digit == current_digit:
            current_length += 1
        else:
            #counts.append((current_length, current_digit))
            outstr.write(str(current_length))
            outstr.write(current_digit)

            current_digit = digit
            current_length = 1
        # if counts:
        #     print(counts[-1])

    #counts.append((current_length, current_digit))
    outstr.write(str(current_length))
    outstr.write(current_digit)

    #with io.StringIO() as outstr:

    #outstr = io.StringIO()
    # for c in counts:
    #     outstr.write(str(c[0]) + c[1])

    #return outstr.getvalue()
    return outstr


def look_and_say_seq_str(i):
    while True:
        i = look_and_say_next_str(i)
        yield i

def memostr(val):
    """memoized str()"""
    if val not in memostr.cache:
        memostr.cache[val] = str(val)
    return memostr.cache[val]
memostr.cache = {}

def look_and_say_seq_from_seq(digits):
    current_digit = None
    current_count = 0
    for digit in digits:
        #print("DIGIT: ", digit)
        if current_digit is None:
            current_digit = digit
        #print("in loop: ", (current_count, current_digit))
        if digit == current_digit:
            current_count += 1
        else:
            yield memostr(current_count)
            yield current_digit
            current_count = 1
            current_digit = digit
    #print("out of loop: ", (current_count, current_digit))
    if current_digit is not None:
        yield memostr(current_count)
        yield current_digit
    else:
        raise Exception(f"current_digit: {current_digit}, current_count: {current_count}")

def characters(stringbuf):
    while True:
        c = stringbuf.read(1)
        #print(c)
        if c is None or c == "":
            break
        yield c

def run_default(start, order):
    cur = start
    curbuf = io.StringIO(cur)
    curbuf.seek(0)
    nextbuf = io.StringIO()
    try:
        for _ in range(order):
            # print("curbuf: ", curbuf.getvalue())
            curbuf.seek(0)
            next = look_and_say_seq_from_seq(characters(curbuf))
            for d in next:
                sys.stdout.write(d)
                nextbuf.write(d)
            print()
            curbuf.truncate()
            curbuf.seek(0)
            # curbuf = nextbuf
            # nextbuf = io.StringIO()
            nextbuf, curbuf = curbuf, nextbuf
    finally:
        #print("memostr cache: ", memostr.cache)
        pass


if __name__ == '__main__':
    start, order = sys.argv[1], int(sys.argv[2])
    # cur = io.StringIO(start)
    # # seq = look_and_say_seq_str(start)
    # # for _ in range(order):
    # #     print(next(seq))
    # for _ in range(order):
    #     next = look_and_say_next_str(cur)
    #     print(next.getvalue())
    #     cur.close()
    #     cur = next
    # try:
    #     cur.close()
    # except:
    #     pass

    # cur = start
    # curbuf = io.StringIO(cur)
    # curbuf.seek(0)
    # nextbuf = io.StringIO()
    # try:
    #     for _ in range(order):
    #         # print("curbuf: ", curbuf.getvalue())
    #         curbuf.seek(0)
    #         next = look_and_say_seq_from_seq(characters(curbuf))
    #         for d in next:
    #             sys.stdout.write(d)
    #             nextbuf.write(d)
    #         print()
    #         curbuf.truncate()
    #         curbuf.seek(0)
    #         # curbuf = nextbuf
    #         # nextbuf = io.StringIO()
    #         nextbuf, curbuf = curbuf, nextbuf
    # finally:
    #     #print("memostr cache: ", memostr.cache)
    #     pass

    run_default(start, order)
