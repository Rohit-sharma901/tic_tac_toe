class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self):
        # Get player move, ensuring valid input
        while True:
            try:
                row, col = map(int, input(f"{self.name} ({self.symbol}), enter your move (row col): ").split())
                return row, col
            except ValueError:
                print("Invalid input! Please enter row and column as two numbers (e.g., '1 2').")
