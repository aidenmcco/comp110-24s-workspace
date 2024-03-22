"""EX03 - Functional Battleship."""

__author__ = "730522247"
import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, user_guess: str) -> int:
    """Prompting an input guess."""
    assert user_guess == "row" or user_guess == "column"
    if user_guess == "row":
        prompt = "Guess a row"
    else:
        prompt = "Guess a column"
    guess = int(input(f"{prompt}: "))
    while guess < 1 or guess > grid_size:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        guess = int(input(f"{prompt}: "))
    return guess 


def print_grid(grid_size: int, row_guess: int, col_guess: int, correct_guess: bool) -> None:
    """Print an emoji grid."""
    idx_row = 1
    while idx_row <= grid_size:
        idx_column = 1
        box_print = ""
        while idx_column <= grid_size:
            if idx_row == row_guess and idx_column == col_guess:
                if correct_guess:
                    box_print += RED_BOX
                else:
                    box_print += WHITE_BOX
            else:
                box_print += BLUE_BOX
            idx_column += 1
        print(box_print)
        idx_row += 1


def correct_guess(secret_row: int, secret_col: int, row_guess: int, col_guess: int) -> bool:
    """Establishing a secret row and column."""
    return secret_row == row_guess and secret_col == col_guess
    

def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """Playing a game of battleship using functions."""
    total_turns = 5
    player_turn = 0
    while player_turn < total_turns:
        player_turn += 1
        print(f"=== Turn {player_turn}/5 ===")
        row_guess = input_guess(grid_size, "row")
        col_guess = input_guess(grid_size, "column")
        correct = correct_guess(secret_row, secret_col, row_guess, col_guess)
        print_grid(grid_size, row_guess, col_guess, correct)
        if correct:
            print("Hit!")
            print(f"You won in {player_turn}/{total_turns} turns!")
            return
        else:
            print("Miss!")
    print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))