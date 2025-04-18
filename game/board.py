from .exceptions import InvalidMoveError

class Board:
    def __init__(self):
        self.size = 3
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def display(self):
        for row in self.grid:
            print('|'.join(row))
            print('-' * 5)

    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == ' '

    def place_move(self, row, col, symbol):
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # Check rows and columns
        for i in range(self.size):
            if all(self.grid[i][j] == symbol for j in range(self.size)):
                return True
            if all(self.grid[j][i] == symbol for j in range(self.size)):
                return True

        # Check diagonals
        if all(self.grid[i][i] == symbol for i in range(self.size)):
            return True
        if all(self.grid[i][self.size - i - 1] == symbol for i in range(self.size)):
            return True

        return False

    def is_draw(self):
        return all(self.grid[i][j] != ' ' for i in range(self.size) for j in range(self.size))

    def place_move(self, row, col, symbol):
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        raise InvalidMoveError(f"Cell ({row}, {col}) is already occupied or out of bounds.")