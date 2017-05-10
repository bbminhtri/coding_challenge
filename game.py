from board import Board, BoardPositionError
from player import Player


class Game(object):

    def __init__(self, win_condition):
        self._win_condition = win_condition
        self._turn = 0
        self.players = None
        self.board = None

    @property
    def win_condition(self):
        return self._win_condition

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, value):
        self._turn = value

    def start(self):
        try:
            self._turn = 0
            self.players = [
                Player('X', raw_input("Please input first player's name: ").strip().upper()),
                Player('O', raw_input("Please input second player's name: ").strip().upper())
            ]
            size = int(raw_input("Please enter the board's size: "))
            self.board = Board(size)
            self.board.display()
            self.run_game()
            self.prompt_reset()
        except (ValueError, TypeError):
            print "Invalid input. Please try again."
            self.start()

    def prompt_position(self):
        try:
            position = int(raw_input("%s's turn. Please enter next position: " % self.players[self.turn % len(self.players)].name).strip())
            return position
        except (ValueError, TypeError):
            print "Invalid position. Please input again."
            return self.prompt_position()

    def run_game(self):
        while True:
            try:
                position = self.prompt_position()
                self.board.move(self.players[self.turn % len(self.players)].symbol, position)
                self.board.display()
                if self.board.check_win(position, self.win_condition):
                    print "%s has won the game!" % self.players[self.turn % len(self.players)].name
                    break
                if self.board.check_full(self.turn + 1):
                    print "DRAW!"
                    break
                self.turn += 1
            except BoardPositionError:
                print "Invalid position. Please input again."
                continue

    def prompt_reset(self):
        ans = raw_input("Game ended. Start another game? (Y/N)").strip().upper()
        if ans == "Y":
            self.start()
