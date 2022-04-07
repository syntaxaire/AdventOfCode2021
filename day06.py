"""Advent of Code 2021"""
from collections import Counter

DAY = 6


def simulate_fish_naive(inputs: list[int], iterations):
    for n in range(iterations):
        for i in range(len(inputs)):
            if inputs[i] > 0:
                inputs[i] = inputs[i] - 1
            elif inputs[i] == 0:
                inputs[i] = 6
                inputs.append(8)
            else:
                raise ValueError
    return len(inputs)


def simulate_fish_counter(inputs: list[int], iterations):
    count = Counter(inputs)
    for n in range(iterations):
        new_count = Counter()
        for time, num in count.items():
            if time == 0:
                new_count[8] += num
                new_count[0] -= 0
                new_count[6] += num
            else:
                new_count[time - 1] += num
        count = new_count
    return count.total()


def solve_part1(inputs: list[str]):
    iterations = 80
    line = inputs[0]
    fish = [int(n) for n in line.split(',')]
    return simulate_fish_counter(fish, iterations)


def solve_part2(inputs: list[str]):
    iterations = 256
    line = inputs[0]
    fish = [int(n) for n in line.split(',')]
    return simulate_fish_counter(fish, iterations)


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
