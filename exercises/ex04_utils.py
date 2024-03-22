"""EX04 - list Utility Functions."""

__author__ = "730522247"


def all(options: list[int], choice: int) -> bool:
    """Returns a boolean value if all integers are the same in the list as a chosen integer."""
    if not options:
        return False
    idx = 0
    while idx < len(options):
        if options[idx] != choice:
            return False
        idx += 1
    return True 


def max(options: list[int]) -> int:
    """Returns the largest integer in a given list."""
    if len(options) == 0:
        raise ValueError("max() arg is an empty List")
    max_int = options[0]
    idx = 0
    while idx < len(options):
        if options[idx] > max_int:
            max_int = options[idx]
        idx += 1
    return max_int


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Evaluates if each list at each index is equal."""
    if len(first_list) != len(second_list):
        return False 
    for idx in range(len(first_list)):
        if first_list[idx] != second_list[idx]:
            return False
    return True


def extend(first_list: list[int], second_list: list[int]) -> None:
    """Mutating two lists."""
    for idx in range(len(second_list)):
        first_list.append(second_list[idx])