"""EX02 - One Shot Battleship."""

__author__ = "730522247"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

result: str
row_counter: int = 1
column_counter: int = 1
box_print: str = ""

correct: bool = False
row_correct: bool = False
column_correct: bool = False

while not row_correct:
    row_choice: int = int(input("Guess a row: "))
    if row_choice > 4:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    elif row_choice < 1:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    else: 
        row_correct = True
while not column_correct:
    column_choice: int = int(input("Guess a column: "))  
    if column_choice > 4:
        print("The grid is only 4 by 4. Try again: ")
    elif column_choice < 1:
        print("The grid is only 4 by 4. Try again: ")
    else:
        column_correct = True

if row_choice == secret_row and column_choice == secret_column:
    result = RED_BOX
else:
    result = WHITE_BOX

while not correct:
    row_counter = 1 
    while row_counter <= grid_size:
        column_counter = 1  
        while column_counter <= grid_size:
            if row_choice == row_counter and column_choice == column_counter:
                box_print += result
            else:
                box_print += BLUE_BOX
            column_counter += 1
        print(box_print)
        row_counter += 1
        box_print = "" 
    if row_choice == secret_row and column_choice != secret_column:
        print("Close! Correct row, wrong column.")
        break
    elif row_choice != secret_row and column_choice == secret_column:
        print("Close! Correct column, wrong row.")
        break
    elif row_choice != secret_row and column_choice != secret_column:
        print("Miss!")
        break
    elif row_choice == secret_row and column_choice == secret_column:
        print("Hit!")
        break