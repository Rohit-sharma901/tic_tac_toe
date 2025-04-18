from .board import Board
from .player import Player
from .exceptions import InvalidMoveError


class Game:
    def __init__(self, player1_name, player2_name):
        self.board = Board()
        self.player1 = Player(player1_name, 'X')
        self.player2 = Player(player2_name, 'O')
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play(self):
        while True:
            self.board.display()
            print(f"{self.current_player.name}'s turn ({self.current_player.symbol})")

            try:
                row, col = self.current_player.get_move()
                self.board.place_move(row, col, self.current_player.symbol)
            except InvalidMoveError as e:
                print(e)
                continue

            if self.board.check_winner(self.current_player.symbol):
                self.board.display()
                print(f"{self.current_player.name} wins!")
                break

            if self.board.is_draw():
                self.board.display()
                print("It's a draw!")
                break

            self.switch_player()