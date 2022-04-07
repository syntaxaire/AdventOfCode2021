"""Advent of Code 2021"""
DAY = 10

closer = {'(': ')',
          '[': ']',
          '{': '}',
          '<': '>',
          }


def score_corrupt(chars):
    total = 0
    for char in chars:
        match char:
            case ')':
                total += 3
            case ']':
                total += 57
            case '}':
                total += 1197
            case '>':
                total += 25137
    return total


def solve_part1(inputs: list[str]):
    bad_closers = []
    for line in inputs:
        stack = []
        for char in line.strip():
            if char in closer:  # an opening character
                stack.append(char)
            else:  # a closing character
                if char == closer[stack[-1]]:
                    stack.pop()
                else:
                    # received a closing character that did not match the last opener
                    bad_closers.append(char)
                    break
    return score_corrupt(bad_closers)


def solve_part2(inputs: list[str]):
    incompletes = []
    for line in inputs:
        stack = []
        corrupt = False
        for char in line.strip():
            if char in closer:  # an opening character
                stack.append(char)
            else:  # a closing character
                if char == closer[stack[-1]]:
                    stack.pop()
                else:
                    corrupt = True
                    break
        if corrupt is False:
            incompletes.append((line.strip(), ''.join(stack)[::-1]))
    worth = {'(': 1,
              '[': 2,
              '{': 3,
              '<': 4,
              }
    scores = []
    for line, stack in incompletes:
        score = 0
        for char in stack:
            score *= 5
            score += worth[char]
        scores.append(score)
    scores.sort()
    midpoint = int(len(scores)/2 - 0.5)
    return scores[midpoint]



def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
