"""Advent of Code 2021"""
DAY = 8


def decode(codes):
    book = {}
    # '1' digit
    for code in codes:
        if len(code) == 2:
            book[1] = code
    # '4' digit
    for code in codes:
        if len(code) == 4:
            book[4] = code
    # '7' digit
    for code in codes:
        if len(code) == 3:
            book[7] = code
    # '8' digit
    for code in codes:
        if len(code) == 7:
            book[8] = code
    # '3' digit: has 5 segments and '1' digit is a subset of them
    five_segments = []
    for code in codes:
        if len(code) == 5:
            five_segments.append(code)
    for candidate in five_segments:
        if book[1].issubset(candidate):
            book[3] = candidate
    # '2' digit: has 5 segments, 2 of which intersect with '4' digit, and is not '3' digit
    for candidate in five_segments:
        if len(candidate.intersection(book[4])) == 2 and candidate is not book[3]:
            book[2] = candidate
    # '5' digit: is the other 5-segment digit which is not '2' or '3'
    for candidate in five_segments:
        if (candidate is not book[3]) and (candidate is not book[2]):
            book[5] = candidate
    # '9', '6' and '0' digits:
    # all have six segments, '4' is subset of '9' and '5' is a subset of '6'
    six_segments = []
    for code in codes:
        if len(code) == 6:
            six_segments.append(code)
    for candidate in six_segments:
        if book[4].issubset(candidate):
            book[9] = candidate
        elif book[5].issubset(candidate):
            book[6] = candidate
        else:
            book[0] = candidate
    return book


def get_digit(book, code):
    """Return the digit encoded by a scrambled segment given the current code book"""
    for digit, entry in book.items():
        if entry == code:
            return digit


def solve_part1(inputs: list[str]):
    uniques = 0
    for line in inputs:
        digits_strings = line.split('|')[0].split()
        outputs_strings = line.split('|')[1].split()
        digits = [set(_) for _ in digits_strings]
        outputs = [set(_) for _ in outputs_strings]
        book = decode(digits)
        for output in outputs:
            digit = get_digit(book, output)
            if digit in (1, 4, 7, 8):
                uniques += 1
    return uniques


def solve_part2(inputs: list[str]):
    finals = []
    for line in inputs:
        final = ''
        digits_strings = line.split('|')[0].split()
        outputs_strings = line.split('|')[1].split()
        digits = [set(_) for _ in digits_strings]
        outputs = [set(_) for _ in outputs_strings]
        book = decode(digits)
        for output in outputs:
            digit = get_digit(book, output)
            final += str(digit)
        finals.append(int(final))
    return sum(finals)


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
