"""EX05 - Dictionary Utility Functions."""

__author__ = "730522247"


def invert(input_dictionary: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values in a dictionary."""
    new_dictionary: dict[str, str] = {}
    for key in input_dictionary:
        value = input_dictionary[key]
        if value in new_dictionary:
            raise KeyError("Duplicate value found, unable to invert the dictionary.")
        new_dictionary[value] = key
    return new_dictionary


def favorite_color(input_dictionary: dict[str, str]) -> str:
    """Determines highest frequency of a favorite color."""
    most_color: str = ""
    idx_max = 0
    for color_choice in input_dictionary.values():
        idx = 0
        for value in input_dictionary.values():
            if value == color_choice:
                idx += 1 
        if idx > idx_max or (idx == idx_max and color_choice not in input_dictionary):
            idx_max = idx
            most_color = color_choice
    return most_color


def count(input_list: list[str]) -> dict[str, int]:
    """Produces a dictionary tracking frequency/value of a character."""
    new_dictionary: dict[str, int] = {}
    for value in input_list:
        if value in new_dictionary:
            new_dictionary[value] += 1
        else:
            new_dictionary[value] = 1
    return new_dictionary


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Categorizes words into lists by starting letter."""
    new_dictionary: dict[str, list[str]] = {} 
    for value in word_list:
        first_letter = value[0].lower()
        if 'a' <= first_letter <= 'z':
            if first_letter in new_dictionary:
                new_dictionary[first_letter].append(value)
            else:
                new_dictionary[first_letter] = [value]
    return new_dictionary


def update_attendance(attendance_dictionary: dict[str, list[str]], day: str, student: str) -> None:
    """Updating an existing dictionary for student attendance."""
    if day in attendance_dictionary:
        attendance_dictionary[day].append(student)
    else:
        attendance_dictionary[day] = [student] 