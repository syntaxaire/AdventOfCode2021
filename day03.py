from collections import Counter


def solve_part1(inputs):
    # this puzzle involves finding the most common binary digit in a series of binary strings
    powers = [2**n for n in range(12)]
    count = Counter()
    for line in inputs:
        dec = int(line, 2)
        for power in powers:
            if power & dec:
                count[power] += 1
    gamma = 0
    epsilon = 0
    for power in powers:
        if count[power] > (len(inputs) / 2):
            # for this power of 2, binary 1 was more common than binary 0
            gamma += power
        else:
            epsilon += power
    return gamma * epsilon


def solve_part2(inputs):
    # this puzzle involves the same as above but reduces two candidate lists based on whether
    # each digit is popular or unpopular
    o2_candidates = list(inputs)
    co2_candidates = list(inputs)
    powers = [2 ** n for n in range(12)]
    powers = powers[::-1]

    # find oxygen generator rating
    for position in powers:
        count = Counter()
        for line in o2_candidates:
            # determine the full counts of '1' digits per power
            dec = int(line, 2)
            for power in powers:
                if power & dec:
                    count[power] += 1

        most_popular_digit = 1 if (count[position] > (len(o2_candidates) / 2)) else 0
        if count[position] == (len(o2_candidates) / 2):
            most_popular_digit = 1
        new_o2_candidates = []
        for candidate in o2_candidates:
            if most_popular_digit == 1 and (int(candidate, 2) & position):
                new_o2_candidates.append(candidate)
            elif most_popular_digit == 0 and not (int(candidate, 2) & position):
                new_o2_candidates.append(candidate)
        o2_candidates = new_o2_candidates
        if len(o2_candidates) == 1:
            break

    # find co2 scrubber rating
    for position in powers:
        count = Counter()
        for line in co2_candidates:
            # determine the full counts of '1' digits per power
            dec = int(line, 2)
            for power in powers:
                if power & dec:
                    count[power] += 1

        least_popular_digit = 0 if (count[position] > (len(co2_candidates) / 2)) else 1
        if count[position] == (len(co2_candidates) / 2):
            least_popular_digit = 0
        new_co2_candidates = []
        for candidate in co2_candidates:
            if least_popular_digit == 1 and (int(candidate, 2) & position):
                new_co2_candidates.append(candidate)
            elif least_popular_digit == 0 and not (int(candidate, 2) & position):
                new_co2_candidates.append(candidate)
        co2_candidates = new_co2_candidates
        if len(co2_candidates) == 1:
            break

    return int(o2_candidates[0], 2) * int(co2_candidates[0], 2)


if __name__ == '__main__':
    with open('day03input.txt', 'r') as dayinputs:
        _ = dayinputs.readlines()
        print(solve_part1(_))
        print(solve_part2(_))
