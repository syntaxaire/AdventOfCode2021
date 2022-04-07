"""Advent of Code 2021"""
from collections import Counter, deque
from itertools import islice

DAY = 14


def get_start_from_inputs(inputs: list[str]) -> str:
    return inputs[0].strip()


def get_rules_from_inputs(inputs: list[str]) -> dict[str:str]:
    rules = {}
    for line in inputs[2:]:
        a, b = line.split(' -> ')
        rules[a] = b.strip()
    return rules


def get_rules_from_inputs_part2(inputs: list[str]) -> dict[str:str]:
    rules = {}
    for line in inputs[2:]:
        a, b = line.split(' -> ')
        rules[tuple(a)] = b.strip()
    return rules


# from recipes at https://docs.python.org/3/library/itertools.html
def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


class Polymer:
    def __init__(self, start, rules):
        self.start = start
        self.rules = rules
        self.last = (start[-2], start[-1])
        self.state = Counter()
        for pair in sliding_window(start, 2):
            self.state[pair] += 1
        pass

    def step(self):
        copy = Counter(self.state)
        for pair, num in self.state.items():
            if pair in self.rules:
                copy[pair] -= num
                copy[(pair[0], self.rules[pair])] += num
                copy[(self.rules[pair], pair[1])] += num
                if pair == self.last:
                    self.last = (self.rules[pair], pair[1])
        self.state = copy

    def total(self):
        count = Counter()
        for pair, num in self.state.items():
            count[pair[0]] += num
        count[self.last[1]] += 1
        big = max(count, key=count.get)
        small = min(count, key=count.get)
        return count[big] - count[small]

    def __str__(self):
        return str(self.state)


def solve_part1(inputs: list[str]):
    start = get_start_from_inputs(inputs)
    rules = get_rules_from_inputs_part2(inputs)
    polymer = Polymer(start, rules)
    for i in range(10):
        polymer.step()
    return polymer.total()


def solve_part2(inputs: list[str]):
    start = get_start_from_inputs(inputs)
    rules = get_rules_from_inputs_part2(inputs)
    polymer = Polymer(start, rules)
    for i in range(40):
        polymer.step()
    return polymer.total()


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
