"""Advent of Code 2021"""
import parsec
from anytree import Node
from enum import Enum
from itertools import zip_longest

DAY = 16

digit = parsec.regex('[0-1]')
header = digit + digit + digit


def grouper(iterable, n, fillvalue=None):
    """Collect data into non-overlapping fixed-length chunks or blocks"""
    # from https://docs.python.org/3/library/itertools.html
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def decode_literal(bitstring: str) -> int:
    """Take the literal portion of a value bitstring and return the integer equivalent."""
    literalstring = ''
    for chunk in grouper(bitstring, 5):
        literalstring += ''.join(chunk[1:])
        if chunk[0] == '0':
            # final chunk
            break
    literal = int(literalstring, 2)
    return literal


def test_decode_literal():
    assert decode_literal('101111111000101') == 2021
    assert decode_literal('101111111000101000') == 2021
    assert decode_literal('10111111100010100000000000000000000') == 2021
    assert decode_literal('01010') == 10
    assert decode_literal('1000100100') == 20
    assert decode_literal('10001001000000000') == 20


def hex_to_bitstring(hex_s):
    bitstring = ''
    for char in hex_s:
        bitstring += f'{int(char, 16):04b}'
    return bitstring


def solve_part1(inputs: list[str]):
    for line in inputs:
        bitstring = hex_to_bitstring(line.strip())


def solve_part2(inputs: list[str]):
    pass


def solve(desc, file):
    with open(file, 'r') as dayinputs:
        _ = dayinputs.readlines()
    print(f'{desc}, part 1:', solve_part1(_))
    print(f'{desc}, part 2:', solve_part2(_))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
