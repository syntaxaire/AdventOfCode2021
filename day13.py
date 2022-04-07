"""Advent of Code 2021"""
DAY = 13


class Paper:
    def __init__(self, sizex: int, sizey: int, coords: list[tuple[int, int]]):
        self.sizex = sizex
        self.sizey = sizey
        self.coords = set(coords)

    def __str__(self):
        ret = ''
        for j in range(self.sizey + 1):
            for i in range(self.sizex + 1):
                if (i, j) in self.coords:
                    ret +='#'
                else:
                    ret += '.'
            ret += '\n'
        return ret

    def count(self):
        return len(self.coords)

    def fold(self, axis: str, index: int):
        new_coords = set()
        for x, y in self.coords:
            if (axis == 'x' and x == index) or (axis == 'y' and y == index):
                # drop this point, it is on the fold
                continue
            if axis == 'x':
                if x > index:
                    new_coords.add((index - (x - index), y))
                else:
                    new_coords.add((x, y))
            if axis == 'y':
                if y > index:
                    new_coords.add((x, (index - (y - index))))
                else:
                    new_coords.add((x, y))
        if axis == 'x':
            self.sizex = index - 1
        elif axis == 'y':
            self.sizey = index - 1
        self.coords = new_coords


def paper_from_inputs(inputs):
    coords = []
    max_x = 0
    max_y = 0
    for line in inputs:
        if line[0].isdigit():
            xs, ys = line.split(',')
            x = int(xs)
            y = int(ys)
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            coords.append((int(xs), int(ys)))
    return Paper(max_x, max_y, coords)


def folds_from_inputs(inputs):
    folds = []
    for line in inputs:
        if line.startswith('fold'):
            direction, index = line.split('=')
            axis = direction[-1]
            index = int(index)
            folds.append((axis, index))
    return folds


def solve_part1(inputs: list[str]):
    paper = paper_from_inputs(inputs)
    folds = folds_from_inputs(inputs)
    paper.fold(*folds[0])
    return paper.count()


def solve_part2(inputs: list[str]):
    paper = paper_from_inputs(inputs)
    folds = folds_from_inputs(inputs)
    for fold in folds:
        paper.fold(*fold)
    print(paper)


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
