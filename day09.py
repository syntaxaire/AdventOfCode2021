"""Advent of Code 2021"""
DAY = 9


def is_local_minimum(arr, x, y):
    """Return whether a point is the lowest point in its surroundings."""
    compare = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i, j in compare:
        try:
            if x + i == -1 or y + j == -1:  # guard against reading the end of a different line
                continue
            if arr[y + j][x + i] <= arr[y][x]:
                return False
        except IndexError:
            pass
    return True


def find_basin(arr, x, y, found: set) -> list[tuple]:
    """Take a point and add to a Set of all points in its basin as tuples. Recursive."""
    if x < 0 or y < 0:
        # guard against underflow
        return
    try:
        if arr[y][x] == 9:
            return
    except IndexError:
        # out of bounds
        return
    if (x, y) in found:
        return
    found.add((x, y))
    compare = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i, j in compare:
        find_basin(arr, x+i, y+j, found)


def solve_part1(inputs: list[str]):
    total = 0
    dimy = len(inputs)
    dimx = len(inputs[0].strip())
    grid = []
    for line in inputs:
        stripped = line.strip()
        grid.append([int(n) for n in stripped])
    for j in range(dimy):
        for i in range(dimx):
            if is_local_minimum(grid, i, j):
                total += 1 + grid[j][i]
    return total  # 1624 too high, 522 too low


def solve_part2(inputs: list[str]):
    total = 0
    dimy = len(inputs)
    dimx = len(inputs[0].strip())
    grid = []
    minima = []
    for line in inputs:
        stripped = line.strip()
        grid.append([int(n) for n in stripped])
    for j in range(dimy):
        for i in range(dimx):
            if is_local_minimum(grid, i, j):
                minima.append((i, j))
    basins = []
    for x, y in minima:
        found = set()
        find_basin(grid, x, y, found)
        basins.append(found)
    basins.sort(key=len, reverse=True)
    return len(basins[0]) * len(basins[1]) * len(basins[2])


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
