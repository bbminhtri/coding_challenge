class BoardPositionError(Exception):
    pass


class Board(object):
    def __init__(self, size):
        self._size = size
        self._board = [['.' for i in xrange(self.size)] for j in xrange(0, self.size)]

    @property
    def size(self):
        return self._size

    @property
    def board(self):
        return self._board

    def _first_diagonal_check(self, row, col):
        symbol = self.board[row][col]
        count = 1
        r = row
        c = col
        while r - 1 >= 0 and c - 1 >= 0 and self.board[r - 1][c - 1] == symbol:
            count += 1
            r -= 1
            c -= 1
        r = row
        c = col
        while r + 1 < self.size and c + 1 < self.size and self.board[r + 1][c + 1] == symbol:
            count += 1
            r += 1
            c += 1
        return count

    def _second_diagonal_check(self, row, col):
        symbol = self.board[row][col]
        count = 1
        r = row
        c = col
        while r - 1 >= 0 and c + 1 < self.size and self.board[r - 1][c + 1] == symbol:
            count += 1
            r -= 1
            c += 1
        r = row
        c = col
        while r + 1 < self.size and c - 1 >= 0 and self.board[r + 1][c - 1] == symbol:
            count += 1
            r += 1
            c -= 1
        return count

    def _column_check(self, row, col):
        symbol = self.board[row][col]
        count = 1
        r = row
        while r - 1 >= 0 and self.board[r - 1][col] == symbol:
            count += 1
            r -= 1
        r = row
        while r + 1 < self.size and self.board[r + 1][col] == symbol:
            count += 1
            r += 1
        return count

    def _row_check(self, row, col):
        symbol = self.board[row][col]
        count = 1
        c = col
        while c - 1 >= 0 and self.board[row][c - 1] == symbol:
            count += 1
            c -= 1
        c = col
        while c + 1 < self.size and self.board[row][c + 1] == symbol:
            count += 1
            c += 1
        return count

    def valid_position(self, position):
        return 1 <= position <= self.size * self.size

    def check_win(self, position, win_condition):
        try:
            if not self.valid_position(position):
                raise BoardPositionError()
            row = (position - 1) / self.size
            col = (position - 1) % self.size
            if self._first_diagonal_check(row, col) >= win_condition:
                return True
            if self._second_diagonal_check(row, col) >= win_condition:
                return True
            if self._column_check(row, col) >= win_condition:
                return True
            if self._row_check(row, col) >= win_condition:
                return True
            return False
        except IndexError:
            raise BoardPositionError()

    def display(self):
        for i in xrange(self.size):
            row = ''
            for j in range(self.size):
                if j > 0:
                    row += '|'
                if self.board[i][j] != '.':
                    row += '   %s ' % self.board[i][j]
                else:
                    row += ' {0:3} '.format(i * self.size + j + 1)
            print row

    def move(self, symbol, position):
        try:
            if not self.valid_position(position):
                raise BoardPositionError()
            row = (position - 1) / self.size
            col = (position - 1) % self.size
            if self.board[row][col] != '.':
                raise BoardPositionError()
            self.board[row][col] = symbol
        except IndexError:
            raise BoardPositionError()

    def check_full(self, tile_no):
        return tile_no >= self.size * self.size
