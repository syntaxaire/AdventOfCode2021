"""Advent of Code 2021"""
DAY = 11


class Octos:
    def __init__(self, lines):
        self.grid = []
        for line in lines:
            self.grid.append([int(_) for _ in line.strip()])
        self.flashes = 0

    def iter_squares_around(self, x, y):
        for j in (-1, 0, 1):
            for i in (-1, 0, 1):
                if i == j == 0:
                    continue
                x2 = x + i
                y2 = y + j
                if x2 < 0 or y2 < 0:
                    continue
                if x2 + 1 > len(self.grid[0]) or y2 + 1 > len(self.grid):
                    continue
                yield x2, y2

    def flash(self, x, y, flashed_this_turn: set):
        self.flashes += 1
        flashed_this_turn.add((x, y))
        for x2, y2 in self.iter_squares_around(x, y):
            if (x2, y2) not in flashed_this_turn:
                self.grid[y2][x2] += 1
        for x2, y2 in self.iter_squares_around(x, y):
            if (x2, y2) not in flashed_this_turn:
                if self.grid[y2][x2] > 9:
                    self.flash(x2, y2, flashed_this_turn)

    def step(self):
        flashed_this_turn = set()
        # first: increase all octos by 1
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                self.grid[y][x] += 1
        # second: flash any octos with an energy level greater than 9
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] > 9:
                    if (x, y) in flashed_this_turn:
                        continue
                    self.flash(x, y, flashed_this_turn)
        # third: reset any octos that flashed
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if (x, y) in flashed_this_turn:
                    self.grid[y][x] = 0
        return len(flashed_this_turn)

    def __str__(self):
        ret = ''
        for row in self.grid:
            ret += (''.join([str(_) for _ in row])) + '\n'
        return ret


def solve_part1(inputs: list[str]):
    grid = Octos(inputs)
    for i in range(100):
        grid.step()
    return grid.flashes


def solve_part2(inputs: list[str]):
    grid = Octos(inputs)
    iteration = 0
    while True:
        iteration += 1
        num_flashed = grid.step()
        if num_flashed == 100:
            return iteration


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
