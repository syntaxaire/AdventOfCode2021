import collections
from itertools import islice


def solve_part1(depths):
    prior = 0
    increases = 0
    for depth in depths:
        if depth > prior:
            increases += 1
        prior = depth
    return increases - 1


# from recipes at https://docs.python.org/3/library/itertools.html
def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def solve_part2(depths):
    prior = 0
    increases = 0
    for window in sliding_window(depths, 3):
        if sum(window) > prior:
            increases += 1
        prior = sum(window)
    return increases - 1


if __name__ == '__main__':
    with open('day01input.txt', 'r') as day1inputs:
        day1inputs = [int(x) for x in day1inputs.readlines()]
        print(solve_part1(day1inputs))
        print(solve_part2(day1inputs))
