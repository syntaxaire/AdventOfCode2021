import itertools


class BingoCard:
    def __init__(self, dimx, dimy, numbers):
        self.dimx = dimx
        self.dimy = dimy
        self.grid = []
        self.marked = []
        self.winner = False
        for j in range(dimy):
            pos = j * dimx
            self.grid.append(list(numbers[pos:pos + dimx]))

    def mark_number(self, num):
        self.marked.append(num)
        self.check_if_winner()

    def check_if_winner(self):
        # check rows
        for row in self.grid:
            if all(pos in self.marked for pos in row):
                self.winner = True
                return
        # check columns
        for i in range(self.dimx):
            col_wins = True
            for row in self.grid:
                if row[i] not in self.marked:
                    col_wins = False
            if col_wins:
                self.winner = True
                return

    def get_checksum(self):
        val = 0
        for j in self.grid:
            for i in j:
                if i not in self.marked:
                    val += int(i)
        return val * int(self.marked[-1])

    def __repr__(self):
        ret = ''
        for j in self.grid:
            for i in j:
                ret += f'{i:3}'
            ret += '\n'
        return ret

    def __str__(self):
        ret = ''
        for j in self.grid:
            for i in j:
                if i in self.marked:
                    ret += f'{i:3}'
                else:
                    ret += '   '
            ret += '\n'
        return ret


def bingo_card_from_lines(lines: list):
    dimx = len(lines[0].split())
    dimy = len(lines)
    numbers = []
    for line in lines:
        numbers.extend(line.split())
    card = BingoCard(dimx, dimy, numbers)
    return card


def solve_part1(bingo_cards, draws):
    for draw in draws:
        for card in bingo_cards:
            card.mark_number(draw)
            if card.winner:
                break
        if card.winner:
            break
    print(card)
    print(card.get_checksum())


def solve_part2(bingo_cards, draws):
    # 12177 wrong
    candidates = set(bingo_cards)
    for draw in draws:
        print(draw)
        for card in bingo_cards:
            card.mark_number(draw)
            if card.winner and len(candidates) > 1 and card in candidates:
                candidates.remove(card)
        print(f'Candidates: {len(candidates)}')
        if len(candidates) == 1:
            final = list(candidates)[0]
            # continue playing until final wins
            if final.winner:
                break
    print(final)
    print(final.get_checksum())


if __name__ == '__main__':
    with open('day04input.txt', 'r') as dayinputs:
        draws = dayinputs.readline().split(',')
        bingo_cards = []
        current_grid = []
        for line in dayinputs.readlines():
            if len(line) > 1:
                current_grid.append(line)
            else:
                if len(current_grid) > 0:
                    bingo_cards.append(bingo_card_from_lines(current_grid))
                    current_grid = []
        # catch final grid if there was no following empty line
        if len(current_grid) > 0:
            bingo_cards.append(bingo_card_from_lines(current_grid))
    solve_part1(bingo_cards, draws)
    solve_part2(bingo_cards, draws)


    # print(solve_part1(_))
    # print(solve_part2(_))
