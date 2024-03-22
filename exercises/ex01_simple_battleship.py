"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730522247"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

Wrong_1: str = (WHITE_BOX) + (BLUE_BOX) + (BLUE_BOX) + (BLUE_BOX) + "\n Incorrect! You missed the ship."
Wrong_2: str = (BLUE_BOX) + (WHITE_BOX) + (BLUE_BOX) + (BLUE_BOX) + "\n Incorrect! You missed the ship."
Wrong_3: str = (BLUE_BOX) + (BLUE_BOX) + (WHITE_BOX) + (BLUE_BOX) + "\n Incorrect! You missed the ship."
Wrong_4: str = (BLUE_BOX) + (BLUE_BOX) + (BLUE_BOX) + (WHITE_BOX) + "\n Incorrect! You missed the ship."
Right_1: str = (RED_BOX) + (BLUE_BOX) + (BLUE_BOX) + (BLUE_BOX) + "\n Correct! You hit the ship."
Right_2: str = (BLUE_BOX) + (RED_BOX) + (BLUE_BOX) + (BLUE_BOX) + "\n Correct! You hit the ship."
Right_3: str = (BLUE_BOX) + (BLUE_BOX) + (RED_BOX) + (BLUE_BOX) + "\n Correct! You hit the ship."
Right_4: str = (BLUE_BOX) + (BLUE_BOX) + (BLUE_BOX) + (RED_BOX) + "\n Correct! You hit the ship."

boat_input: str = input("Pick a secret boat location between 1 and 4:")
boat_location: int = int(boat_input)

if boat_location < 1:
    print(f"Error! {boat_location} too low!")
    exit()
elif boat_location > 4: 
    print(f"Error! {boat_location} too high!")
    exit()


boat_inputp2: str = input("Guess a number between 1 and 4:")
boat_locationp2: int = int(boat_inputp2) 

if boat_locationp2 < 1:
    print(f"Error! {boat_locationp2} too low!")
    exit()
elif boat_locationp2 > 4: 
    print(f"Error! {boat_locationp2} too high!")
    exit()
    
if boat_locationp2 != boat_location and boat_locationp2 == 1:
    print(Wrong_1)
elif boat_locationp2 != boat_location and boat_locationp2 == 2:
    print(Wrong_2)
elif boat_locationp2 != boat_location and boat_locationp2 == 3:
    print(Wrong_3)
elif boat_locationp2 != boat_location and boat_locationp2 == 4:
    print(Wrong_4)
elif boat_locationp2 == boat_location and boat_locationp2 == 1:
    print(Right_1)
elif boat_locationp2 == boat_location and boat_locationp2 == 2:
    print(Right_2)
elif boat_locationp2 == boat_location and boat_locationp2 == 3:
    print(Right_3)
elif boat_locationp2 == boat_location and boat_locationp2 == 4:
    print(Right_4)