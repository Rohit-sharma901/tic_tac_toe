from .board import Board
from .player import Player

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

            # Get the current player's move
            row, col = self.current_player.get_move()

            # Check if the move is valid
            if not self.board.place_move(row, col, self.current_player.symbol):
                print("Invalid move, try again.")
                continue

            # Check if there's a winner
            if self.board.check_winner(self.current_player.symbol):
                self.board.display()
                print(f"{self.current_player.name} wins!")
                break

            # Check if it's a draw
            if self.board.is_draw():
                self.board.display()
                print("It's a draw!")
                break

            # Switch to the other player
            self.switch_player()
