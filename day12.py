"""Advent of Code 2021"""
DAY = 12


def load_graph(inputs: list[str]) -> dict[str:list[str]]:
    graph = {}
    for line in inputs:
        a, b = line.strip().split('-')
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def build_paths_part1(graph: dict[str:list[str]],
                      prior: list[str],
                      paths: list[list[str]],
                      start: str,
                      end: str):
    if start == end:
        path = list(prior)
        path.append(end)
        paths.append(path)
        return
    my_prior = list(prior)
    my_prior.append(start)
    for choice in graph[start]:
        if choice.islower() and choice in prior:
            continue
        build_paths_part1(graph, my_prior, paths, start=choice, end=end)


def build_paths_part2(graph: dict[str:list[str]],
                      prior: list[str],
                      paths: list[list[str]],
                      used_small_choice: bool,
                      start: str,
                      end: str):
    if start == end:
        path = list(prior)
        path.append(end)
        paths.append(path)
        return
    my_prior = list(prior)
    my_prior.append(start)
    for choice in graph[start]:
        if choice == 'start':
            continue
        if choice.islower():
            if prior.count(choice) == 2:
                continue
            elif prior.count(choice) == 1:
                if used_small_choice is True:
                    continue
                else:
                    build_paths_part2(graph, my_prior, paths, used_small_choice=True, start=choice, end=end)
            else:
                build_paths_part2(graph, my_prior, paths, used_small_choice=used_small_choice,
                                  start=choice, end=end)
        else:
            build_paths_part2(graph, my_prior, paths, used_small_choice=used_small_choice, start=choice, end=end)


def solve_part1(inputs: list[str]):
    graph = load_graph(inputs)
    prior = []
    paths = []
    build_paths_part1(graph, prior, paths, start='start', end='end')
    return len(paths)


def solve_part2(inputs: list[str]):
    graph = load_graph(inputs)
    prior = []
    paths = []
    build_paths_part2(graph, prior, paths, used_small_choice=False, start='start', end='end')
    return len(paths)


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
