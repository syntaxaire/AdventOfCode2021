"""Advent of Code 2021"""
from itertools import product
from collections import defaultdict

DAY = 15


class Grid:
    def __init__(self, inputs):
        self.inputs = inputs
        self.grid = []
        self.distances = []
        for line in inputs:
            row = []
            costs_row = []
            for char in line:
                if char.isdigit():
                    row.append(int(char))
                    costs_row.append(-1)
            self.grid.append(row)
            self.distances.append(costs_row)
        self.distances[0][0] = 0
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def make_part_2(self):
        # make this grid into a part 2 grid
        # first, extend the columns
        for j in range(self.height):
            orig_row = list(self.grid[j])
            for i in range(1, 5):
                self.grid[j].extend([(x + i) % 9 if (x + i) > 9 else (x + i)for x in orig_row])
        # second, extend the rows
        for copy in range(1, 5):
            for j in range(self.height):
                self.grid.append([(x + copy) % 9 if (x + copy) > 9 else (x + copy) for x in self.grid[j]])
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        # finally, make the distances grid size match the new grid
        self.distances = []
        self.distances.append([-1] * len(self.grid[0]))
        for j in range(self.height - 1):
            self.distances.append(list(self.distances[0]))
        pass


    def iter_ortho_around(self, x, y):
        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if x + i < 0 or y + j < 0 or x + i > self.width - 1 or y + j > self.height - 1:
                continue
            yield x + i, y + j

    def set_costs_from_to(self, x, y, endx, endy):
        current = (x, y)
        dest = (endx, endy)
        nodes = set(product(range(self.width), range(self.height)))
        unvisited = set(nodes)
        distances = {node:float('inf') for node in nodes}
        distances[current] = 0  # unique to this advent of code problem
        while True:
            current_distance = distances[current]
            unvisited_neighbours = set(self.iter_ortho_around(*current))
            for neighbour in unvisited_neighbours:
                neighbour_marked_distance = distances[neighbour]
                neighbour_cost = self.grid[neighbour[1]][neighbour[0]]
                neighbour_tentative_distance = current_distance + neighbour_cost
                if neighbour_tentative_distance < neighbour_marked_distance:
                    distances[neighbour] = neighbour_tentative_distance
            unvisited.remove(current)
            if current == dest:
                break
            # find smallest tentative distance among unvisited nodes
            min_tentative = ((-1, -1), float('inf'))
            for node in unvisited:
                cost = distances[node]
                if cost < min_tentative[1]:
                    min_tentative = (node, cost)
            if min_tentative[1] == float('inf'):
                break
            else:
                current = min_tentative[0]
        # write distances to self.distances for rendering
        for node, distance in distances.items():
            self.distances[node[1]][node[0]] = distance

    def print_distances(self):
        for j in range(self.height):
            for i in range(self.width):
                print(f'{str(self.distances[j][i]):>5}', end='')
            print()

    def find_lowest_path(self, start: tuple[int, int], end: tuple[int, int]):
        x, y = start
        endx, endy = end
        path = [(x, y)]
        while (x, y) != (endx, endy):
            cur_distance = self.distances[y][x]
            # find lowest neighbour
            neighbours = set(self.iter_ortho_around(x, y))
            min_distance = cur_distance
            for neighbour in neighbours:
                distance = self.distances[neighbour[1]][neighbour[0]]
                if distance < min_distance:
                    x, y = neighbour
                    min_distance = distance
            if min_distance == cur_distance:
                return path
            path.append((x, y))
        return path

    def __str__(self):
        ret = ''
        for line in self.grid:
            ret += ''.join([str(char) for char in line]) + '\n'
        return ret


def solve_part1(inputs: list[str]):
    grid = Grid(inputs)
    grid.set_costs_from_to(0, 0, grid.width, grid.height)
    grid.print_distances()
    path = grid.find_lowest_path((grid.width - 1, grid.height - 1), (0, 0))
    path = path[:-1]  # remove starting node
    total_cost = 0
    for node in path:
        total_cost += grid.grid[node[1]][node[0]]
    return total_cost


def solve_part2(inputs: list[str]):
    grid = Grid(inputs)
    grid.make_part_2()
    grid.set_costs_from_to(0, 0, grid.width, grid.height)
    path = grid.find_lowest_path((grid.width - 1, grid.height - 1), (0, 0))
    path = path[:-1]  # remove starting node
    total_cost = 0
    for node in path:
        total_cost += grid.grid[node[1]][node[0]]
    return total_cost


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
