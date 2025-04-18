class InvalidMoveError(Exception):
    """Raised when a move is not valid (e.g., out of bounds or occupied)."""
    pass

class GameOverError(Exception):
    """Raised when a move is attempted after the game has ended."""
    pass
