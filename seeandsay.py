import sys

def digits(i):
    yield from (int(d) for d in str(i))

DIGIT_NAMES = {
    0: ("zero", "zeroes"),
    1: ("one", "one's"),
    2: ("two", "two's"),
    3: ("three", "three's"),
    4: ("four", "four's"),
    5: ("five", "five's"),
    6: ("six", "six's"),
    7: ("seven", "seven's"),
    8: ("eight", "eight's"),
    9: ("nine", "nine's"),
}

def count_digits(i):
    counts = {}
    for n in range(10):
        counts[n] = 0
    for d in digits(i):
        counts[d] += 1
    return counts

def named_counts(counts):
    out_strings = []
    for i in range(10):
        if counts[i] == 1:
            out_strings.append("1 " + DIGIT_NAMES[i][0])
        elif counts[i] > 1:
            out_strings.append(str(counts[i]) + " " + DIGIT_NAMES[i][1])
    if out_strings:
        return ", ".join(out_strings)
    else:
        return "No digits :("

if __name__ == '__main__':
    for line in sys.stdin:
        if len(line.strip()) == 0:
            line = "0"
        print(named_counts(count_digits(int(line))))
