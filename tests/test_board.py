import unittest
from game.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board_is_empty(self):
        for row in self.board.grid:
            for cell in row:
                self.assertEqual(cell, ' ')

    def test_valid_move(self):
        self.assertTrue(self.board.place_move(0, 0, 'X'))
        self.assertEqual(self.board.grid[0][0], 'X')

    def test_invalid_move_on_occupied_cell(self):
        self.board.place_move(0, 0, 'X')
        self.assertFalse(self.board.place_move(0, 0, 'O'))

    def test_winner_row(self):
        self.board.place_move(0, 0, 'X')
        self.board.place_move(0, 1, 'X')
        self.board.place_move(0, 2, 'X')
        self.assertTrue(self.board.check_winner('X'))

    def test_draw(self):
        moves = [
            (0, 0, 'X'), (0, 1, 'O'), (0, 2, 'X'),
            (1, 0, 'O'), (1, 1, 'X'), (1, 2, 'O'),
            (2, 0, 'O'), (2, 1, 'X'), (2, 2, 'O'),
        ]
        for row, col, symbol in moves:
            self.board.place_move(row, col, symbol)
        self.assertTrue(self.board.is_draw())

if __name__ == '__main__':
    unittest.main()
