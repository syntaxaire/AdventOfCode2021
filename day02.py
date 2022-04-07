def solve_part1(inputs):
    hor = 0
    dep = 0
    for line in inputs:
        cmd, distance = line.split()
        distance = int(distance)
        match cmd:
            case 'forward':
                hor += distance
            case 'up':
                dep -= distance
            case 'down':
                dep += distance
    return hor * dep


def solve_part2(inputs):
    hor = 0
    dep = 0
    aim = 0
    for line in inputs:
        cmd, distance = line.split()
        distance = int(distance)
        match cmd:
            case 'forward':
                hor += distance
                dep += (distance * aim)
            case 'up':
                aim -= distance
            case 'down':
                aim += distance
    return hor * dep


if __name__ == '__main__':
    with open('day02input.txt', 'r') as dayinputs:
        _ = dayinputs.readlines()
        print(solve_part1(_))
        print(solve_part2(_))
