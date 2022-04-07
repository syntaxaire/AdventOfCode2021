"""Advent of Code 2021"""

DAY = 7


def solve_part1(inputs: list[str]):
    crabs = [int(x) for x in inputs[0].split(',')]
    top = max(crabs)
    candidates = {}
    for position in range(top):
        cost = 0
        for crab in crabs:
            cost += abs(crab - position)
        candidates[position] = cost
    costs = candidates.values()
    return min(costs)


def solve_part2(inputs: list[str]):
    crabs = [int(x) for x in inputs[0].split(',')]
    top = max(crabs)
    candidates = {}
    for position in range(top):
        cost = 0
        for crab in crabs:
            # https://oeis.org/A000217
            cost += int(abs(crab - position) * (abs(crab - position) + 1) / 2)
        candidates[position] = cost
    costs = candidates.values()
    return min(costs)


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
