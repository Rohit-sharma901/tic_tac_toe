from game.game import Game

def main():
    print("Welcome to Tic Tac Toe!")

    # Get player names
    player1_name = input("Enter name for Player 1 (X): ")
    player2_name = input("Enter name for Player 2 (O): ")

    # Initialize the game
    game = Game(player1_name, player2_name)

    # Start the game
    game.play()

if __name__ == "__main__":
    main()
