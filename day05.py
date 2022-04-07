from collections import Counter

DAY = 5


def iter_ortho_between_points(point1, point2):
    """For straight lines only"""
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    if dy == 0:
        # horizontal line
        start = min(point1[0], point2[0])
        end = max(point1[0], point2[0]) + 1
        for i in range(start, end):
            yield i, point2[1]
    elif dx == 0:
        # vertical line
        start = min(point1[1], point2[1])
        end = max(point1[1], point2[1]) + 1
        for i in range(start, end):
            yield point2[0], i
    else:
        # diagonal line
        return


def iter_between_points(point1, point2):
    """For straight or diagonal lines"""
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    step = max(abs(dx), abs(dy)) + 1
    if dx < 0:
        slopex = 1
    elif dx > 0:
        slopex = -1
    else:
        slopex = 0
    if dy < 0:
        slopey = 1
    elif dy > 0:
        slopey = -1
    else:
        slopey = 0
    for i in range(step):
        x = point1[0] + (i * slopex)
        y = point1[1] + (i * slopey)
        yield x, y


def parse_lines_from_inputs(inputs):
    lines = []
    for line in inputs:
        point1s, point2s = line.split(' -> ')
        x1, y1 = point1s.split(',')
        x2, y2 = point2s.split(',')
        point1 = (int(x1), int(y1))
        point2 = (int(x2), int(y2))
        lines.append((point1, point2))
    return lines


def solve_part1(inputs):
    count = Counter()
    lines = parse_lines_from_inputs(inputs)
    for line in lines:
        for point in iter_ortho_between_points(line[0], line[1]):
            count[point] += 1
    more_than_one = 0
    for point in count:
        if count[point] > 1:
            more_than_one += 1
    return more_than_one


def solve_part2(inputs):
    count = Counter()
    lines = parse_lines_from_inputs(inputs)
    for line in lines:
        for point in iter_between_points(line[0], line[1]):
            count[point] += 1
    more_than_one = 0
    for point in count:
        if count[point] > 1:
            more_than_one += 1
    return more_than_one


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
